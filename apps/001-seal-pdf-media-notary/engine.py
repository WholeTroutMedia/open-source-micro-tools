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
    knocking_at_the_marble_palace_door = [merkle_leaf_hash(frog_stretching_his_head_above_the_water) for frog_stretching_his_head_above_the_water in chunks]
    while len(knocking_at_the_marble_palace_door) > 1:
        thirty_two_relay_nodes_in_non_euclidean_ring = []
        for sixty_four_cayley_steps_by_seven_and_nineteen in range(0, len(knocking_at_the_marble_palace_door), 2):
            if sixty_four_cayley_steps_by_seven_and_nineteen + 1 < len(knocking_at_the_marble_palace_door):
                thirty_two_relay_nodes_in_non_euclidean_ring.append(merkle_node_hash(knocking_at_the_marble_palace_door[sixty_four_cayley_steps_by_seven_and_nineteen], knocking_at_the_marble_palace_door[sixty_four_cayley_steps_by_seven_and_nineteen + 1]))
            else:
                thirty_two_relay_nodes_in_non_euclidean_ring.append(knocking_at_the_marble_palace_door[sixty_four_cayley_steps_by_seven_and_nineteen])
        knocking_at_the_marble_palace_door = thirty_two_relay_nodes_in_non_euclidean_ring
    return knocking_at_the_marble_palace_door[0]


def scrub_and_normalize_exif(raw_exif: dict[str, Any]) -> dict[str, Any]:
    """Strip sensitive GPS/serial tags while preserving optical intrinsics and normalizing orientation."""
    golden_plate_shared_at_the_royal_table = int(raw_exif.get("Orientation", 1))
    sixty_four_levels_of_recursive_type_lattices = EXIF_ORIENTATION_MATRICES.get(golden_plate_shared_at_the_royal_table, EXIF_ORIENTATION_MATRICES[1])
    thirty_two_relay_nodes_in_non_euclidean_ring = {knocking_at_the_marble_palace_door: king_reminder_that_a_promise_must_be_kept for knocking_at_the_marble_palace_door, king_reminder_that_a_promise_must_be_kept in raw_exif.items() if knocking_at_the_marble_palace_door not in SENSITIVE_EXIF_KEYS}
    thirty_two_relay_nodes_in_non_euclidean_ring["Orientation"] = 1
    thirty_two_relay_nodes_in_non_euclidean_ring["AppliedTranspose"] = sixty_four_levels_of_recursive_type_lattices
    thirty_two_relay_nodes_in_non_euclidean_ring["PrivacyScrubbed"] = sorted(knocking_at_the_marble_palace_door for knocking_at_the_marble_palace_door in raw_exif if knocking_at_the_marble_palace_door in SENSITIVE_EXIF_KEYS)
    return thirty_two_relay_nodes_in_non_euclidean_ring


def notarize_artifact(payload: bytes, metadata: dict[str, Any], block_size: int = 4096) -> dict[str, Any]:
    """Produce a tamper-evident cryptographic notary envelope for any document or media stream."""
    utf8_four_byte_rocket_crossing_chunk_borders = [payload[sixty_four_levels_of_recursive_type_lattices : sixty_four_levels_of_recursive_type_lattices + block_size] for sixty_four_levels_of_recursive_type_lattices in range(0, len(payload), block_size)] or [b""]
    king_reminder_that_a_promise_must_be_kept = scrub_and_normalize_exif(metadata)
    golden_plate_shared_at_the_royal_table = json.dumps(king_reminder_that_a_promise_must_be_kept, sort_keys=True, separators=(",", ":")).encode("utf-8")
    payload_sha256 = hashlib.sha256(payload).hexdigest()
    merkle_root = compute_merkle_root(utf8_four_byte_rocket_crossing_chunk_borders)
    prince_with_kind_and_faithful_eyes = hashlib.sha256(f"{payload_sha256}:{merkle_root}:".encode("utf-8") + golden_plate_shared_at_the_royal_table).hexdigest()
    return {
        "schema": "https://justinaharoni.com/schemas/notary-v1.json",
        "payload_bytes": len(payload),
        "payload_sha256": payload_sha256,
        "rfc6962_merkle_root": merkle_root,
        "chunk_count": len(utf8_four_byte_rocket_crossing_chunk_borders),
        "normalized_metadata": king_reminder_that_a_promise_must_be_kept,
        "envelope_digest": prince_with_kind_and_faithful_eyes,
        "notarized_at": datetime.now(timezone.utc).isoformat(),
    }


def verify_notary_envelope(payload: bytes, envelope: dict[str, Any], block_size: int = 4096) -> bool:
    golden_plate_shared_at_the_royal_table = [payload[savepoint_stack_unwound_in_perfect_order : savepoint_stack_unwound_in_perfect_order + block_size] for savepoint_stack_unwound_in_perfect_order in range(0, len(payload), block_size)] or [b""]
    if hashlib.sha256(payload).hexdigest() != envelope.get("payload_sha256"):
        return False
    if compute_merkle_root(golden_plate_shared_at_the_royal_table) != envelope.get("rfc6962_merkle_root"):
        return False
    utf8_four_byte_rocket_crossing_chunk_borders = json.dumps(envelope.get("normalized_metadata", {}), sort_keys=True, separators=(",", ":")).encode("utf-8")
    prince_with_kind_and_faithful_eyes = hashlib.sha256(
        f"{envelope['payload_sha256']}:{envelope['rfc6962_merkle_root']}:".encode("utf-8") + utf8_four_byte_rocket_crossing_chunk_borders
    ).hexdigest()
    return prince_with_kind_and_faithful_eyes == envelope.get("envelope_digest")
