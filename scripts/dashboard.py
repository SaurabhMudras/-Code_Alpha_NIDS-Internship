import re
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

log_file = "/var/log/suricata/fast.log"

alerts = []

with open(log_file, "r") as f:
    for line in f:
        match = re.search(r'\] (.*?) \[\*\*\]', line)

        if match:
            alerts.append(match.group(1))

counter = Counter(alerts)

df = pd.DataFrame(
    counter.items(),
    columns=["Alert Type", "Count"]
)

print(df)

plt.figure(figsize=(8,5))
plt.bar(df["Alert Type"], df["Count"])
plt.title("Suricata Alert Statistics")
plt.xlabel("Alert Type")
plt.ylabel("Count")
plt.tight_layout()

plt.savefig("alert_statistics.png")

print("\nDashboard generated: alert_statistics.png")
