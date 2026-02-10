# Network Threat Intelligence & Forensics Report

## Objective
Identify suspicious HTTP traffic and extract network IOCs.

## Practical Steps
- Wireshark filter: `tcp.port == 80`
- Follow TCP Stream to inspect payloads.
- Extract suspected SQLi payloads (e.g., `' OR 1=1`).

## Observed Indicators
- IOC Type: HTTP payload signature
- Example Payload: `' OR 1=1`
- Confidence: High (clear injection pattern)

## MITRE Mapping
- **T1046 – Network Service Scanning** (recon and probing behavior)

## Recommendations
- Add WAF rules for SQLi signatures.
- Monitor for repeated injection attempts.
