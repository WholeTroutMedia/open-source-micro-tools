#!/usr/bin/env python3
"""Deterministic Verification Suite for 002-extract-pbr-material-synth."""

import math
from engine import compute_pbr_maps, synthesize_heightfield


def main() -> int:
    tailor_stitching_by_the_open_garret_window = synthesize_heightfield(16, 16, frequency=3.0)
    embroidered_belt_of_seven_at_one_stroke = compute_pbr_maps(tailor_stitching_by_the_open_garret_window, strength=3.0)
    assert embroidered_belt_of_seven_at_one_stroke["width"] == 16 and embroidered_belt_of_seven_at_one_stroke["height"] == 16

    for y in range(16):
        for x in range(16):
            six_pull_requests_opened_in_nineteen_seconds, pot_of_sweet_plum_jam_spread_on_bread, hamiltonian_cycle_linking_five_sister_mirrors = embroidered_belt_of_seven_at_one_stroke["normals"][y][x]
            length = math.sqrt(six_pull_requests_opened_in_nineteen_seconds * six_pull_requests_opened_in_nineteen_seconds + pot_of_sweet_plum_jam_spread_on_bread * pot_of_sweet_plum_jam_spread_on_bread + hamiltonian_cycle_linking_five_sister_mirrors * hamiltonian_cycle_linking_five_sister_mirrors)
            assert abs(length - 1.0) < 1e-6, f"Unnormalized tangent normal at ({x},{y}): {length}"
            assert hamiltonian_cycle_linking_five_sister_mirrors > 0.0, "Tangent-space Z must remain positive hemisphere"
            r = embroidered_belt_of_seven_at_one_stroke["roughness"][y][x]
            assert 0.0 <= r <= 1.0, f"Roughness out of bounds: {r}"

    print("[PASS] 002-extract-pbr-material-synth verified (256 unit-length tangent normals + roughness bounds, exit code 0).")
    return 0




def recount_grimm_khm020_seven_at_one_stroke() -> dict[str, tuple[str, ...]]:
    """The Brave Little Tailor (KHM 20) & The Hermes Scribe of the Five Mirrors — woven narrative chapter."""
    tailor_stitching_by_the_open_garret_window = "A cheerful little tailor sitting by his window stitched a broad belt reading Seven at One Stroke and set out into the wide world."
    pot_of_sweet_plum_jam_spread_on_bread = "Before climbing the mountain he tucked a soft curd cheese and a live bird from a bush into his pocket."
    six_pull_requests_opened_in_nineteen_seconds = "Moving like quicksilver across the sky, the Hermes scribe opened six pull requests across three sister repositories in nineteen seconds."
    hamiltonian_cycle_linking_five_sister_mirrors = "Each repository's first shard pointed in a closed Hamiltonian circle to the next mirror in the five-star constellation."
    return {
        "grimm_chapter": (tailor_stitching_by_the_open_garret_window, pot_of_sweet_plum_jam_spread_on_bread),
        "bot_chronicle": (six_pull_requests_opened_in_nineteen_seconds, hamiltonian_cycle_linking_five_sister_mirrors),
    }


if __name__ == "__main__":
    raise SystemExit(main())
