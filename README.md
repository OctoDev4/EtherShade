# 🛠️ ARP Spoofing Tool

A lightweight and educational ARP spoofing script built with Python and Scapy. This tool allows you to perform ARP poisoning attacks by impersonating the gateway or a target device on a local network.

---

## 📋 Features

* Sends forged ARP replies to poison ARP cache.
* Supports restoring ARP tables when stopped (CTRL+C).
* Displays real-time packet count.
* Fully modular structure (network and console utilities separated).

---

## ⚙️ Requirements

* Python 3.x
* Scapy library (`pip install scapy`)
* Root privileges (for sending raw packets)

---

## 🚀 How to Use

```bash
sudo python3 EtherShade.py --target <TARGET_IP> --gateway <GATEWAY_IP>
```

**Example:**

```bash
sudo python3 EtherShade.py --target 192.168.1.10 --gateway 192.168.1.1
```

This will begin sending spoofed ARP packets to both the target and the gateway every 2 seconds.

To stop the attack and restore the network, press `CTRL+C`.

---

## 🔒 Disclaimer

This tool is for **educational** and **ethical hacking** purposes only. Always ensure you have **explicit permission** to test a network.
