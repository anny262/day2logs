# ELK + SOAR Integration Notes

## Objective
Use ELK queries to detect authentication failures and trigger SOAR alerts.

## Example Kibana Query
```
event.type:login AND authentication_result:fail AND @timestamp >= now-1h
```

## Visualization & Alerting
- Create a bar chart of failed logons per source IP.
- Set an alert threshold based on historical baselines.

## SOAR Trigger Logic
- When threshold is exceeded, send an alert with IOC list and context.
- Example: POST findings to a SOAR endpoint (mocked in automation flow).

## Theory
- ELK centralizes log ingestion and indexing.
- SOAR enables rapid orchestration and response.
- Gartner SOC maturity Level 3 emphasizes proactive automation.
