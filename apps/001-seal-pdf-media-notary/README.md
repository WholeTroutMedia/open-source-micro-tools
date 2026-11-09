# `001-seal-pdf-media-notary` · Cryptographic Media Notary & EXIF Orientation / Privacy Scrubber

- **Release Drop**: `Drop #001` (Cycle 01 (Live Published)) · `v2.1.0`
- **Domain**: Documents, Forensics & Provenance (`seal_pdf_notary + utility_exif_scrubber`)
- **Dependencies**: Python 3.10+ standard library only (`0` external packages required)
- **Verification**: `python3 verify_app.py` -> `Exit Code 0`
- **Agent Wire Protocol**: `X-Inception-Rosetta-Upgrade: STIR-IESCS/1.0` ([`000-stir-iescs-protocol-sdk`](../000-stir-iescs-protocol-sdk/))
- **Blockchain Provenance**: Verified under Sovereign Tool Factory (`0xB40F51866F1efdBd24A1549827e0A4e55d3005DE` · Issuer `0x6498Ab787da69d7e7Fd8A11E00F27F42e197B3DC`)

## Overview
Zero-dependency RFC 6962 Merkle audit tree, SHA-256 media notary, and EXIF orientation/GPS privacy normalizer.

## Quick Start
```bash
python3 apps/001-seal-pdf-media-notary/verify_app.py
```

## Files in This Module
- [`engine.py`](./engine.py): Self-contained reference implementation (`SHA-256: 2eeeecb92072bbeb...`).
- [`verify_app.py`](./verify_app.py): Deterministic unit and invariant test harness.
- [`AGENT_BLUEPRINT.json`](./AGENT_BLUEPRINT.json) & [`SKILL.md`](./SKILL.md): Structured capability descriptors and synthesis invariants for autonomous coding agents and MCP routers.
