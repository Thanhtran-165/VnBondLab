# Runtime Evidence

## RE-001 — 2026-09-05 17:00 UTC+7

File: `VN10Y_2026-09-05_17-00-47.png`

Environment:
- TradingView
- Symbol: `TVC:VN10Y`
- Timeframe: `1D`
- Indicator: VN YieldCurveLab 3.4

Observed runtime state:
- Bond as-of: 04/09/2026.
- Bond conclusion: mặt bằng cao, chưa hạ nhiệt rộng.
- Liquidity IB as-of: 28/08/2026.
- Policy as-of: 31/08/2026.
- Liquidity freshness: stale, lag 7 ngày.
- Current Transmission: not ready vì Liquidity Engine chưa sẵn sàng.
- Last Valid Transmission vẫn được hiển thị như historical snapshot riêng.
- Evidence surface hiển thị component ranks, Pressure decomposition, per-tenor 1D/1W/1M/3M, event windows/ranges, Active Contract và Research Trigger.

Runtime findings cần theo dõi:
1. Pressure decomposition UI có thể lệch 0.1 khi cộng các số đã round một chữ số; cần hiểu đây là presentation rounding, không tự suy ra backend sai.
2. Raw Gap move có thể có hướng rõ nhưng vẫn dưới threshold Transmission; report phải phân biệt raw move với classification threshold.
3. Dashboard gần giới hạn chiều cao của một screenshot; không nên tiếp tục thêm hàng nếu chưa loại/ghép evidence khác.

Cần thu thêm runtime cases:
- Liquidity fresh.
- Gap down do IB down.
- Gap down do policy up.
- Liquidity down + Bond up.
- Liquidity up + Bond down.
- Broad Bond shock.
