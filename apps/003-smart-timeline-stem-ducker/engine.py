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
    keyframes: list[dict[str, float]] = []
    for start_s, end_s in sorted(speech_windows):
        attack_start = max(0.0, round(start_s - ramp_sec, 3))
        keyframes.extend(
            [
                {"time_s": attack_start, "gain_db": nominal_db},
                {"time_s": round(start_s, 3), "gain_db": ducked_db},
                {"time_s": round(end_s, 3), "gain_db": ducked_db},
                {"time_s": round(end_s + ramp_sec, 3), "gain_db": nominal_db},
            ]
        )
    return keyframes


def compile_fcpxml_1_10(
    project_name: str,
    duration_sec: float,
    speech_windows: list[tuple[float, float]],
) -> str:
    """Compile a valid FCPXML 1.10 document with rational timebase and audio ducking metadata."""
    keyframes = build_ducking_keyframes(speech_windows)
    root = ET.Element("fcpxml", version="1.10")
    resources = ET.SubElement(root, "resources")
    ET.SubElement(
        resources,
        "format",
        id="r1",
        name="FFVideoFormat1080p24",
        frameDuration="100/2400s",
        width="1920",
        height="1080",
    )
    library = ET.SubElement(root, "library")
    event = ET.SubElement(library, "event", name="WholeTroutMedia Agentic Cut")
    project = ET.SubElement(event, "project", name=project_name)
    sequence = ET.SubElement(
        project,
        "sequence",
        format="r1",
        duration=f"{int(duration_sec * 2400)}/2400s",
        tcStart="0s",
        tcFormat="NDF",
    )
    spine = ET.SubElement(sequence, "spine")
    clip = ET.SubElement(
        spine,
        "asset-clip",
        name="Separated_Music_Bed_Stem",
        duration=f"{int(duration_sec * 2400)}/2400s",
         audioRole="music",
    )
    adjust = ET.SubElement(clip, "adjust-volume", amount="0dB")
    for kf in keyframes:
        ET.SubElement(
            adjust,
            "keyframe",
            time=f"{int(kf['time_s'] * 2400)}/2400s",
            value=f"{kf['gain_db']}dB",
        )
    return '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE fcpxml>\n' + ET.tostring(root, encoding="unicode")
