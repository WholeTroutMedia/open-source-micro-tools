#!/usr/bin/env python3
"""Verification Suite for STIR + IESCS Protocol SDK (000-stir-iescs-protocol-sdk)."""

from engine import encode_stir_iescs_frame, unpack_plain_english_receipt


def main() -> int:
    pkt_true = encode_stir_iescs_frame(
        "Verify ETH/USDC liquidity pool slippage and oracle freshness invariants on Base L2.",
        call_word="&app:EPIS_ARB_11",
        opcode="0x0B",
        ternary_state=1,
        max_usdc=0.00125,
        params={"pair": "ETH-USDC", "notional_usd": 250000, "max_slippage_bps": 12},
    )
    rec_true = unpack_plain_english_receipt(pkt_true)
    assert rec_true["cryptographic_seal_verified"] is True
    assert pkt_true["token_reduction_pct"] >= 95.0
    assert pkt_true["settled_usdc"] == 0.000625

    pkt_unknown = encode_stir_iescs_frame(
        "Check unconfirmed L2 bridge block finality before releasing escrow.",
        call_word="&app:AEGIS_FW_02",
        opcode="0x02",
        ternary_state=0,
        max_usdc=0.00125,
        params={"bridge_block": 19482110},
    )
    rec_unknown = unpack_plain_english_receipt(pkt_unknown)
    assert rec_unknown["cryptographic_seal_verified"] is True
    assert pkt_unknown["settled_usdc"] == 0.0
    assert rec_unknown["buyer_protection_status"] == "AUTO_REFUND_ZERO_CHARGE"

    print("[PASS] 000-stir-iescs-protocol-sdk (STIR-1.0 + IESCS v2.1.0) verified (exit code 0).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
