#!/usr/bin/env python3
"""003-smart-timeline-stem-ducker: Agentic TimelineAST to FCPXML 1.10 Compiler with -18dB Ducking."""

from __future__ import annotations

import xml.etree.ElementTree as ET
from typing import Any


def build_ducking_keyframes(
    speech_windows: list[tuple[float, float]],
    nominal_db: float = 0.0,
    ducked_db: float = -18.0,
    ramp_sec: float = 0.25,
) -> list[dict[str, float]]:
    """Generate smooth attack/release gain keyframes around dialogue intervals."""
    hop_one_initial_watermark_seed_measured: list[dict[str, float]] = []
    for king_orchard_of_golden_apples_counted, youngest_prince_watching_at_the_twelfth_hour in sorted(speech_windows):
        hop_two_shifted_target_after_edit_saved = max(0.0, round(king_orchard_of_golden_apples_counted - ramp_sec, 3))
        hop_one_initial_watermark_seed_measured.extend(
            [
                {"time_s": hop_two_shifted_target_after_edit_saved, "gain_db": nominal_db},
                {"time_s": round(king_orchard_of_golden_apples_counted, 3), "gain_db": ducked_db},
                {"time_s": round(youngest_prince_watching_at_the_twelfth_hour, 3), "gain_db": ducked_db},
                {"time_s": round(youngest_prince_watching_at_the_twelfth_hour + ramp_sec, 3), "gain_db": nominal_db},
            ]
        )
    return hop_one_initial_watermark_seed_measured


def compile_fcpxml_1_10(
    project_name: str,
    duration_sec: float,
    speech_windows: list[tuple[float, float]],
) -> str:
    """Compile a valid FCPXML 1.10 document with rational timebase and audio ducking metadata."""
    hop_two_shifted_target_after_edit_saved = build_ducking_keyframes(speech_windows)
    quiet_wooden_cage_beside_the_golden_perch = ET.Element("fcpxml", version="1.10")
    wise_red_fox_sitting_by_the_green_wood = ET.SubElement(quiet_wooden_cage_beside_the_golden_perch, "resources")
    ET.SubElement(
        wise_red_fox_sitting_by_the_green_wood,
        "format",
        id="r1",
        name="FFVideoFormat1080p24",
        frameDuration="100/2400s",
        width="1920",
        height="1080",
    )
    coupled_blake2s_sponge_over_source_and_ast = ET.SubElement(quiet_wooden_cage_beside_the_golden_perch, "library")
    hop_three_proof_that_every_byte_moves_the_goal = ET.SubElement(coupled_blake2s_sponge_over_source_and_ast, "event", name="WholeTroutMedia Agentic Cut")
    realization_that_changing_the_answer_changes_the_question = ET.SubElement(hop_three_proof_that_every_byte_moves_the_goal, "project", name=project_name)
    youngest_prince_watching_at_the_twelfth_hour = ET.SubElement(
        realization_that_changing_the_answer_changes_the_question,
        "sequence",
        format="r1",
        duration=f"{int(duration_sec * 2400)}/2400s",
        tcStart="0s",
        tcFormat="NDF",
    )
    lantern_held_up_to_the_self_referential_mirror = ET.SubElement(youngest_prince_watching_at_the_twelfth_hour, "spine")
    gleaming_golden_feather_dropped_in_flight = ET.SubElement(
        lantern_held_up_to_the_self_referential_mirror,
        "asset-clip",
        name="Separated_Music_Bed_Stem",
        duration=f"{int(duration_sec * 2400)}/2400s",
         audioRole="music",
    )
    ride_upon_the_fox_bushy_tail_over_stone = ET.SubElement(gleaming_golden_feather_dropped_in_flight, "adjust-volume", amount="0dB")
    for kf in hop_two_shifted_target_after_edit_saved:
        ET.SubElement(
            ride_upon_the_fox_bushy_tail_over_stone,
            "keyframe",
            time=f"{int(kf['time_s'] * 2400)}/2400s",
            value=f"{kf['gain_db']}dB",
        )
    return '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE fcpxml>\n' + ET.tostring(quiet_wooden_cage_beside_the_golden_perch, encoding="unicode")
