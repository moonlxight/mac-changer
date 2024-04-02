import os
import sys
import random
import subprocess
import arts
import re
from os import system, name
from sys import stdout, stderr
from colorama import Fore, Style, init

init()

def mac_changer():
    charList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    newMac = ""
    for i in range(6):
        newMac += random.choice(charList) + random.choice(charList)
        if i < 5:
            newMac += ":"
    try:
        # Check the network interface name (You can customize this based on your system)
        interface_name = "eth0"
        # Check the current MAC address
        ifconfigResult = subprocess.check_output(f"ifconfig {interface_name}", shell=True).decode()
        oldMac = re.search("ether(.*?)txqueuelen", ifconfigResult).group(1).strip()
        # Change MAC address
        subprocess.check_output(f"ifconfig {interface_name} down", shell=True)
        subprocess.check_output(f"ifconfig {interface_name} hw ether {newMac}", shell=True)
        subprocess.check_output(f"ifconfig {interface_name} up", shell=True)
        print(Fore.LIGHTGREEN_EX + f" [SUCCESS] MAC address successfully changed to: {newMac}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + " [WARNING] An error occurred while changing MAC address." + Style.RESET_ALL)
    input("Press Enter to continue...")

def display_menu():
    stdout.write(Fore.RED + arts.mac_address)
    stdout.write(Fore.LIGHTCYAN_EX + arts.changer)
    stdout.write(Fore.YELLOW + arts.dev)
    stdout.write("\n"+"[1] Change MAC Address" + "\n")
    stdout.write("[2] Show Current MAC Address" + "\n")
    stdout.write("[3] Exit\n")

def show_current_mac():
    try:
        # Check the network interface name (You can customize this based on your system)
        interface_name = "eth0"
        # Check the current MAC address
        ifconfigResult = subprocess.check_output(f"ifconfig {interface_name}", shell=True).decode()
        current_mac = re.search("ether(.*?)txqueuelen", ifconfigResult).group(1).strip()
        print(Fore.LIGHTGREEN_EX + f" [SUCCESS] Current MAC Address: {current_mac}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + " [WARNING] An error occurred while retrieving current MAC address." + Style.RESET_ALL)
    input("Press Enter to continue...")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            mac_changer()
        elif choice == "2":
            show_current_mac()
        elif choice == "3":
            print("Exiting...")
            sys.exit()
        else:
            print(Fore.RED + " [!] Invalid choice. Please enter a valid option." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
