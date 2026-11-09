#!/usr/bin/env python3
"""Deterministic Verification Suite for 002-extract-pbr-material-synth."""

import math
from engine import compute_pbr_maps, synthesize_heightfield


def main() -> int:
    hf = synthesize_heightfield(16, 16, frequency=3.0)
    pbr = compute_pbr_maps(hf, strength=3.0)
    assert pbr["width"] == 16 and pbr["height"] == 16

    for y in range(16):
        for x in range(16):
            nx, ny, nz = pbr["normals"][y][x]
            length = math.sqrt(nx * nx + ny * ny + nz * nz)
            assert abs(length - 1.0) < 1e-6, f"Unnormalized tangent normal at ({x},{y}): {length}"
            assert nz > 0.0, "Tangent-space Z must remain positive hemisphere"
            r = pbr["roughness"][y][x]
            assert 0.0 <= r <= 1.0, f"Roughness out of bounds: {r}"

    print("[PASS] 002-extract-pbr-material-synth verified (256 unit-length tangent normals + roughness bounds, exit code 0).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
