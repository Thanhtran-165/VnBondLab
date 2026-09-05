from pathlib import Path
import re, sys
src_path = Path(sys.argv[1]) if len(sys.argv)>1 else Path('VN_YieldCurveLab_V3_4_0_EVIDENCE_SEMANTIC_20260905.pine')
s = src_path.read_text(encoding='utf-8')
checks = {
    'version': 'const string VERSION = "3.4.0"' in s,
    'build': 'V340-EVIDENCE-SEMANTIC' in s,
    'gap_driver': 'f_gap_driver' in s and 'liquidityGapDriver5' in s,
    'liq_two_states': 'liquidityIBTrend' in s and 'liquidityGapStateLabel' in s,
    'ranges': 'f_recent_range' in s and 'liquidityIBRange20' in s,
    'bond_windows': 'bondWindow5Start' in s and 'bondWindow60Start' in s,
    'liq_windows': 'liquidityWindow5Start' in s and 'liquidityWindow20Start' in s,
    'alignment': 'transmissionAlignmentLabel' in s and 'transmissionMaxLagDays' in s,
    'last_valid_tx': 'lastValidTransmissionMessage' in s and 'LAST VALID TRANSMISSION' in s,
    'full_matrix': all(x in s for x in ['PHÂN KỲ NGƯỢC CHIỀU', 'BOND DẪN HẠ NHIỆT', 'BOND DẪN TĂNG ÁP LỰC', 'HAI THỊ TRƯỜNG ÍT THAY ĐỔI']),
    'early_observation': 'EARLY OBSERVATION' in s and 'bondEarlyObservation' in s,
    'active_contract': 'ACTIVE CONTRACT' in s,
    'research_trigger': 'RESEARCH TRIGGER' in s and 'researchTrigger' in s,
    'rank_evidence': 'RANK L/S/B/LONG' in s,
    'pressure_decomp_ui': 'PRESSURE Δ1M' in s,
    'tenor_1d_1w_1m_3m': all(x in s for x in ['1D bp', '1W bp', '1M bp', '3M bp']),
    'no_vnindex': 'VNINDEX' not in s,
    'no_combined_score': 'combinedScore' not in s and 'COMBINED SCORE' not in s,
    'requests_8': s.count('request.security(') == 8,
}
failed=[k for k,v in checks.items() if not v]
print(f"checks={len(checks)} pass={len(checks)-len(failed)} fail={len(failed)}")
for k,v in checks.items(): print(('PASS ' if v else 'FAIL ')+k)
if failed: raise SystemExit(1)
