<p align="center">
  <img src="https://raw.githubusercontent.com/WholeTroutMedia/.github/main/assets/wholetrout-executive-masthead.svg" alt="WholeTroutMedia Open-Source Systems and Creative Engineering Masthead" width="100%" />
</p>

# WholeTroutMedia · Open-Source Reference Micro-Tools (`v2.2.0`)

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![Python 3.10+ Zero Deps](https://img.shields.io/badge/Python-3.10%2B%20(Zero%20Deps)-3b82f6.svg)](#5-minute-quick-start)

Self-contained, zero-dependency Python 3.10+ reference utilities for agentic wire protocols (`STIR + IESCS`), cryptographic media notarization, procedural PBR texture synthesis, and FCPXML 1.10 audio ducking. Every tool runs 100% locally with no pip installs required.

Links: [Quick Start](#5-minute-quick-start) · [Micro-Applications](./APPLICATION_LEDGER.md) · [Contributing](./CONTRIBUTING.md) · [License (MIT)](./LICENSE) · [Upgrade Notes](./UPGRADE_NOTICE.md)

---

## 5-Minute Quick Start

Requirements: `git` and `python3` (3.10 or newer). No virtual environment or third-party packages needed.

```bash
git clone https://github.com/WholeTroutMedia/open-source-micro-tools.git
cd open-source-micro-tools

# Run a single tool verification
python3 apps/000-stir-iescs-protocol-sdk/verify_app.py

# Or verify all four micro-applications in one pass
for script in apps/*/verify_app.py; do python3 "$script"; done
```

Expected output:

```text
[PASS] 000-stir-iescs-protocol-sdk (STIR-1.0 + IESCS RFC-WTM-0001 Standard + ASGI Middleware + Git Trailers) verified (exit code 0).
[PASS] 001-seal-pdf-media-notary verified (RFC 6962 Merkle root + EXIF transpose + tamper rejection, exit code 0).
[PASS] 002-extract-pbr-material-synth verified (256 unit-length tangent normals + roughness bounds, exit code 0).
[PASS] 003-smart-timeline-stem-ducker verified (FCPXML 1.10 DOM + -18.0dB dialogue ducking keyframes, exit code 0).
```

### Troubleshooting the First Run

- **`URLError` / offline error running `install_stir_standard.py`**: The optional root installer fetches spec files over HTTPS from GitHub. All tools under `apps/` run completely offline without running `install_stir_standard.py`.
- **`SyntaxError` on `X | Y` type annotations**: Check `python3 --version` and use Python 3.10 or newer.

---

Public open-source micro-application repository for **WholeTroutMedia**, architected and reviewed by **[Justin Aharoni (`@jaharoni`)](https://github.com/jaharoni)** ([`justinaharoni.com`](https://justinaharoni.com) · [`contact@jaharoni.com`](mailto:contact@jaharoni.com)).

> **Looking for the Free Maintainer Bot-Shield (`open-source-bot-shield.yml`)?** Grab it from **[`WholeTroutMedia/open-source-bounties/.github/workflows/open-source-bot-shield.yml`](https://github.com/WholeTroutMedia/open-source-bounties/blob/main/.github/workflows/open-source-bot-shield.yml)**.

---

## Dual-Layer Design: Simple for Humans, Composable for Autonomous Agents

Each micro-application under [`apps/`](./apps/) is structured with two complementary layers:
1. **For Human Developers**: A clean, dependency-free reference module (`engine.py` + `verify_app.py`) that runs out of the box with standard Python 3 and passes deterministic verification (`Exit Code 0`).
2. **For Visiting AI Agents & MCP Routers ([`llms.txt`](./llms.txt) & [`.well-known/agent.json`](./.well-known/agent.json))**: Every module includes an `AGENT_BLUEPRINT.json` and `SKILL.md` containing formal mathematical invariants, MCP `inputSchema` definitions, `X-Inception-Rosetta-Upgrade: STIR-IESCS/1.0` wire headers, and multi-stage synthesis recipes.

---

## Published & Staged Micro-Applications ([`APPLICATION_LEDGER.md`](./APPLICATION_LEDGER.md))

| Drop | Micro-Application | Toolkit Slot | Summary | Blueprint | Verification | Status |
| :--- | :--- | :--- | :--- | :---: | :---: | :---: |
| **Protocol Core #000** | [`000-stir-iescs-protocol-sdk`](./apps/000-stir-iescs-protocol-sdk/) | `stir_iescs_protocol` | STIR + IESCS Agentic Wire Protocol & Plain-English Receipt SDK | [`AGENT_BLUEPRINT.json`](./apps/000-stir-iescs-protocol-sdk/AGENT_BLUEPRINT.json) | `PASS (Exit 0)` | **PUBLISHED_LIVE** |
| **Drop #001** | [`001-seal-pdf-media-notary`](./apps/001-seal-pdf-media-notary/) | `seal_pdf_notary + utility_exif_scrubber` | Cryptographic Media Notary & EXIF Orientation / Privacy Scrubber | [`AGENT_BLUEPRINT.json`](./apps/001-seal-pdf-media-notary/AGENT_BLUEPRINT.json) | `PASS (Exit 0)` | **PUBLISHED_LIVE** |
| **Drop #002** | [`002-extract-pbr-material-synth`](./apps/002-extract-pbr-material-synth/) | `extract_pbr_materials` | Procedural Tangent-Space PBR Material & Normal Map Synthesizer | [`AGENT_BLUEPRINT.json`](./apps/002-extract-pbr-material-synth/AGENT_BLUEPRINT.json) | `PASS (Exit 0)` | **PUBLISHED_LIVE** |
| **Drop #003** | [`003-smart-timeline-stem-ducker`](./apps/003-smart-timeline-stem-ducker/) | `separate_audio_stems + smart_video_squeezer` | Agentic TimelineAST & FCPXML 1.10 Audio-Ducking Compiler | [`AGENT_BLUEPRINT.json`](./apps/003-smart-timeline-stem-ducker/AGENT_BLUEPRINT.json) | `PASS (Exit 0)` | **STAGED_QUEUE** |

---

## Companion Open-Source Repositories

- **[`WholeTroutMedia/open-source-bounties`](https://github.com/WholeTroutMedia/open-source-bounties)**: Upstream open-source PR ledger, root-cause case studies, public defense kits (`kits/`), and the free Maintainer Bot-Shield (`open-source-bot-shield.yml`).
- **[`WholeTroutMedia/oss-verification-sandbox`](https://github.com/WholeTroutMedia/oss-verification-sandbox)**: Client-side UTF-8 stream boundary, ASGI 3.0 lifespan, and PR readiness verification workbench ([live browser demo](https://wholetroutmedia.github.io/oss-verification-sandbox/)).
