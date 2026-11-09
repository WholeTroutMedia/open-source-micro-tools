#!/usr/bin/env python3
"""Verification Suite for STIR + IESCS Protocol SDK (000-stir-iescs-protocol-sdk)."""

import asyncio
from engine import (
    STIRASGIMiddleware,
    encode_stir_iescs_frame,
    format_git_commit_trailers,
    stir_verified,
    unpack_plain_english_receipt,
    verify_git_commit_trailers,
)


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

    # Verify Git Commit Trailer Standard (RFC-WTM-0001)
    trailers = format_git_commit_trailers(pkt_true)
    commit_check = verify_git_commit_trailers("feat: add liquidity check" + chr(10) + chr(10) + trailers)
    assert commit_check["verified"] is True

    # Verify @stir_verified decorator
    @stir_verified(call_word="&app:TEST_DEC_01", opcode="0x05", english_intent="Verify decorator wrapping")
    def sample_tool(x: int) -> int:
        return x * 2

    wrapped_out = sample_tool(21)
    assert wrapped_out["result"] == 42
    assert wrapped_out["stir_receipt"]["cryptographic_seal_verified"] is True

    # Verify STIRASGIMiddleware header injection
    captured_headers: dict[bytes, bytes] = {}

    async def dummy_app(scope, receive, send):
        await send({"type": "http.response.start", "status": 200, "headers": []})
        await send({"type": "http.response.body", "body": b"ok"})

    async def run_asgi_check():
        mw = STIRASGIMiddleware(dummy_app, call_word="&app:ASGI_GATE_01")

        async def receive():
            return {"type": "http.request"}

        async def send(msg):
            if msg["type"] == "http.response.start":
                for k, v in msg["headers"]:
                    captured_headers[k] = v

        await mw({"type": "http", "method": "GET", "path": "/health"}, receive, send)

    asyncio.run(run_asgi_check())
    assert captured_headers.get(b"x-inception-rosetta-upgrade") == b"STIR-IESCS/1.0"
    assert b"|SHA3:" in captured_headers.get(b"x-stir-receipt", b"")

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

    print("[PASS] 000-stir-iescs-protocol-sdk (STIR-1.0 + IESCS RFC-WTM-0001 Standard + ASGI Middleware + Git Trailers) verified (exit code 0).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
