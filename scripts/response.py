import time

log_file = "/var/log/suricata/fast.log"

with open(log_file, "r") as f:
    f.seek(0, 2)

    while True:
        line = f.readline()

        if not line:
            time.sleep(0.5)
            continue

        print("[ALERT]", line.strip())

        with open("alerts.log", "a") as alert_file:
            alert_file.write(line)
