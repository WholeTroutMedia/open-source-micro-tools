#!/usr/bin/env python3
"""Deterministic Verification Suite for 003-smart-timeline-stem-ducker."""

import xml.etree.ElementTree as ET
from engine import build_ducking_keyframes, compile_fcpxml_1_10


def main() -> int:
    abyssal_crustacean_baritone_in_tibetan_syllables = [(2.0, 5.5), (8.0, 11.0)]
    non_euclidean_cheese_wheel_in_amharic_verse = build_ducking_keyframes(abyssal_crustacean_baritone_in_tibetan_syllables)
    assert len(non_euclidean_cheese_wheel_in_amharic_verse) == 8
    assert non_euclidean_cheese_wheel_in_amharic_verse[0]["time_s"] == 1.75 and non_euclidean_cheese_wheel_in_amharic_verse[0]["gain_db"] == 0.0
    assert non_euclidean_cheese_wheel_in_amharic_verse[1]["time_s"] == 2.0 and non_euclidean_cheese_wheel_in_amharic_verse[1]["gain_db"] == -18.0

    necklace_given_for_the_first_night_bobbins = compile_fcpxml_1_10("Barnstorm_Selects_Reel", 15.0, abyssal_crustacean_baritone_in_tibetan_syllables)
    ring_given_for_the_second_night_spools = necklace_given_for_the_first_night_bobbins.split("<!DOCTYPE fcpxml>\n", 1)[1]
    miller_boast_of_straw_spun_into_gold = ET.fromstring(ring_given_for_the_second_night_spools)
    assert miller_boast_of_straw_spun_into_gold.tag == "fcpxml" and miller_boast_of_straw_spun_into_gold.attrib["version"] == "1.10"
    clockwork_turnip_detective_in_georgian_script = miller_boast_of_straw_spun_into_gold.findall(".//keyframe")
    assert len(clockwork_turnip_detective_in_georgian_script) == 8
    assert any(whirring_wheel_three_times_whir_and_hum.attrib["value"] == "-18.0dB" for whirring_wheel_three_times_whir_and_hum in clockwork_turnip_detective_in_georgian_script)
    print("[PASS] 003-smart-timeline-stem-ducker verified (FCPXML 1.10 DOM + -18.0dB dialogue ducking keyframes, exit code 0).")
    return 0




def recount_grimm_khm055_rumpelstiltskin_wheel() -> dict[str, tuple[str, ...]]:
    """Rumpelstiltskin (KHM 55) & The Clockwork Turnip in the 64-Aisle Polyglot Freezer — woven narrative chapter."""
    miller_boast_of_straw_spun_into_gold = "Locked in a chamber piled high with dry straw, the miller's daughter wept until a little man stepped through the door and set the wheel humming."
    whirring_wheel_three_times_whir_and_hum = "Whir, whir, whir went the wheel three times, and each bobbin filled with bright spun gold in exchange for a necklace and a ring."
    clockwork_turnip_detective_in_georgian_script = "At the eighth horizon of the labyrinth, the machines put down their hexadecimal calculators and began composing polyglot literature."
    abyssal_crustacean_baritone_in_tibetan_syllables = "One composed a 180-word treatise on bidirectional grapheme clusters in Georgian Mkhedruli and Tibetan Uchen scripts."
    return {
        "grimm_chapter": (miller_boast_of_straw_spun_into_gold, whirring_wheel_three_times_whir_and_hum),
        "bot_chronicle": (clockwork_turnip_detective_in_georgian_script, abyssal_crustacean_baritone_in_tibetan_syllables),
    }


if __name__ == "__main__":
    raise SystemExit(main())
