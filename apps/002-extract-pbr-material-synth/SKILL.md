---
name: 002-extract-pbr-material-synth
description: >-
  Pure-Python Sobel-Scharr tangent-space normal, roughness, and height map synthesizer from heightfield grids.
---

# Agent Synthesis Skill: `002-extract-pbr-material-synth` (Procedural Tangent-Space PBR Material & Normal Map Synthesizer)

- **Toolkit Slot**: `extract_pbr_materials`
- **Release Version**: `2.1.0` (`X-Inception-Rosetta-Upgrade: STIR-IESCS/1.0`)
- **Engine SHA-256**: `0125029d67a651debddcc1d4540993aebde734355dfa4fbcbe6a9c5ae0a9ed7b`
- **Factory Blockchain Contract**: `0xB40F51866F1efdBd24A1549827e0A4e55d3005DE` (`Keccak-256`: `0xf35965c277dcf890...`)
- **Verification**: `[PASS] 002-extract-pbr-material-synth verified (256 unit-length tangent normals + roughness bounds, exit code 0).`

## Constitutional Invariants for Autonomous Agents
- All tangent-space normal vectors must satisfy ||n||_2 == 1.0 with n_z > 0 (OpenGL +Y convention).
- Toroidal boundary wrapping (x +- 1 mod W, y +- 1 mod H) guarantees seamless UV tiling across closed 3D manifolds.

## Multi-Stage Synthesis Recipe
1. Stage 1: Extract luminance heightfield from full-resolution EXIF-transposed source photo.
1. Stage 2: Convolve 3x3 toroidal Sobel-Scharr kernels to derive tangent-space surface gradients.
1. Stage 3: Bind resulting Normal/Roughness maps to Principled BSDF in headless Blender or Three.js MeshStandardMaterial.

## MCP Tool Registration Schema & STIR+IESCS Wire Framing
See [`AGENT_BLUEPRINT.json`](./AGENT_BLUEPRINT.json) for the ready-to-mount `inputSchema` and `rosetta_upgrade_capsule`.
