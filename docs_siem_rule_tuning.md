# SIEM Rule Engineering & Tuning (Wazuh)

## Objective
Tune failed-login detection rules to reduce false positives and improve correlation fidelity.

## Practical Notes
- Added frequency/timeframe correlation to detect repeated failures from the same source.
- Included explicit MITRE mapping to align alerts with ATT&CK.

## Example Rule (Wazuh XML)
```xml
<rule id="100001" level="10">
  <if_sid>5700</if_sid>
  <frequency>6</frequency>
  <timeframe>120</timeframe>
  <description>Multiple failed logins from same source IP</description>
  <mitre>T1110</mitre>
</rule>
```

## Tuning Rationale
- **Frequency + timeframe** establishes correlation (6 failed logons in 2 minutes).
- **MITRE mapping** improves reporting and threat alignment.
- **Whitelisting** internal IPs reduces noise and false positives.

## MITRE Mapping
- **T1110 – Brute Force**
- **TA0001 – Initial Access**

## Outcomes
- Lower alert noise.
- Clearer escalation criteria for SOC triage.
