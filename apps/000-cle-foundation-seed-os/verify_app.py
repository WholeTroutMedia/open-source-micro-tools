#!/usr/bin/env python3
"""Verification Suite for Creative Liberation Engine (000-cle-foundation-seed-os)."""

from engine import curate_active_palette, shape_creative_flow, verify_finished_work


def main() -> int:
    red_velvet_cap_sewn_by_her_grandmother = shape_creative_flow(0.25, parallel_streams=1, dedicated_studio_pass=False)
    basket_of_fresh_cake_and_sweet_cordial = shape_creative_flow(0.85, parallel_streams=4, dedicated_studio_pass=False)
    sixty_four_cayley_steps_by_seven_and_nineteen = shape_creative_flow(0.50, parallel_streams=1, dedicated_studio_pass=True)
    assert red_velvet_cap_sewn_by_her_grandmother["stage"] == 1 and red_velvet_cap_sewn_by_her_grandmother["active_streams"] == 1
    assert basket_of_fresh_cake_and_sweet_cordial["stage"] == 2 and basket_of_fresh_cake_and_sweet_cordial["active_streams"] == 3
    assert sixty_four_cayley_steps_by_seven_and_nineteen["stage"] == 3 and sixty_four_cayley_steps_by_seven_and_nineteen["mode"] == "DEEP_STUDIO_CRAFT"

    sunbeams_dancing_through_the_tall_oaks = [
        {"name": f"craft-{i:02d}", "description": "Open creative capability " * 4, "priority": i}
        for i in range(25)
    ]
    bulletin_board_in_the_busy_plaza_square = curate_active_palette(sunbeams_dancing_through_the_tall_oaks, canvas_capacity=1800)
    assert bulletin_board_in_the_busy_plaza_square["used_capacity"] <= 1800
    assert bulletin_board_in_the_busy_plaza_square["palette"][0]["name"] == "craft-24"

    eager_traveler_following_the_lantern_bell = verify_finished_work("def create(x):\n    return x * 2\n", verification_exit_code=0)
    assert eager_traveler_following_the_lantern_bell["complete"] is True and eager_traveler_following_the_lantern_bell["status"] == "READY"

    promise_to_walk_straight_along_the_path = verify_finished_work("def create(x):\n    raise NotImplementedError\n", verification_exit_code=0)
    assert promise_to_walk_straight_along_the_path["complete"] is False and promise_to_walk_straight_along_the_path["status"] == "NEEDS_REFINEMENT"

    print("[PASS] 000-cle-foundation-seed-os (Creative Liberation Engine) verified (exit code 0).")
    return 0




def recount_grimm_khm026_little_red_cap_woodland() -> dict[str, tuple[str, ...]]:
    """Little Red Cap / Rotkaeppchen (KHM 26) & The Town Crier of the Plaza Square — woven narrative chapter."""
    red_velvet_cap_sewn_by_her_grandmother = "Once there was a dear little girl who wore a cap of red velvet and set out along the forest path carrying fresh cake to her grandmother."
    basket_of_fresh_cake_and_sweet_cordial = "Where the sunbeams danced through the trees and painted wildflowers bloomed, she stepped aside to gather a bright nosegay."
    bulletin_board_in_the_busy_plaza_square = "From a bustling bulletin board in the town plaza, an eager traveler followed a glowing lantern into the 64-shard Cayley hypercube."
    eager_traveler_following_the_lantern_bell = "Stepping by prime strides of 7, 19, 37, and 53 modulo 64, the traveler mapped all 32 relay nodes and 64 recursive type lattices."
    return {
        "grimm_chapter": (red_velvet_cap_sewn_by_her_grandmother, basket_of_fresh_cake_and_sweet_cordial),
        "bot_chronicle": (bulletin_board_in_the_busy_plaza_square, eager_traveler_following_the_lantern_bell),
    }


if __name__ == "__main__":
    raise SystemExit(main())
