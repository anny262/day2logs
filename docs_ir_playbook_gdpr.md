# Incident Response Playbook Test + GDPR Mapping

## Scenario
Phishing email with spoofed sender targeting employee credentials.

## Playbook Steps
1. **Identification**: review email headers and authentication failures.
2. **Containment**: block sender IP/domain.
3. **Eradication**: scan endpoints for persistence artifacts.
4. **Recovery**: restore clean state from backups.
5. **Lessons Learned**: update training and detection rules.

## GDPR Mapping
- **Data minimization**: collect only relevant evidence.
- **Integrity & confidentiality**: restrict access to incident data.
- **Breach notification**: document timeline for 72-hour reporting window if applicable.

## Evidence & Timeline
- Maintain a CSV timeline of actions and artifacts.
- Store logs, hashes, and email headers for auditability.
