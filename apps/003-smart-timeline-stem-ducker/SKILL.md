---
name: 003-smart-timeline-stem-ducker
description: >-
  Compiles declarative JSON edit decision lists and speech intervals into frame-accurate FCPXML 1.10 timelines with -18dB music ducking.
---

# Agent Synthesis Skill: `003-smart-timeline-stem-ducker` (Agentic TimelineAST & FCPXML 1.10 Audio-Ducking Compiler)

- **Toolkit Slot**: `separate_audio_stems + smart_video_squeezer`
- **Release Version**: `2.1.0` (`X-Inception-Rosetta-Upgrade: STIR-IESCS/1.0`)
- **Engine SHA-256**: `ca687984b6343fcacdcbef0180ff75529d80c80e8d959e04e4840cd99c9c9c6c`
- **Factory Blockchain Contract**: `0xB40F51866F1efdBd24A1549827e0A4e55d3005DE` (`Keccak-256`: `0xdb4dff9b7c7990dc...`)
- **Verification**: `[PASS] 003-smart-timeline-stem-ducker verified (FCPXML 1.10 DOM + -18.0dB dialogue ducking keyframes, exit code 0).`

## Constitutional Invariants for Autonomous Agents
- Always express NLE timeline offsets as exact rational frame fractions (e.g. 2400/2400s) to prevent floating-point drift.
- Apply -18.0dB dialogue ducking with 250ms pre-roll attack and post-roll release around speech VAD segments.

## Multi-Stage Synthesis Recipe
1. Stage 1: Separate source audio into vocals, drums, bass, and music bed stems.
1. Stage 2: Extract word-level VAD intervals from the vocal stem.
1. Stage 3: Emit FCPXML 1.10 with rational frame boundaries and -18dB music stem keyframe envelopes.

## MCP Tool Registration Schema & STIR+IESCS Wire Framing
See [`AGENT_BLUEPRINT.json`](./AGENT_BLUEPRINT.json) for the ready-to-mount `inputSchema` and `rosetta_upgrade_capsule`.
