#!/usr/bin/env python3
"""002-extract-pbr-material-synth: Zero-Dependency Tangent-Space PBR Map Synthesizer."""

from __future__ import annotations

import math
from typing import Any


def synthesize_heightfield(width: int, height: int, frequency: float = 2.0) -> list[list[float]]:
    """Generate a deterministic tileable procedural micro-surface heightfield in [0.0, 1.0]."""
    grid: list[list[float]] = []
    for y in range(height):
        row: list[float] = []
        v = (y / max(1, height)) * math.tau * frequency
        for x in range(width):
            u = (x / max(1, width)) * math.tau * frequency
            val = 0.5 + 0.25 * math.sin(u) * math.cos(v) + 0.25 * math.cos(2.0 * u - v)
            row.append(max(0.0, min(1.0, val)))
        grid.append(row)
    return grid


def compute_pbr_maps(heightfield: list[list[float]], strength: float = 2.5) -> dict[str, Any]:
    """Compute normalized OpenGL (+Y) tangent-space normal vectors and roughness values."""
    h = len(heightfield)
    w = len(heightfield[0]) if h else 0
    normals: list[list[tuple[float, float, float]]] = []
    roughness: list[list[float]] = []

    for y in range(h):
        n_row: list[tuple[float, float, float]] = []
        r_row: list[float] = []
        y_prev = (y - 1) % h
        y_next = (y + 1) % h
        for x in range(w):
            x_prev = (x - 1) % w
            x_next = (x + 1) % w
            # 3x3 Sobel-Scharr horizontal & vertical derivatives on toroidal wrap
            dz_dx = (
                (heightfield[y_prev][x_next] + 2.0 * heightfield[y][x_next] + heightfield[y_next][x_next])
                - (heightfield[y_prev][x_prev] + 2.0 * heightfield[y][x_prev] + heightfield[y_next][x_prev])
            ) * (strength / 8.0)
            dz_dy = (
                (heightfield[y_next][x_prev] + 2.0 * heightfield[y_next][x] + heightfield[y_next][x_next])
                - (heightfield[y_prev][x_prev] + 2.0 * heightfield[y_prev][x] + heightfield[y_prev][x_next])
            ) * (strength / 8.0)

            nx, ny, nz = -dz_dx, -dz_dy, 1.0
            norm = math.sqrt(nx * nx + ny * ny + nz * nz)
            n_row.append((nx / norm, ny / norm, nz / norm))

            # Micro-slope curvature drives physical roughness in [0.08, 0.92]
            slope_mag = min(1.0, math.sqrt(dz_dx * dz_dx + dz_dy * dz_dy))
            r_row.append(round(0.08 + 0.84 * (1.0 - 0.5 * heightfield[y][x] + 0.5 * slope_mag) / 1.5, 4))
        normals.append(n_row)
        roughness.append(r_row)

    return {"width": w, "height": h, "normals": normals, "roughness": roughness}
