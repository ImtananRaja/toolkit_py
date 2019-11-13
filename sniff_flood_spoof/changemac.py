#!/usr/bin/python

# allows us to execute system commands and get the results
import subprocess

def change_mac_address(interface, new_mac):
    # shut the interface down
    subprocess.call(["ifconfig",  interface, "down"])
    # change the interface mac address
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    # start the interface again
    subprocess.call(["ifconfig", interface, "up"])


def main():
    # get the interface to change mac address on e.g. eth0 or wlan0 or lo
    interface = str(input("Please enter the interface you'd like to change the mac address on: "))
    # get the new mac address the user wants
    new_mac_add = str(input("What is the new mac address you would like: "))

    # get the current details for the interface
    #mac_before = subprocess.check_output(["ifconfig", interface])
    mac_before2 = subprocess.check_output(["cat", "/sys/class/net/{}/address".format(interface)])
    change_mac_address(interface, new_mac_add)
    #mac_after = subprocess.check_output(["ifconfig", interface])
    mac_after2 = subprocess.check_output(["cat", "/sys/class/net/{}/address".format(interface)])
    print(str(mac_after2))

    if mac_before2 == mac_after2:
        print("Failed to change mac address to: " + new_mac_add)
    else:
        print("mac address changed to: " + new_mac_add + " on " + interface)

if __name__ == '__main__':
    main()
