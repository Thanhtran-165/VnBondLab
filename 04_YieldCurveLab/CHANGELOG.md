# Changelog

## v3.4.0 — 2026-09-05

### Added
- Evidence package cho Bond Engine: component ranks, Pressure decomposition và 1W/1M/3M windows.
- Per-tenor evidence: Yield + 1D + 1W + 1M + 3M cho 1Y/2Y/3Y/5Y/7Y/10Y.
- Liquidity semantics tách IB trend khỏi relative-gap state.
- Gap Driver (`ΔGap = ΔIB - ΔPolicy`) cho 5/20 liquidity events.
- Liquidity event windows và range.
- Full Transmission direction matrix với trạng thái đồng thuận/phân kỳ/Bond-leading.
- Alignment quality và Last Valid Transmission.
- Early Observation, Active Contract và Research Trigger.
- AI benchmark và runtime evidence package.

### Preserved
- Dual Engine + Late Fusion architecture.
- IB lag contract 0–5 ngày.
- No VNINDEX.
- No forecast probability.
- No combined score.
- No causal attribution.

### Known limitations / runtime findings
- Pressure decomposition trên UI có thể có sai khác cộng trừ 0.1 do rounding khi hiển thị một chữ số; backend dùng precision đầy đủ.
- Trạng thái dưới ngưỡng Transmission có thể đi cùng một Gap Driver có hướng rõ; report cần phân biệt raw move với threshold classification.
- Overview đã gần giới hạn chiều cao; ưu tiên thay thế/đóng gói evidence thay vì tiếp tục thêm hàng vô hạn.
- Cần thêm runtime evidence cho Liquidity fresh, policy-only update, divergence và broad Bond shock.
