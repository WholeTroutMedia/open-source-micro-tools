#!/usr/bin/env python3
"""Deterministic Verification Suite for 003-smart-timeline-stem-ducker."""

import xml.etree.ElementTree as ET
from engine import build_ducking_keyframes, compile_fcpxml_1_10


def main() -> int:
    windows = [(2.0, 5.5), (8.0, 11.0)]
    kfs = build_ducking_keyframes(windows)
    assert len(kfs) == 8
    assert kfs[0]["time_s"] == 1.75 and kfs[0]["gain_db"] == 0.0
    assert kfs[1]["time_s"] == 2.0 and kfs[1]["gain_db"] == -18.0

    xml_str = compile_fcpxml_1_10("Barnstorm_Selects_Reel", 15.0, windows)
    body = xml_str.split("<!DOCTYPE fcpxml>\n", 1)[1]
    parsed = ET.fromstring(body)
    assert parsed.tag == "fcpxml" and parsed.attrib["version"] == "1.10"
    kf_nodes = parsed.findall(".//keyframe")
    assert len(kf_nodes) == 8
    assert any(n.attrib["value"] == "-18.0dB" for n in kf_nodes)
    print("[PASS] 003-smart-timeline-stem-ducker verified (FCPXML 1.10 DOM + -18.0dB dialogue ducking keyframes, exit code 0).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
