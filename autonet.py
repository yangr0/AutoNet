#!/usr/bin/python3

# Created by inc0gnit0

# Please don't copy this code without my permission



# MODULES #

try:

	import speech_recognition as sr

	import os

	import random

	import time

except ImportError:

	print("  You did not follow the instructions")

	print("\n")

	print("  I will do them for you...")

	time.sleep(3)

	os.system("chmod +x * && sudo ./install.sh")



# Check if root #

if os.geteuid() != 0:

	print("  Please run as root!")



# COLORS #

red = "\u001b[31;1m"

reset = "\u001b[0m"

green = "\u001b[32;1m"

cyan = "\u001b[36;1m"

yellow = "\u001b[33;1m"

magenta = "\u001b[35;1m"

blue = "\u001b[34;1m"

white = "\u001b[37;1m"

list = [red, green, cyan, yellow, magenta, blue] # List of colors to chose from #



os.system("clear")

for x in range(5): # Loading Effect #

	print(random.choice(list) + "|")

	time.sleep(0.1)

	os.system("clear")

	print(random.choice(list) + "/")

	time.sleep(0.1)

	os.system("clear")

	print(random.choice(list) + "-")

	time.sleep(0.1)

	os.system("clear")

	print(random.choice(list) + "\\")

	time.sleep(0.1)

	os.system("clear")

	print(random.choice(list) + "|")

	time.sleep(0.1)

	os.system("clear")

print(random.choice(list) + "  AutoNet is starting")

time.sleep(3)

os.system("clear") # Clear the terminal #



# BANNER #

def banner():

	print("\n")
	print(random.choice(list) + "                                https://github.com/iinc0gnit0/AutoNet")
	print("\n")
	time.sleep(0.1)
	print(random.choice(list) + "                                                888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                              888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                            888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                          888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                        88888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                      888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                    88888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                  888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                88888888")
	time.sleep(0.1)
	print(random.choice(list) + "    888888888888              888888888                  8888888888888")
	time.sleep(0.1)
	print(random.choice(list) + "    888888888888            888888888                    8888888888888")
	time.sleep(0.1)
	print(random.choice(list) + "    888888888888              888888888                  8888888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                  888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                    888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                      88888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                        888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                          888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                            888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                              888888888")
	time.sleep(0.1)
	print(random.choice(list) + "          88                    888888                    88   88    888888")
	time.sleep(0.1)
	print(random.choice(list) + "                               88   888                        88   88   888")
	time.sleep(0.1)
	print(random.choice(list) + "          88 88888888  888888  88  8 88  888888  88888888 88 888888 88  8 88")
	time.sleep(0.1)
	print(random.choice(list) + "          88 88    88 8        88 8  88 88    88 88    88 88   88   88 8  88")
	time.sleep(0.1)
	print(random.choice(list) + "          88 88    88 88    88 888  888 88    88 88    88 88   88   888   88")
	time.sleep(0.1)
	print(random.choice(list) + "          88 88    88  888888   888888   8888888 88    88 88   88    888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                             888")
	time.sleep(0.1)
	print(random.choice(list) + "                                         888888" + red + "                                v1.2")
	time.sleep(0.1)
	print("\n")
	print(random.choice(list) + "                                     Created by: inc0gnit0")
	time.sleep(0.1)
	print("\n")
	print(random.choice(list) + "                                     GitHub: iinc0gnit0")
	time.sleep(0.1)
	print("\n")
	print(random.choice(list) + "                                     Email: iinc0gnit0@pm.me")
	time.sleep(0.1)
	print("\n")
	print(random.choice(list) + "                                     Instagram: i.nc0gnit0")
	time.sleep(0.1)
	print("\033[0m")



# Main #

def main():

	banner()

	# Variables #

	print("\n")

	range = input(random.choice(list) + "                            range of IP adress(ex: 192.168.0.0/8): ")

	print("\n")

	passive = input(random.choice(list) + "           do you want to sniff only(passive mode) blank for no, [y/yes] for yes: ")

	print("\n")

	interface = input(random.choice(list) + "                     what interface do you want to use(ex: wlan0): ")

	print("\n")

	fs = input(random.choice(list) + "     do you want to enable fast scan(only scans .1, .100, .254) blank for no, [y/yes] for yes: ")

	# Checks #

	range = " -r " + range

	interface = " -i " + interface

	if passive in "y" or "yes":

		passive = " -p"

	elif fs in "y" or "yes":

		fs = " -f"

	os.system("netdiscover" + range + passive + interface + fs)



# START #

try:

	if __name__ == "__main__":

		main()

except KeyboardInterrupt: # Catch KeyboardInterruption errors #

	print("\n")

	print("  KeyboardInterrupt detected, Exiting...")

	print("\n")

	print(random.choice(list) + "  Have a nice day!! \033[0m")

	print("\n")

	time.sleep(3)

	os.system("clear")

	exit(1)
