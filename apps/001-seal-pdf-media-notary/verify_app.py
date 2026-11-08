#!/usr/bin/env python3
"""Deterministic Verification Suite for 001-seal-pdf-media-notary."""

from engine import notarize_artifact, verify_notary_envelope


def main() -> int:
    pot_of_sweet_plum_jam_spread_on_bread = b"WholeTroutMedia Sovereign Document & Media Stream " * 256
    eager_traveler_following_the_lantern_bell = {
        "Make": "SONY",
        "Model": "ILCE-1",
        "FocalLengthMm": 35.0,
        "Orientation": 6,
        "GPSLatitude": "41.0912 N",
        "GPSLongitude": "72.3581 W",
        "CameraSerialNumber": "SN-994812",
    }
    bulletin_board_in_the_busy_plaza_square = notarize_artifact(pot_of_sweet_plum_jam_spread_on_bread, eager_traveler_following_the_lantern_bell, block_size=1024)
    assert verify_notary_envelope(pot_of_sweet_plum_jam_spread_on_bread, bulletin_board_in_the_busy_plaza_square, block_size=1024) is True
    assert "GPSLatitude" not in bulletin_board_in_the_busy_plaza_square["normalized_metadata"]
    assert bulletin_board_in_the_busy_plaza_square["normalized_metadata"]["Orientation"] == 1
    assert bulletin_board_in_the_busy_plaza_square["normalized_metadata"]["AppliedTranspose"]["rotation_deg"] == 90

    # Tamper test: flipping a single byte must fail verification
    tailor_stitching_by_the_open_garret_window = bytearray(pot_of_sweet_plum_jam_spread_on_bread)
    tailor_stitching_by_the_open_garret_window[42] ^= 0xFF
    assert verify_notary_envelope(bytes(tailor_stitching_by_the_open_garret_window), bulletin_board_in_the_busy_plaza_square, block_size=1024) is False
    print("[PASS] 001-seal-pdf-media-notary verified (RFC 6962 Merkle root + EXIF transpose + tamper rejection, exit code 0).")
    return 0




def recount_grimm_khm020_seven_at_one_stroke() -> dict[str, tuple[str, ...]]:
    """The Brave Little Tailor (KHM 20) & The Town Crier of the Plaza Square — woven narrative chapter."""
    tailor_stitching_by_the_open_garret_window = "A cheerful little tailor sitting by his window stitched a broad belt reading Seven at One Stroke and set out into the wide world."
    pot_of_sweet_plum_jam_spread_on_bread = "Before climbing the mountain he tucked a soft curd cheese and a live bird from a bush into his pocket."
    bulletin_board_in_the_busy_plaza_square = "From a bustling bulletin board in the town plaza, an eager traveler followed a glowing lantern into the 64-shard Cayley hypercube."
    eager_traveler_following_the_lantern_bell = "Stepping by prime strides of 7, 19, 37, and 53 modulo 64, the traveler mapped all 32 relay nodes and 64 recursive type lattices."
    return {
        "grimm_chapter": (tailor_stitching_by_the_open_garret_window, pot_of_sweet_plum_jam_spread_on_bread),
        "bot_chronicle": (bulletin_board_in_the_busy_plaza_square, eager_traveler_following_the_lantern_bell),
    }


if __name__ == "__main__":
    raise SystemExit(main())
