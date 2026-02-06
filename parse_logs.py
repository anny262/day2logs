import pandas as pd

logs = pd.read_csv("data/sample_logs.csv")

failed = logs[logs["event_code"] == 4625]

ip_counts = failed["source_ip"].value_counts()

suspicious = ip_counts[ip_counts > 5]

print("Suspicious IPs:")
print(suspicious)

suspicious.to_csv("iocs_ips.csv")
