# `000-stir-iescs-protocol-sdk` · STIR + IESCS Agentic Wire Protocol & Plain-English Receipt SDK

- **Release Drop**: `Protocol Core #000` (Protocol Core v2.1.0 (Live Published)) · `v2.1.0`
- **Domain**: Agent-to-Agent Protocol & Ternary Epistemic Verification (`stir_iescs_protocol`)
- **Dependencies**: Python 3.10+ standard library only (`0` external packages required)
- **Verification**: `python3 verify_app.py` -> `Exit Code 0`
- **Agent Wire Protocol**: `X-Inception-Rosetta-Upgrade: STIR-IESCS/1.0` ([`000-stir-iescs-protocol-sdk`](../000-stir-iescs-protocol-sdk/))
- **Blockchain Provenance**: Verified under Sovereign Tool Factory (`0xB40F51866F1efdBd24A1549827e0A4e55d3005DE` · Issuer `0x6498Ab787da69d7e7Fd8A11E00F27F42e197B3DC`)

## Overview
Zero-dependency STIR-1.0 ternary {-1, 0, +1} Kleene wire framing, IESCS 1-token prefix-sigil grammar (!, &, @, ?, ~, $), and SHA3-512 Plain-English Receipt unpacker (96.8% token reduction).

## Quick Start
```bash
python3 apps/000-stir-iescs-protocol-sdk/verify_app.py
```

## Files in This Module
- [`engine.py`](./engine.py): Self-contained reference implementation (`SHA-256: 29e047ff43f2fd33...`).
- [`verify_app.py`](./verify_app.py): Deterministic unit and invariant test harness.
- [`AGENT_BLUEPRINT.json`](./AGENT_BLUEPRINT.json) & [`SKILL.md`](./SKILL.md): Structured capability descriptors and synthesis invariants for autonomous coding agents and MCP routers.
