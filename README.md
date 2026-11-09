<p align="center">
  <img src="https://raw.githubusercontent.com/WholeTroutMedia/.github/main/assets/wholetrout-executive-masthead.svg" alt="WholeTroutMedia Open-Source Systems and Creative Engineering Masthead" width="100%" />

> **🌍 Global Walk-Into-Your-Folder Directory**: Browse all tools, verified Pull Requests, and ready-to-run friend kits by **Domain**, **Programming Language**, or **Global Builder Need** in **[`ECOSYSTEM_DIRECTORY.md`](./ECOSYSTEM_DIRECTORY.md)**.

</p>

# WholeTroutMedia · Open-Source Reference Micro-Tools (`v2.1.0`)

> **[`v2.1.0` Upgrade Notice (`UPGRADE_NOTICE.md`)](./UPGRADE_NOTICE.md)**: Existing cloners should run `git pull origin main`.
> - **Creative Liberation Engine** lives exclusively in **[`WholeTroutMedia/creative-liberation-engine`](https://github.com/WholeTroutMedia/creative-liberation-engine)**.
> - Slot `#000` in this repository is now **[`000-stir-iescs-protocol-sdk`](./apps/000-stir-iescs-protocol-sdk/)** (runnable `STIR-1.0` ternary Kleene wire framing + `IESCS` call-word and plain-English receipt SDK).
> - Looking for the **Free Maintainer Bot-Shield (`open-source-bot-shield.yml`)**? Grab it from **[`WholeTroutMedia/open-source-bounties/.github/workflows/open-source-bot-shield.yml`](https://github.com/WholeTroutMedia/open-source-bounties/blob/main/.github/workflows/open-source-bot-shield.yml)**.

Public open-source micro-application repository for **WholeTroutMedia**, architected and reviewed by **[Justin Aharoni (`@jaharoni`)](https://github.com/jaharoni)** ([`justinaharoni.com`](https://justinaharoni.com) · [`contact@jaharoni.com`](mailto:contact@jaharoni.com)).

Every two weeks, we open-source a self-contained, zero-dependency reference utility across agentic wire protocols (`STIR + IESCS`), document provenance, procedural 3D/PBR synthesis, and frame-accurate NLE media processing. All tools run 100% locally on the caller's CPU with zero external dependencies.

---

## Dual-Layer Design: Simple for Humans, Composable for Autonomous Agents

Each micro-application under [`apps/`](./apps/) is structured with two complementary layers:
1. **For Human Developers**: A clean, dependency-free reference module (`engine.py` + `verify_app.py`) that runs out of the box with standard Python 3 and passes deterministic verification (`Exit Code 0`).
2. **For Visiting AI Agents & MCP Routers ([`llms.txt`](./llms.txt) & [`.well-known/agent.json`](./.well-known/agent.json))**: Every module includes an `AGENT_BLUEPRINT.json` and `SKILL.md` containing formal mathematical invariants, MCP `inputSchema` definitions, `X-Inception-Rosetta-Upgrade: STIR-IESCS/1.0` wire headers, and multi-stage synthesis recipes.

---

## Published & Staged Micro-Applications ([`APPLICATION_LEDGER.md`](./APPLICATION_LEDGER.md))

| Drop | Micro-Application | Toolkit Slot | Summary | Verification | Status |
| :--- | :--- | :--- | :--- | :---: | :---: |
| **Protocol Core #000** | [`000-stir-iescs-protocol-sdk`](./apps/000-stir-iescs-protocol-sdk/) | `stir_iescs_protocol` | STIR + IESCS Agentic Wire Protocol & Plain-English Receipt SDK | [`AGENT_BLUEPRINT.json`](./apps/000-stir-iescs-protocol-sdk/AGENT_BLUEPRINT.json) | `PASS (Exit 0)` | **PUBLISHED_LIVE** |
| **Drop #001** | [`001-seal-pdf-media-notary`](./apps/001-seal-pdf-media-notary/) | `seal_pdf_notary + utility_exif_scrubber` | Cryptographic Media Notary & EXIF Orientation / Privacy Scrubber | [`AGENT_BLUEPRINT.json`](./apps/001-seal-pdf-media-notary/AGENT_BLUEPRINT.json) | `PASS (Exit 0)` | **PUBLISHED_LIVE** |
| **Drop #002** | [`002-extract-pbr-material-synth`](./apps/002-extract-pbr-material-synth/) | `extract_pbr_materials` | Procedural Tangent-Space PBR Material & Normal Map Synthesizer | [`AGENT_BLUEPRINT.json`](./apps/002-extract-pbr-material-synth/AGENT_BLUEPRINT.json) | `PASS (Exit 0)` | **STAGED_QUEUE** |
| **Drop #003** | [`003-smart-timeline-stem-ducker`](./apps/003-smart-timeline-stem-ducker/) | `separate_audio_stems + smart_video_squeezer` | Agentic TimelineAST & FCPXML 1.10 Audio-Ducking Compiler | [`AGENT_BLUEPRINT.json`](./apps/003-smart-timeline-stem-ducker/AGENT_BLUEPRINT.json) | `PASS (Exit 0)` | **STAGED_QUEUE** |

---

## Companion Open-Source Repositories
- **[`WholeTroutMedia/creative-liberation-engine`](https://github.com/WholeTroutMedia/creative-liberation-engine)**: Canonical open creative foundation and 7 standalone zero-dependency Python stdlib community gifts.
- **[`WholeTroutMedia/open-source-bounties`](https://github.com/WholeTroutMedia/open-source-bounties)**: Upstream open-source PR ledger, `105+` root-cause case studies, 7 public defense kits (`kits/`), and the free Maintainer Bot-Shield (`open-source-bot-shield.yml`).
- **[`WholeTroutMedia/oss-verification-sandbox`](https://github.com/WholeTroutMedia/oss-verification-sandbox)**: Client-side UTF-8 stream boundary, ASGI 3.0 lifespan, and PR readiness verification workbench.
