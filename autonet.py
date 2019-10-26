#!/usr/bin/python3

# Created by inc0gnit0

# Please don't copy this code without my permission



# MODULES #

try:

	import os

	import random

	import time

except ImportError:

	print("  You did not follow the instructions")

	print("\n")

	print("  I will do them for you...")

	time.sleep(3)

	os.system("chmod +x * && sudo ./install.sh")



# COLORS #

red = "\033[31;1m"

reset = "\033[0m"

green = "\033[32;1m"

cyan = "\033[36;1m"

yellow = "\033[33;1m"

magenta = "\033[35;1m"

blue = "\033[34;1m"

white = "\033[37;1m"

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

print(random.choice(list) + "  AutoNet has started")

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
	print(random.choice(list) + "                                         888888" + red + "                                v2.0")
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
	print(random.choice(list) + "                                     Instagram: inc0gnit0.offical")
	time.sleep(0.1)
	print("\033[0m")



# Main #

def main():

	# Check if root #

	if os.geteuid() != 0:

		print("  Please run as root!")

		exit(0)

	banner()

	# Variables #

	print("\n")

	range = input(random.choice(list) + "                              range of IP adress(ex: 192.168.0.0/8): ")

	print("\n")

	passive = input(random.choice(list) + "                   do you want to sniff only(passive mode) [no/yes]: ")

	print("\n")

	interface = input(random.choice(list) + "                          what interface do you want to use(ex: wlan0): ")

	print("\n")

	fs = input(random.choice(list) + "                  do you want to enable fast scan(only scans .1, .100, .254) [no/yes]: ")

	# Checks #

	range1 = " -r " + range

	interface1 = " -i " + interface

	if passive in "yes":

		passive1 = " -p"

	if passive in "no":

		passive1 = ""

	if fs in "yes":

		fs1 = "-f"

	if fs in "no":

		fs1 = ""



	os.system("netdiscover" + interface1 + range1 + passive1 + fs1)



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
