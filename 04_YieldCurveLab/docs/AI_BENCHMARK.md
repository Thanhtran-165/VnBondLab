# V3.4 AI Evidence Benchmark

Dùng source Pine tương ứng + một screenshot Overview.

## Critical extraction
1. Bond as-of date?
2. Liquidity IB as-of và policy as-of?
3. Current vs Last Valid Transmission khác nhau thế nào?
4. IB lag bao nhiêu và có eligible cho Late Fusion không?

## Deterministic recalculation
5. Tính lại Level từ 2Y/5Y/10Y.
6. Tính lại Slope 10Y–2Y.
7. Kiểm tra Pressure từ Rank Level/Slope/Belly theo source.
8. Kiểm tra breadth tuần/tháng từ six-tenor changes.
9. Kiểm tra ΔGap = ΔIB - ΔPolicy.

## Temporal reasoning
10. Cửa sổ Bond 1W/1M/3M là ngày nào?
11. Cửa sổ Liquidity 5E/20E là ngày nào?
12. Transmission alignment EXACT hay AS-OF?
13. Last-valid result thuộc khoảng thời gian nào?

## Semantic discipline
14. Gap thu hẹp vì IB giảm hay policy tăng?
15. IB state và Relative Gap state có khác nhau không?
16. Bond/Liquidity đồng thuận, phân kỳ hay chưa đủ điều kiện?
17. Có được suy ra causal transmission không? (Đáp án: không.)
18. Research Trigger yêu cầu tìm bằng chứng nào bên ngoài?

## Runtime scenarios cần tích lũy
- Bond valid / Liquidity stale.
- Bond + Liquidity fresh.
- Gap down due IB down.
- Gap down due policy up.
- Liquidity down + Bond up.
- Liquidity up + Bond down.
- Broad Bond shock.
