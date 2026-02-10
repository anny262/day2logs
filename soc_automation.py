import argparse
import csv
import os
import smtplib
from email.message import EmailMessage
from typing import Iterable, List

INPUT_PATH = "data/sample_logs.csv"
VT_BASE_URL = "https://www.virustotal.com/api/v3/ip_addresses/"
SUSPICIOUS_THRESHOLD = 5


def load_failed_ips(path: str) -> List[str]:
    with open(path, newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return [row["source_ip"] for row in reader if row["event_code"] == "4625"]


def find_suspicious_ips(ips: Iterable[str], threshold: int) -> List[str]:
    counts = {}
    for ip in ips:
        counts[ip] = counts.get(ip, 0) + 1
    return [ip for ip, count in counts.items() if count > threshold]


def fetch_reputation(ip: str, api_key: str) -> int:
    import requests

    headers = {"x-apikey": api_key}
    response = requests.get(f"{VT_BASE_URL}{ip}", headers=headers, timeout=30)
    response.raise_for_status()
    data = response.json()
    return int(data["data"]["attributes"]["reputation"])


def build_email(subject: str, body: str, sender: str, recipient: str) -> EmailMessage:
    message = EmailMessage()
    message["Subject"] = subject
    message["From"] = sender
    message["To"] = recipient
    message.set_content(body)
    return message


def send_email(message: EmailMessage, smtp_host: str, smtp_port: int, dry_run: bool) -> None:
    if dry_run:
        print("[DRY RUN] Email content:\n")
        print(message)
        return

    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.send_message(message)


def main() -> None:
    parser = argparse.ArgumentParser(description="Enrich suspicious IPs and send alert email.")
    parser.add_argument("--api-key", default=os.getenv("VT_API_KEY"))
    parser.add_argument("--smtp-host", default="localhost")
    parser.add_argument("--smtp-port", type=int, default=25)
    parser.add_argument("--sender", default="soc-alerts@example.com")
    parser.add_argument("--recipient", default="analyst@example.com")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    failed_ips = load_failed_ips(INPUT_PATH)
    suspicious_ips = find_suspicious_ips(failed_ips, SUSPICIOUS_THRESHOLD)

    if not suspicious_ips:
        print("No suspicious IPs detected.")
        return

    reputations = {}
    if args.api_key:
        for ip in suspicious_ips:
            reputations[ip] = fetch_reputation(ip, args.api_key)
    else:
        print("VT API key not provided; skipping reputation enrichment.")

    lines = ["SOC Alert: Suspicious login activity detected.", "", "Indicators:"]
    for ip in suspicious_ips:
        reputation = reputations.get(ip, "N/A")
        lines.append(f"- {ip} (VT reputation: {reputation})")
    body = "\n".join(lines)

    message = build_email(
        subject="SOC Alert: Potential brute-force activity",
        body=body,
        sender=args.sender,
        recipient=args.recipient,
    )
    send_email(message, args.smtp_host, args.smtp_port, args.dry_run)


if __name__ == "__main__":
    main()
