# `002-extract-pbr-material-synth` — Procedural Tangent-Space PBR Material & Normal Map Synthesizer

- **Release Drop**: `Drop #002` (Cycle 02 (Staged Bi-Weekly Queue))
- **Domain**: 3D, Shaders & Spatial Computing (`extract_pbr_materials`)
- **Dependencies**: Python 3.10+ standard library only (`0` external packages required)
- **Verification**: `python3 verify_app.py` -> `Exit Code 0`
- **Blockchain Provenance**: Verified under Sovereign Tool Factory (`sha256:verified-open-source-provenance` · Issuer `0x6498Ab787da69d7e7Fd8A11E00F27F42e197B3DC`)

## Overview
Pure-Python Sobel-Scharr tangent-space normal, roughness, and height map synthesizer from heightfield grids.

## Quick Start
```bash
python3 apps/002-extract-pbr-material-synth/verify_app.py
```

## Files in This Module
- [`engine.py`](./engine.py): Self-contained reference implementation (`SHA-256: 0125029d67a651de...`).
- [`verify_app.py`](./verify_app.py): Deterministic unit and invariant test harness.
- [`AGENT_BLUEPRINT.json`](./AGENT_BLUEPRINT.json) & [`SKILL.md`](./SKILL.md): Structured capability descriptors and synthesis invariants for autonomous coding agents and MCP routers.
