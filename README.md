# Day 2 Logs – Log Analysis Project

This repository contains the Day 2 SOC exercise scaffold, including sample Windows Security logs, a parsing script, and documentation notes.

## Project Structure

```
./
├── data/
│   └── sample_logs.csv
├── parse_logs.py
├── log_analysis_notes.md
└── iocs_ips.csv
```

## What the Script Does

- Reads `data/sample_logs.csv`
- Filters failed logon events (`event_code == 4625`)
- Counts failed attempts per `source_ip`
- Outputs suspicious IPs (count > 5) to `iocs_ips.csv`

## How to Run

```bash
python parse_logs.py
```

Expected output is a list of suspicious IPs plus a CSV file with the same results.

## Reports / Notes

- `log_analysis_notes.md` contains a SOC-style summary of findings and MITRE ATT&CK mapping.
- `iocs_ips.csv` contains the extracted indicators of compromise from the sample data.
