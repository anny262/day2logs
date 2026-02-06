# Day 2 SOC Portfolio (Refresh)

Αυτό το repo είναι το ολοκληρωμένο portfolio για την Ημέρα 2 (SOC Analyst). Περιλαμβάνει parsing logs, SIEM rule tuning, automation, network forensics, IR playbooks και ELK/SOAR notes.

## About This Repository
This project is a day‑by‑day SOC learning portfolio. It showcases detection logic, automation, and documentation standards using realistic workflows and SOC-style reporting.

## Portfolio Snapshot
**SOC Analyst Focus:** detection engineering, automation mindset, network IOC analysis, incident response workflow, SOC-style documentation.

### CV-Style Highlights
- Designed brute-force detections mapped to MITRE ATT&CK.
- Tuned SIEM rules with correlation windows to reduce false positives.
- Automated IOC enrichment and alerting with Python.
- Conducted network forensics analysis and documented IR playbooks.

## Project Structure
```
./
├── data/
│   └── sample_logs.csv
├── parse_logs.py
├── soc_automation.py
├── iocs_ips.csv
├── log_analysis_notes.md
├── requirements.txt
├── docs_advanced_log_analysis.md
├── docs_siem_rule_tuning.md
├── docs_python_automation.md
├── docs_git_workflows.md
├── docs_network_forensics.md
├── docs_ir_playbook_gdpr.md
├── docs_elk_soar_integration.md
└── docs_reflection_notes.md
```

## Running the Scripts
### Log Parsing
```bash
python parse_logs.py
```

### SOC Automation (Dry Run)
```bash
python soc_automation.py --dry-run
```

## Reports & Notes
- **Log parsing + MITRE mapping:** `docs_advanced_log_analysis.md`
- **SIEM rule tuning notes:** `docs_siem_rule_tuning.md`
- **Python automation notes:** `docs_python_automation.md`
- **Git workflows notes:** `docs_git_workflows.md`
- **Network forensics report:** `docs_network_forensics.md`
- **IR playbook test + GDPR mapping:** `docs_ir_playbook_gdpr.md`
- **ELK/SOAR integration notes:** `docs_elk_soar_integration.md`
- **Reflection notes:** `docs_reflection_notes.md`

## Skills Demonstrated
- Detection logic
- Automation mindset
- Network IOC analysis
- Incident response flow
- SOC-style documentation
