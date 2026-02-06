# Python Automation for SOC

## Objective
Automate IOC enrichment via VirusTotal and notify analysts via email.

## Practical Summary
- Built `soc_automation.py` to:
  - Parse failed logons.
  - Enrich suspicious IPs via VirusTotal (if API key present).
  - Send alert email (or dry-run preview).

## Bug Fix Highlight
- Ensured `reputation` is captured from the API response before evaluation.

## Example Usage
```bash
python soc_automation.py --dry-run
```

## Notes
- The script reads the same sample log data to stay consistent with the log parsing workflow.
- If `VT_API_KEY` is not set, enrichment is skipped and the script continues gracefully.

## Theory Links
- **NIST AU-6:** Audit review and reporting.
- **SOAR principles:** automated enrichment and routing.
