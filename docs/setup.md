1. Install Suricata

sudo apt update
sudo apt install suricata -y

2. Verify installation

suricata --build-info

3. Add custom rules

configs/custom.rules

4. Start monitoring

sudo suricata -i eth0 -S configs/custom.rules

5. View alerts

tail -f /var/log/suricata/fast.log

6. Run dashboard

python3 scripts/dashboard.py
