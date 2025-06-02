import random
import socket as sk
import threading
import sqlite3
import re
import time
from scapy.all import *
import argparse


ip_pattern = r'''
^
(                                  # Start of IP
  (25[0-5]|                        # 250–255
   2[0-4][0-9]|                    # 200–249
   1[0-9]{2}|                      # 100–199
   [1-9][0-9]?|                    # 1–99
   0)                              # 0
  \.
){3}
(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]?|0)   # Last segment
$
'''

pars = argparse.ArgumentParser(description="A multi-funcion hacking and reconaissance tool.")
pars.add_argument("--help" or "-h", )

socket_main = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
code_status : bool = True

def menu():
    print("|----------------------------------|")
    print("|       Automatic Hack tool        |")
    print("|----------------------------------|")
    print("| 1. Main attack procedure         |")
    print("| 2. Scan network                  |")
    print("| 3. Scan target                   |")
    print("| 4. Targets history               |")
    print("| 5. Exploit types                 |")
    print("| 6. Exit program                  |")
    print("|----------------------------------|")
    print("\nSelect a option for the tool: ", end="")


def main_attack():
    print("|----------------------------------|")
    print("|       MAIN ATTACK PROCEDURE      |")
    print("|----------------------------------|")
    print("|  Target IP: 000.000.000.000      |")
    print("|----------------------------------|")
    print("Insert the target's IP address (type 'back' to return): ", end="")
    

def scan_network():
    return 0

def scan_target():
    print(r"Instert the target's ip address")
    ip_aim = input()
    if re.fullmatch(ip_pattern, ip_aim, re.VERBOSE):
        print(f"Valid ip address! Scanning {ip_aim} for open ports and services...")
        time.sleep(0.5)
        for port in range(1, 1025):
            try:
                skt = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

                skt.settimeout(0.2)
                result = skt.connect_ex((ip_aim, port))
                if result == 0:
                    print(f"port {port} is open! :D")
                skt.close()
            except Exception as e:
                print(f"Error scanning {port} port: {e}")
        time.sleep(1)

def history():
    return 0

def exploits():
    return 0

while(code_status):
    menu()
    select_main_menu = int(input())

    if select_main_menu == 1:
        session_main_attack : bool = True
        while(session_main_attack):
            main_attack()
            target_ipadd = input()
            if target_ipadd == "back":
                session_main_attack = False
            elif re.fullmatch(ip_pattern, target_ipadd, re.VERBOSE):
                print("|----------------------------------|")
                print("|       MAIN ATTACK PROCEDURE      |")
                print("|----------------------------------|")
                print("|  Target IP: " + target_ipadd)
                print("|----------------------------------|")
                session_main_attack = False
                time.sleep(1)
            else:
                print("\nthat is not a valid entry, please try again.")
                time.sleep(1)


    elif select_main_menu == 2:
        scan_network()
    elif select_main_menu == 3:
        scan_target()
    elif select_main_menu == 4:
        history()
    elif select_main_menu == 5:
        exploits()
    elif select_main_menu == 6:
        code_status = False
    else:
        print("this is not a valid option, try again.\n")
