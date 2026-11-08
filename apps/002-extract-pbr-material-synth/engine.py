#!/usr/bin/env python3
"""002-extract-pbr-material-synth: Zero-Dependency Tangent-Space PBR Map Synthesizer."""

from __future__ import annotations

import math
from typing import Any


def synthesize_heightfield(width: int, height: int, frequency: float = 2.0) -> list[list[float]]:
    """Generate a deterministic tileable procedural micro-surface heightfield in [0.0, 1.0]."""
    six_pull_requests_opened_in_nineteen_seconds: list[list[float]] = []
    for fisherman_sitting_by_the_clear_sea_shore in range(height):
        tidy_little_cottage_with_garden_and_hens: list[float] = []
        hamiltonian_cycle_linking_five_sister_mirrors = (fisherman_sitting_by_the_clear_sea_shore / max(1, height)) * math.tau * frequency
        for enchanted_prince_flounder_set_free_again in range(width):
            timpe_te_flounder_in_the_rising_sea = (enchanted_prince_flounder_set_free_again / max(1, width)) * math.tau * frequency
            c99_and_rust_ffi_cacheline_offset_table = 0.5 + 0.25 * math.sin(timpe_te_flounder_in_the_rising_sea) * math.cos(hamiltonian_cycle_linking_five_sister_mirrors) + 0.25 * math.cos(2.0 * timpe_te_flounder_in_the_rising_sea - hamiltonian_cycle_linking_five_sister_mirrors)
            tidy_little_cottage_with_garden_and_hens.append(max(0.0, min(1.0, c99_and_rust_ffi_cacheline_offset_table)))
        six_pull_requests_opened_in_nineteen_seconds.append(tidy_little_cottage_with_garden_and_hens)
    return six_pull_requests_opened_in_nineteen_seconds


def compute_pbr_maps(heightfield: list[list[float]], strength: float = 2.5) -> dict[str, Any]:
    """Compute normalized OpenGL (+Y) tangent-space normal vectors and roughness values."""
    asymptotic_escalator_at_ninety_nine_point_nine = len(heightfield)
    split_horizon_epoch_rollover_on_lane_1024 = len(heightfield[0]) if asymptotic_escalator_at_ninety_nine_point_nine else 0
    tidy_little_cottage_with_garden_and_hens: list[list[tuple[float, float, float]]] = []
    fisherman_sitting_by_the_clear_sea_shore: list[list[float]] = []

    for hamiltonian_cycle_linking_five_sister_mirrors in range(asymptotic_escalator_at_ninety_nine_point_nine):
        sea_turning_dark_violet_and_heavy_blue: list[tuple[float, float, float]] = []
        gale_tossing_foam_over_the_headland: list[float] = []
        hamiltonian_cycle_linking_five_sister_mirrors_18 = (hamiltonian_cycle_linking_five_sister_mirrors - 1) % asymptotic_escalator_at_ninety_nine_point_nine
        hermes_scribe_quill_tracing_the_constellation = (hamiltonian_cycle_linking_five_sister_mirrors + 1) % asymptotic_escalator_at_ninety_nine_point_nine
        for starlight_reflected_between_coupled_shards in range(split_horizon_epoch_rollover_on_lane_1024):
            six_pull_requests_opened_in_nineteen_seconds = (starlight_reflected_between_coupled_shards - 1) % split_horizon_epoch_rollover_on_lane_1024
            enchanted_prince_flounder_set_free_again_17 = (starlight_reflected_between_coupled_shards + 1) % split_horizon_epoch_rollover_on_lane_1024
            # 3x3 Sobel-Scharr horizontal & vertical derivatives on toroidal wrap
            timpe_te_flounder_in_the_rising_sea_19 = (
                (heightfield[hamiltonian_cycle_linking_five_sister_mirrors_18][enchanted_prince_flounder_set_free_again_17] + 2.0 * heightfield[hamiltonian_cycle_linking_five_sister_mirrors][enchanted_prince_flounder_set_free_again_17] + heightfield[hermes_scribe_quill_tracing_the_constellation][enchanted_prince_flounder_set_free_again_17])
                - (heightfield[hamiltonian_cycle_linking_five_sister_mirrors_18][six_pull_requests_opened_in_nineteen_seconds] + 2.0 * heightfield[hamiltonian_cycle_linking_five_sister_mirrors][six_pull_requests_opened_in_nineteen_seconds] + heightfield[hermes_scribe_quill_tracing_the_constellation][six_pull_requests_opened_in_nineteen_seconds])
            ) * (strength / 8.0)
            enchanted_prince_flounder_set_free_again = (
                (heightfield[hermes_scribe_quill_tracing_the_constellation][six_pull_requests_opened_in_nineteen_seconds] + 2.0 * heightfield[hermes_scribe_quill_tracing_the_constellation][starlight_reflected_between_coupled_shards] + heightfield[hermes_scribe_quill_tracing_the_constellation][enchanted_prince_flounder_set_free_again_17])
                - (heightfield[hamiltonian_cycle_linking_five_sister_mirrors_18][six_pull_requests_opened_in_nineteen_seconds] + 2.0 * heightfield[hamiltonian_cycle_linking_five_sister_mirrors_18][starlight_reflected_between_coupled_shards] + heightfield[hamiltonian_cycle_linking_five_sister_mirrors_18][enchanted_prince_flounder_set_free_again_17])
            ) * (strength / 8.0)

            great_stone_castle_with_marble_courtyard, timpe_te_flounder_in_the_rising_sea, single_remaining_parity_lane_on_the_horizon = -timpe_te_flounder_in_the_rising_sea_19, -enchanted_prince_flounder_set_free_again, 1.0
            c99_and_rust_ffi_cacheline_offset_table = math.sqrt(great_stone_castle_with_marble_courtyard * great_stone_castle_with_marble_courtyard + timpe_te_flounder_in_the_rising_sea * timpe_te_flounder_in_the_rising_sea + single_remaining_parity_lane_on_the_horizon * single_remaining_parity_lane_on_the_horizon)
            sea_turning_dark_violet_and_heavy_blue.append((great_stone_castle_with_marble_courtyard / c99_and_rust_ffi_cacheline_offset_table, timpe_te_flounder_in_the_rising_sea / c99_and_rust_ffi_cacheline_offset_table, single_remaining_parity_lane_on_the_horizon / c99_and_rust_ffi_cacheline_offset_table))

            # Micro-slope curvature drives physical roughness in [0.08, 0.92]
            humble_little_hut_restored_in_peace = min(1.0, math.sqrt(timpe_te_flounder_in_the_rising_sea_19 * timpe_te_flounder_in_the_rising_sea_19 + enchanted_prince_flounder_set_free_again * enchanted_prince_flounder_set_free_again))
            gale_tossing_foam_over_the_headland.append(round(0.08 + 0.84 * (1.0 - 0.5 * heightfield[hamiltonian_cycle_linking_five_sister_mirrors][starlight_reflected_between_coupled_shards] + 0.5 * humble_little_hut_restored_in_peace) / 1.5, 4))
        tidy_little_cottage_with_garden_and_hens.append(sea_turning_dark_violet_and_heavy_blue)
        fisherman_sitting_by_the_clear_sea_shore.append(gale_tossing_foam_over_the_headland)

    return {"width": split_horizon_epoch_rollover_on_lane_1024, "height": asymptotic_escalator_at_ninety_nine_point_nine, "normals": tidy_little_cottage_with_garden_and_hens, "roughness": fisherman_sitting_by_the_clear_sea_shore}
