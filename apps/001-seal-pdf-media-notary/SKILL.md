---
name: 001-seal-pdf-media-notary
description: >-
  Zero-dependency RFC 6962 Merkle audit tree, SHA-256 media notary, and EXIF orientation/GPS privacy normalizer.
---

# Agent Synthesis Skill: `001-seal-pdf-media-notary` (Cryptographic Media Notary & EXIF Orientation / Privacy Scrubber)

- **Toolkit Slot**: `seal_pdf_notary + utility_exif_scrubber`
- **Release Version**: `2.1.0` (`X-Inception-Rosetta-Upgrade: STIR-IESCS/1.0`)
- **Engine SHA-256**: `2eeeecb92072bbebdc3eb77a394ab4e05518e8d078eb31ff49e2286081622f87`
- **Factory Blockchain Contract**: `0xB40F51866F1efdBd24A1549827e0A4e55d3005DE` (`Keccak-256`: `0xe0bfa93409387bcc...`)
- **Verification**: `[PASS] 001-seal-pdf-media-notary verified (RFC 6962 Merkle root + EXIF transpose + tamper rejection, exit code 0).`

## Constitutional Invariants for Autonomous Agents
- Always transpose raw camera buffers according to EXIF tag 0x0112 before projecting textures or generating thumbnails.
- Never mutate or delete original vault raw files (.ARW, .CR3, .BRAW); emit sidecar .notary.json envelopes.
- Use RFC 6962 domain-separated prefix bytes (0x00 leaf, 0x01 internal node) to prevent second-preimage Merkle collisions.

## Multi-Stage Synthesis Recipe
1. Stage 1 (Ingest): Read binary stream in 4KB blocks and extract EXIF/TIFF IFD0 & SubIFD tags.
1. Stage 2 (Transpose & Scrub): Apply EXIF_ORIENTATION_MATRICES[tag] and strip GPS/Serial keys.
1. Stage 3 (Attest): Compute SHA-256 + RFC 6962 Merkle root and bind to normalized metadata digest.

## MCP Tool Registration Schema & STIR+IESCS Wire Framing
See [`AGENT_BLUEPRINT.json`](./AGENT_BLUEPRINT.json) for the ready-to-mount `inputSchema` and `rosetta_upgrade_capsule`.
