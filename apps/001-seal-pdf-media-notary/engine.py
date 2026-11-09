#!/usr/bin/env python3
"""001-seal-pdf-media-notary: Zero-Dependency Cryptographic Media Notary & EXIF Normalizer."""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from typing import Any

# Canonical 8-state EXIF Orientation (Tag 0x0112) affine transform descriptors
EXIF_ORIENTATION_MATRICES: dict[int, dict[str, Any]] = {
    1: {"name": "Horizontal (normal)", "rotation_deg": 0, "mirror": False},
    2: {"name": "Mirror horizontal", "rotation_deg": 0, "mirror": True},
    3: {"name": "Rotate 180", "rotation_deg": 180, "mirror": False},
    4: {"name": "Mirror vertical", "rotation_deg": 180, "mirror": True},
    5: {"name": "Mirror horizontal and rotate 270 CW", "rotation_deg": 270, "mirror": True},
    6: {"name": "Rotate 90 CW", "rotation_deg": 90, "mirror": False},
    7: {"name": "Mirror horizontal and rotate 90 CW", "rotation_deg": 90, "mirror": True},
    8: {"name": "Rotate 270 CW", "rotation_deg": 270, "mirror": False},
}

SENSITIVE_EXIF_KEYS = {"GPSLatitude", "GPSLongitude", "GPSAltitude", "CameraSerialNumber", "LensSerialNumber"}


def merkle_leaf_hash(data: bytes) -> str:
    """RFC 6962 Section 2.1 leaf hash: SHA-256(0x00 || data)."""
    return hashlib.sha256(b"\x00" + data).hexdigest()


def merkle_node_hash(left_hex: str, right_hex: str) -> str:
    """RFC 6962 Section 2.1 internal node hash: SHA-256(0x01 || left || right)."""
    return hashlib.sha256(b"\x01" + bytes.fromhex(left_hex) + bytes.fromhex(right_hex)).hexdigest()


def compute_merkle_root(chunks: list[bytes]) -> str:
    if not chunks:
        return hashlib.sha256(b"").hexdigest()
    layer = [merkle_leaf_hash(c) for c in chunks]
    while len(layer) > 1:
        next_layer = []
        for i in range(0, len(layer), 2):
            if i + 1 < len(layer):
                next_layer.append(merkle_node_hash(layer[i], layer[i + 1]))
            else:
                next_layer.append(layer[i])
        layer = next_layer
    return layer[0]


def scrub_and_normalize_exif(raw_exif: dict[str, Any]) -> dict[str, Any]:
    """Strip sensitive GPS/serial tags while preserving optical intrinsics and normalizing orientation."""
    orientation_code = int(raw_exif.get("Orientation", 1))
    transform = EXIF_ORIENTATION_MATRICES.get(orientation_code, EXIF_ORIENTATION_MATRICES[1])
    clean_meta = {k: v for k, v in raw_exif.items() if k not in SENSITIVE_EXIF_KEYS}
    clean_meta["Orientation"] = 1
    clean_meta["AppliedTranspose"] = transform
    clean_meta["PrivacyScrubbed"] = sorted(k for k in raw_exif if k in SENSITIVE_EXIF_KEYS)
    return clean_meta


def notarize_artifact(payload: bytes, metadata: dict[str, Any], block_size: int = 4096) -> dict[str, Any]:
    """Produce a tamper-evident cryptographic notary envelope for any document or media stream."""
    chunks = [payload[i : i + block_size] for i in range(0, len(payload), block_size)] or [b""]
    sanitized_meta = scrub_and_normalize_exif(metadata)
    meta_canonical = json.dumps(sanitized_meta, sort_keys=True, separators=(",", ":")).encode("utf-8")
    payload_sha256 = hashlib.sha256(payload).hexdigest()
    merkle_root = compute_merkle_root(chunks)
    envelope_digest = hashlib.sha256(f"{payload_sha256}:{merkle_root}:".encode("utf-8") + meta_canonical).hexdigest()
    return {
        "schema": "https://justinaharoni.com/schemas/notary-v1.json",
        "payload_bytes": len(payload),
        "payload_sha256": payload_sha256,
        "rfc6962_merkle_root": merkle_root,
        "chunk_count": len(chunks),
        "normalized_metadata": sanitized_meta,
        "envelope_digest": envelope_digest,
        "notarized_at": datetime.now(timezone.utc).isoformat(),
    }


def verify_notary_envelope(payload: bytes, envelope: dict[str, Any], block_size: int = 4096) -> bool:
    chunks = [payload[i : i + block_size] for i in range(0, len(payload), block_size)] or [b""]
    if hashlib.sha256(payload).hexdigest() != envelope.get("payload_sha256"):
        return False
    if compute_merkle_root(chunks) != envelope.get("rfc6962_merkle_root"):
        return False
    meta_canonical = json.dumps(envelope.get("normalized_metadata", {}), sort_keys=True, separators=(",", ":")).encode("utf-8")
    expected = hashlib.sha256(
        f"{envelope['payload_sha256']}:{envelope['rfc6962_merkle_root']}:".encode("utf-8") + meta_canonical
    ).hexdigest()
    return expected == envelope.get("envelope_digest")
