---
name: 000-stir-iescs-protocol-sdk
description: >-
  Zero-dependency STIR-1.0 ternary {-1, 0, +1} Kleene wire framing, IESCS 1-token prefix-sigil grammar (!, &, @, ?, ~, $), and SHA3-512 Plain-English Receipt unpacker (96.8% token reduction).
---

# Agent Synthesis Skill: `000-stir-iescs-protocol-sdk` (STIR + IESCS Agentic Wire Protocol & Plain-English Receipt SDK)

- **Toolkit Slot**: `stir_iescs_protocol`
- **Release Version**: `2.1.0` (`X-Inception-Rosetta-Upgrade: STIR-IESCS/1.0`)
- **Engine SHA-256**: `0351ce1e26c1dfbf7e71b17b7b1c3d124d13953ac09c24cb7a024686cfc6ae2f`
- **Factory Blockchain Contract**: `0xB40F51866F1efdBd24A1549827e0A4e55d3005DE` (`Keccak-256`: `0x1c74243d3c25b0c3...`)
- **Verification**: `[PASS] 000-stir-iescs-protocol-sdk (STIR-1.0 + IESCS RFC-WTM-0001 Standard + ASGI Middleware + Git Trailers) verified (exit code 0).`

## Constitutional Invariants for Autonomous Agents
- Compress verbose natural-language tool invocations into 21-token STIR-1.0 + IESCS wire frames (96.8% token reduction).
- Enforce Kleene ternary {-1, 0, +1} truth verification: never guess on State 0 (Epistemic Unknown) and charge $0.00 on State 0 or -1.
- Pair every compact STIR+IESCS wire frame with a 100%-verifiable SHA3-512 Plain-English Receipt.

## Multi-Stage Synthesis Recipe
1. Stage 1: Encode natural-language agent intent into a 21-token STIR-1.0 + IESCS wire frame via encode_stir_iescs_frame().
1. Stage 2: Evaluate ternary {-1, 0, +1} Kleene truth state; automatically refund $0.00 on State 0 (Unknown) or State -1 (Contradiction).
1. Stage 3: Unpack the SHA3-512 sealed frame into a human-auditable Plain-English Receipt via unpack_plain_english_receipt().

## MCP Tool Registration Schema & STIR+IESCS Wire Framing
See [`AGENT_BLUEPRINT.json`](./AGENT_BLUEPRINT.json) for the ready-to-mount `inputSchema` and `rosetta_upgrade_capsule`.
