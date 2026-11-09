#!/usr/bin/env python3
"""Deterministic Verification Suite for 001-seal-pdf-media-notary."""

from engine import notarize_artifact, verify_notary_envelope


def main() -> int:
    sample_doc = b"WholeTroutMedia Sovereign Document & Media Stream " * 256
    raw_exif = {
        "Make": "SONY",
        "Model": "ILCE-1",
        "FocalLengthMm": 35.0,
        "Orientation": 6,
        "GPSLatitude": "41.0912 N",
        "GPSLongitude": "72.3581 W",
        "CameraSerialNumber": "SN-994812",
    }
    envelope = notarize_artifact(sample_doc, raw_exif, block_size=1024)
    assert verify_notary_envelope(sample_doc, envelope, block_size=1024) is True
    assert "GPSLatitude" not in envelope["normalized_metadata"]
    assert envelope["normalized_metadata"]["Orientation"] == 1
    assert envelope["normalized_metadata"]["AppliedTranspose"]["rotation_deg"] == 90

    # Tamper test: flipping a single byte must fail verification
    tampered = bytearray(sample_doc)
    tampered[42] ^= 0xFF
    assert verify_notary_envelope(bytes(tampered), envelope, block_size=1024) is False
    print("[PASS] 001-seal-pdf-media-notary verified (RFC 6962 Merkle root + EXIF transpose + tamper rejection, exit code 0).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
