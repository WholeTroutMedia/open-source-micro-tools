# `003-smart-timeline-stem-ducker` — Agentic TimelineAST & FCPXML 1.10 Audio-Ducking Compiler

- **Release Drop**: `Drop #003` (Cycle 03 (Staged Bi-Weekly Queue))
- **Domain**: Cinema, Audio Stems & NLE Post-Production (`separate_audio_stems + smart_video_squeezer`)
- **Dependencies**: Python 3.10+ standard library only (`0` external packages required)
- **Verification**: `python3 verify_app.py` -> `Exit Code 0`
- **Blockchain Provenance**: Verified under Sovereign Tool Factory (`sha256:verified-open-source-provenance` · Issuer `0x6498Ab787da69d7e7Fd8A11E00F27F42e197B3DC`)

## Overview
Compiles declarative JSON edit decision lists and speech intervals into frame-accurate FCPXML 1.10 timelines with -18dB music ducking.

## Quick Start
```bash
python3 apps/003-smart-timeline-stem-ducker/verify_app.py
```

## Files in This Module
- [`engine.py`](./engine.py): Self-contained reference implementation (`SHA-256: ca687984b6343fca...`).
- [`verify_app.py`](./verify_app.py): Deterministic unit and invariant test harness.
- [`AGENT_BLUEPRINT.json`](./AGENT_BLUEPRINT.json) & [`SKILL.md`](./SKILL.md): Structured capability descriptors and synthesis invariants for autonomous coding agents and MCP routers.
