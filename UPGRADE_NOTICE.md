# WholeTroutMedia Release Notice · `v2.1.0` (2026-11-09 09:12 UTC)

If you previously cloned any **WholeTroutMedia** repository (`creative-liberation-engine`, `open-source-micro-tools`, `open-source-bounties`, or `oss-verification-sandbox`), pull the latest `main` branch (`git pull origin main`) or download the `v2.1.0` release tag for three major upgrades:

1. **Unified Single-Home Architecture for Creative Liberation Engine**:
   - **[`WholeTroutMedia/creative-liberation-engine`](https://github.com/WholeTroutMedia/creative-liberation-engine)** is the sole canonical repository for the **Creative Liberation Engine** and its 7 standalone Python stdlib community gifts (`gifts/`).
   - The legacy duplicate seed folder (`apps/000-cle-foundation-seed-os`) inside `WholeTroutMedia/open-source-micro-tools` has been retired and replaced by **[`apps/000-stir-iescs-protocol-sdk`](./apps/000-stir-iescs-protocol-sdk/)**.
2. **Runnable `STIR + IESCS` Agentic Wire Protocol SDK (`X-Inception-Rosetta-Upgrade: STIR-IESCS/1.0`)**:
   - Zero-dependency Python stdlib implementation of **STIR-1.0** (Sovereign Ternary Inter-Agent Relay using Kleene logic `{-1, 0, +1}` and CRC32C framing) and **IESCS** (compact `&domain:op{...}` call-words that automatically expand into plain-English human audit receipts).
   - Available directly at [`apps/000-stir-iescs-protocol-sdk/engine.py`](./apps/000-stir-iescs-protocol-sdk/engine.py), in [`creative-liberation-engine/gifts/stir_iescs_rosetta_doctor.py`](https://github.com/WholeTroutMedia/creative-liberation-engine/blob/main/gifts/stir_iescs_rosetta_doctor.py), and in [`open-source-bounties/kits/stir-iescs-agent-protocol/stir_iescs.py`](https://github.com/WholeTroutMedia/open-source-bounties/blob/main/kits/stir-iescs-agent-protocol/stir_iescs.py).
3. **Maintainer Bot-Shield (`v2.1`) & 7 Free Public Defense Kits**:
   - The zero-dependency GitHub Actions workflow [`open-source-bot-shield.yml`](https://github.com/WholeTroutMedia/open-source-bounties/blob/main/.github/workflows/open-source-bot-shield.yml) (also mirrored at `templates/open-source-bot-shield.yml`) is now live at both paths so maintainers can copy-paste it in one step to block automated bounty-farming and duplicate spam PRs.

## Quick Upgrade Commands for Existing Clones
```bash
git fetch --all --tags
git pull origin main
python3 apps/000-stir-iescs-protocol-sdk/verify_app.py
```
