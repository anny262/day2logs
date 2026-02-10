# Log Analysis & Parsing

## Objective
Detect brute-force patterns from Windows Security logs by clustering repeated failed logons and mapping the behavior to MITRE ATT&CK.

## Practical Summary
- Parsed `data/sample_logs.csv` for `event_code == 4625` (failed logon).
- Counted failures per `source_ip`.
- Flagged IPs with more than 5 failures as suspicious.

## Detection Logic
- **Fields:** `timestamp`, `event_code`, `source_ip`.
- **Rule:** `failed logons per IP > 5`.
- **Output:** IOC list (`iocs_ips.csv`).

## MITRE Mapping
- **T1110 – Brute Force** (repeated failed authentication attempts).
- **T1078 – Valid Accounts** (risk of credential abuse after successful compromise).

## Limitations
- Threshold-based approach is deterministic but may miss low-and-slow attacks.
- No behavioral baselining or anomaly detection used in this pass.

## Evidence
- Output file: `iocs_ips.csv`
- Script: `parse_logs.py`
