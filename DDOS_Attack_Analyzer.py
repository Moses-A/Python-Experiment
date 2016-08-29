#!/usr/bin/env python2
# written by Moses Arocha
# Written with the help of TJ O'Connor in his book "Violent Python"

import dpkt
import socket
import optparse

THRESH = 1000

def DDOSAttack(pcap):				
    packetCount = {}					# Begins the packet Counting at null or zero
        for (ts, buf) in pcap:				# Grabs the PCAP file for network monitoring
            try:
                eth = dpkt.ethernet.Ethernet(buf)
                ip = eth.data
                source = socket.inet_ntoa(ip.src)	# Within the PCAP file grabs the source IP address
                destination = socket.inet_ntoa(ip.dst)	# Within the PCAP file grabs the destination IP address
                tcp = ip.data
                DestinationPort = tcp.DestinationPort	# Grabs the destination port from the TCP data anaylzed in the PCAP file
                if DestinationPort == 80 or DestinationPort == 443:	# If the Destination port is either 80 or 443 it continues
                    stream = source + ':' + destination
                    if packetCount.has_key(stream):			
                        packetCount[stream] = packetCount[stream] + 1
                    else:
    	                packetCount[stream] = 1
            except:
		pass

    for stream in packetCount:
        packetsSent = packetCount[stream]
        if packetsSent > THRESH:
            source = stream.split(':')[0]
            destination = stream.split(':')[1]
            print '[+] ' +source+ ' attacked '+destination+ 'with ' + str(packetsSent) + 'pkts.'	
            # The only output the user will see, only seen if an attack is occuring by the packets sent from an IP Address exceeds the thresh hold amount

# The main will examine the user's input, open up the pcap file, then will forward the information to the DDOSAttack function #
def main():
    parser = optparse.OptionParser("Usages For Program:  -p <pcap file> -t <thresh>")
    parser.add_option('-r', '--Read', dest ='pcapFile', type='string', help='specify pcap filename')
    parser.add_option('-T', '--Thresh', dest='thresh', type='int', help='specify threshold count')
    (options, args) = parser.parse_args()
    if options.pcapFile == None:
        print parser.usage					# The catch all function for the parser
        exit(0)			
    if parser.thresh != None:					# If the user doesn't enter in an interger for the thresh, it automatically defaults to the set global value of 1000
	THRESH = parser.thresh
    if not os.geteuid() == 0:
    	sys.exit('Must Be Root!')				# This code checks to see if a user is root
    pcapFile = parser.pcapFile
    f = open(pcapFile)					
    pcap = dpkt.pcap.Reader(f)					# Analyzes the pcap and sends the information along
    DDOSAttack(pcap)						# Calls for the DDOSAttack function

if __name__ == '__main__':
    main()
