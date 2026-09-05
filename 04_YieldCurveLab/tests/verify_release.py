from pathlib import Path
import hashlib

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src" / "VN_YieldCurveLab_v3_4_0.pine"
BASE = ROOT / "tests" / "fixtures" / "VN_YieldCurveLab_v3_3_1_baseline.pine"

s = SRC.read_text(encoding="utf-8")
b = BASE.read_text(encoding="utf-8")
checks = []
def ck(name, cond): checks.append((name, bool(cond)))

ck("version_3_4", 'const string VERSION = "3.4.0"' in s)
ck("build_marker", "20260905-V340-EVIDENCE-SEMANTIC" in s)
ck("requests_8", s.count("request.security(") == 8)
ck("no_vnindex", "VNINDEX" not in s)
ck("no_combined_score", "combinedScore" not in s and "COMBINED SCORE" not in s)
ck("core_source_storage_regression",
   b[b.index("//============================ 03. SOURCE ACQUISITION"):b.index("//============================ 05. BOND ENGINE OUTPUT")] ==
   s[s.index("//============================ 03. SOURCE ACQUISITION"):s.index("//============================ 05. BOND ENGINE OUTPUT")])
ck("gap_driver", "f_gap_driver" in s and "liquidityGapDriver5" in s and "liquidityGapDriver20" in s)
ck("market_vs_gap_states", "liquidityIBTrend" in s and "liquidityGapStateLabel" in s)
ck("temporal_context", all(x in s for x in ["bondWindow5Start", "bondWindow20Start", "bondWindow60Start", "liquidityWindow5Start", "liquidityWindow20Start"]))
ck("alignment", "transmissionAlignmentLabel" in s and "transmissionMaxLagDays" in s)
ck("last_valid_tx", "lastValidTransmissionMessage" in s and "LAST VALID TRANSMISSION" in s)
ck("full_matrix", all(x in s for x in ["PHÂN KỲ NGƯỢC CHIỀU", "BOND DẪN HẠ NHIỆT", "BOND DẪN TĂNG ÁP LỰC", "HAI THỊ TRƯỜNG ÍT THAY ĐỔI"]))
ck("evidence_surface", all(x in s for x in ["RANK L/S/B/LONG", "PRESSURE Δ1M", "EARLY OBSERVATION", "ACTIVE CONTRACT", "RESEARCH TRIGGER"]))
ck("selftests_14", "selfTestCount := 14" in s)
ck("no_placeholders", all(x not in s for x in ["TODO", "TBD", "???"]))

failed = [name for name, ok in checks if not ok]
for name, ok in checks:
    print(("PASS " if ok else "FAIL ") + name)
print(f"TOTAL {len(checks)-len(failed)}/{len(checks)} PASS")
print("SOURCE_SHA256", hashlib.sha256(SRC.read_bytes()).hexdigest())
if failed:
    raise SystemExit("FAILED: " + ", ".join(failed))
