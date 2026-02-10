import csv
from collections import Counter

INPUT_PATH = "data/sample_logs.csv"
OUTPUT_PATH = "iocs_ips.csv"
SUSPICIOUS_THRESHOLD = 5

with open(INPUT_PATH, newline="", encoding="utf-8") as handle:
    reader = csv.DictReader(handle)
    failed_ips = [row["source_ip"] for row in reader if row["event_code"] == "4625"]

ip_counts = Counter(failed_ips)
suspicious = {ip: count for ip, count in ip_counts.items() if count > SUSPICIOUS_THRESHOLD}

print("Suspicious IPs:")
for ip, count in sorted(suspicious.items(), key=lambda item: item[1], reverse=True):
    print(f"{ip}: {count}")

with open(OUTPUT_PATH, "w", newline="", encoding="utf-8") as handle:
    writer = csv.writer(handle)
    writer.writerow(["source_ip", "count"])
    for ip, count in sorted(suspicious.items(), key=lambda item: item[1], reverse=True):
        writer.writerow([ip, count])
