# 🕷️ ARP Spoofing Tool

A lightweight Python tool for performing ARP spoofing attacks using Scapy. It targets a victim and a gateway to become a man-in-the-middle (MITM), allowing packet interception on a local network. The tool also restores the ARP tables after interruption and supports IP forwarding for full packet relay.
![Image](https://github.com/user-attachments/assets/f868a627-0198-4223-9ec8-b9d946c7d39c)

---

## 📦 Features

- Sends crafted ARP replies to poison the ARP cache of the target and gateway
- Supports two-way spoofing (victim <-> gateway)
- Automatically restores ARP tables on exit
- Displays live spoofing status
- Clean and readable Python codebase
- Includes IP forwarding toggle instructions

---

## 🔧 Requirements

- Python 3.x  
- Scapy library (`pip install scapy`)
- Root privileges (required to send raw packets)
- Linux system (recommended)

---

## ⚙️ How to Use

```bash
# 1. Enable IP forwarding (required for traffic to pass through your machine)

sudo sysctl -w net.ipv4.ip_forward=1

# 2. Run the attack
sudo python3 EtherShade.py --target <TARGET_IP> --gateway <GATEWAY_IP>

# Example:
sudo python3 EtherShade.py --target 192.168.1.10 --gateway 192.168.1.1

# 3. Stop the attack with Ctrl+C
# The script will automatically restore the ARP tables of both the target and the gateway.

# 4. Disable IP forwarding (recommended after the attack)
sudo sysctl -w net.ipv4.ip_forward=0

#5. Verify status
cat /proc/sys/net/ipv4/ip_forward


```
🔒 Disclaimer
This tool is intended for educational purposes only. Unauthorized use on networks you do not own or have permission to test is illegal and unethical.


