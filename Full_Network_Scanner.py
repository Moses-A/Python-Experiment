#!/usr/bin/env python2
# -*- coding: utf-8 -*- 
# written by Moses Arocha

from __future__ import unicode_literals
import optparse
import socket
import os
import sys


def ProgramInstaller():
    os.system("sudo apt-get install nmap && sudo apt-get install tshark")

def TShark():
    os.system("sudo tshark -i any >> NetworkMonitor.txt")
	
def FinPortScanner(TargetHost):
    OSD = os.system("sudo nmap -sF "+TargetHost+" >> NetworkScan.txt")

def TTLScan(TargetHost):
    Decoy = raw_input(" What Is The Decoy IP Address? : ")
    OSD = os.system("sudo nmap "+TargetHost+" -D "+Decoy+" -ttl 13 >> NetworkScan.txt")
	
def SpecificFinPortScanner(TargetHost, TargetPort):
    OSD = os.system("sudo nmap -sF -p"+TargetPort+ " " +TargetHost+" >> NetworkScan.txt")

def SpecificACKScan(TargetHost, TargetPort):
    OSD = os.system("sudo nmap -sA -p"+TargetPort+ " " +TargetHost+" >> NetworkScan.txt")

def ACKScan(TargetHost):
    OSD = os.system("sudo nmap -sA "+TargetHost+" >> NetworkScan.txt")

def FragmentedIP(TargetHost):
    OSD = os.system("sudo nmap -ff "+TargetHost+" >> NetworkScan.txt")
	
def OSScanner(TargetHost):
    OSD = os.system("sudo nmap -O "+TargetHost+" >> NetworkScan.txt")
	
def MacSpoof(TargetHost):
    OSD = os.system("sudo nmap -spoof-mac Cisco "+TargetHost+" >> NetworkScan.txt")

def WebServer(TargetHost):
    OSD = os.system("sudo nmap -sV -script=http-enum" +TargetHost+" >> NetworkScan.txt")

def SambaServer(TargetHost):
    OSD = os.system(" sudo nmap –script=samba-vuln-cve-2012-1182 -p139 "+TargetHost+" >> NetworkScan.txt")

def SMTPServer(TargetHost):
    OSD = os.system("sudo nmap -sV –script=smtp-strangeport "+TargetHost+ " >> NetworkScan.txt")

def PHPVersion(TargetHost):
    OSD = os.system("sudo nmap -sV –script=http-php-version "+TargetHost+" >> NetworkScan.txt")

def DNSBlackList(TargetHost):
    OSD = os.system("sudo nmap -sn "+TargetHost+" -script dns-blacklist >> NetworkScan.txt")

def HostPing(TargetHost):
    OSD = os.system("sudo nmap -sn "+TargetHost+" >> NetworkScan.txt")

def NetworkPing():
    UserInput = raw_input("\n EX: 192.168.0.* \n Please Insert The Network ID: ")
    OSD = os.system("sudo nmap -sn -sP "+UserInput+" >> NetworkScan.txt")

def PortScan(TargetHost,TargetPort):
    OSD = os.system("sudo nmap -p "+TargetPort+" -sV -sS -T4 "+TargetHost+" >> NetworkScan.txt")	

def NetBios(TargetHost):
    OSD = os.system("sudo nmap -sV -p 139,445 "+TargetHost+" >> NetworkScan.txt")
    User = raw_input(" Do You Want To Continue? [Y/N] ")
    if User == "Y" or User == "y":
        display = os.system("sudo nmap -sU --script nbstat.nse -p 137 "+TargetHost+" >> NetworkScan.txt")
	continuation = os.system("sudo nmap --script-args=unsafe=1 --script smb-check-vulns.nse -p 445 "+TargetHost+" >> NetworkScan.txt")
    else:
	print " Information has been outputed to a textfile."

def CheckHTTPServer(TargetHost):
    OSD = os.system("sudo nmap -oG -p80,443 "+TargetHost+" >> NetworkScan.txt")

def UDPScan(TargetHost,TargetPort):
    OSD = os.system("sudo nmap -p"+TargetPort+" "+TargetHost+" >> NetworkScan.txt")
	
def SCTPScan(TargetHost):
    OSD = os.system("sudo nmap -sY "+TargetHost+" >> NetworkScan.txt")

def AdvSCTPScan(TargetHost):
    OSD = os.system("sudo nmap -sZ "+TargetHost+" >> NetworkScan.txt")

def ZombieAttack(TargetHost,TargetPort):
    mask = raw_input(" What IP Do You Want To Mask Yourself As? ")
    OSD = os.system("sudo nmap -Pn -p"+TargetPort+" -sI "+mask+" "+TargetHost+" >> NetworkScan.txt")

def SpoofAddress(TargetHost):
    OSD = os.system("sudo nmap -S "+TargetHost+" >> NetworkScan.txt") 

def Organizer(TargetHost):
    repeat = 0

    while (repeat == 0):
        os.system('clear')
	print "\n\n Below Are The Tasks You Can Commense. Only Do If You Have Permissions! "
	print "\n\t [0] Exit. \n\t [1] Fin Port Scan \n\t [2] Acknowlegement Port Scan \n\t [3] Send Fragmented IP's \n\t [4] OS Scanner \n\t [5] Mac Spoofing \n\t [6] Analyze Samba Server \n\t [7] Analyze SMTP Server \n\t [8] Check PHP Version \n\t [9] Check DNS Black List \n\t [10] Ping Host \n\t [11] Spoof Address \n\t [12] Analyze NetBios \n\t [13] Check HTTP Server Vuln. \n\t [14] SCTP Scan \n\t [15] Adv SCTP Scan \n\t [16] Network Ping \n\t [17] Decoy Scan Using TTL"
	choice = int(raw_input("\n\t What Is The First Thing You Would Like To Do?  : "))
	
	if choice == 0:
	    repeat = 1
	elif choice == 1:
	    FinPortScanner(TargetHost)
	elif choice == 2:
	    ACKScan(TargetHost)
	elif choice == 3:
	    FragmentedIP(TargetHost)
	elif choice == 4:
	    OSScanner(TargetHost)
	elif choice == 5:
	    MacSpoof(TargetHost)
	elif choice == 6:
	    SambaServer(TargetHost)
	elif choice == 7:
	    SMTPServer(TargetHost)
	elif choice == 8:
	    PHPVersion(TargetHost) 
	elif choice == 9:
	    DNSBlackList(TargetHost)
	elif choice == 10:
	    HostPing(TargetHost)
	elif choice == 11:
	    SpoofAddress(TargetHost)
	elif choice == 12:
	    NetBios(TargetHost)
	elif choice == 13:
	    CheckHTTPServer(TargetHost)
	elif choice == 14:
	    SCTPScan(TargetHost)
	elif choice == 15:
            AdvSCTPScan(TargetHost)
	elif choice == 16:
	    NetworkPing()
	elif choice == 17:
	    TTLScan(TargetHost)
	else:
	    sys.exit('')
		
	
def main():
    extensions = optparse.OptionParser('Usage For Program: -H <Target Host> -P <Target Port>')
    extensions.add_option('-H', '--Host', dest='TargetHost', type='string', help='specify target host')
    extensions.add_option('-P', '--Port', dest='TargetPort', type='string', help='specify target port')
    (options, args) = extensions.parse_args()
    TargetHost = options.TargetHost
    TargetPorts = str(options.TargetPort).split(',')
    if (TargetHost == None) | (TargetPorts[0] == None):
        print extensions.usage
	exit(0)
    if not os.geteuid() == 0:
    	sys.exit('\tMust Be Root!')
    f = open('NetworkScan.txt', 'w')
    os.system('chmod 777 NetworkScan.txt')
    d = open('NetworkMonitor.txt', 'w')
    os.system('chmod 777 NetworkMonitor.txt')
    ProgramInstaller()
    TShark()
    Organizer(TargetHost)
    for TargetPort in TargetPorts:
        repeat = 0
	while (repeat == 0):
	    os.system('clear')
	    print "\n\t Below Are A List Of Port Scans. Choose Wisely! "
	    print "\n\t [0] Exit \n\t [1] TCP SYN Port Scan \n\t [2] UDP SYN Port Scan \n\t [3] Zombie Attack \n\t [4] Specific FIN Port Scan \n\t [5] Specific ACK Scan"
	    choice = int(raw_input("\n\t\t Please Enter A Number : "))

	    if choice == 0:
	        repeat = 1
	    elif choice == 1:
		PortScan(TargetHost, TargetPort)
	    elif choice == 2:
		UDPScan(TargetHost, TargetPort)
	    elif choice == 3:
		ZombieAttack(TargetHost, TargetPort)		
	    elif choice == 4:
		SpecificFinPortScanner(TargetHost, TargetPort)
	    elif choice == 5:
		SpecificACKScan(TargetHost, TargetPort)

if __name__ == '__main__':
    main()
