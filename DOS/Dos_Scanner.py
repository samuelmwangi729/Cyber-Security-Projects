#!/usr/bin/python
from scapy.all import *

class Detector():
    def __init__(self):
        self.Banner()
        print("\nTHE DOS SCANNER WILL SCAN FOR  ABNORMAL TRAFFIC \n BASED ON THE NETWORK INTERFACE SELECTED")
        self.Banner()
    def Banner(self):
        for i in range(0,50):
            print("=",end="")
    def get_Interface(self,interface=None):
        if interface is None or not interface:
            #select the default wlan0
            Interface = "wlan0"
        else:
            Interface = interface
        return Interface
    def deauth_packet_handler(self,pkt):
        if pkt.haslayer(Dot11Deauth):
            print("Deauthentication packet detected")
        print("Deauth Packet monitoring on")
if __name__ == "__main__":
    detector = Detector()
    print("\n[+]Please select an Interface to monitor.\n\n[!!]Default wlan0? Press enter to continue...\n")
    interface = str(input())
    sniff(iface=detector.get_Interface(interface), prn=detector.deauth_packet_handler, store=0)