#!/usr/bin/env python2
#Author is Moses Arocha
# Created in Python, created with the help of TJ O'Connor "Violent Python"

import dpkt
import socket
import pygeoip
import optparse

gi = pygeoip.GeoIP('/opt/GeoIP/Geo.dat')		#Inclusion of Geo.dat database which allows for the location of all IP's

##Analyzes the IP's to discover the location of origination##
def retrieveGeographicSource(ip):					#The function which defines the geographic location of the IP's
   try:
	rec = gi.record_by_name(ip)
	city =  rec['city']				# The inclusion of the city based on the IP address
	if city != '':					
	   Location = city + ', ' + country		# The inclusion of the country based on the IP address 
	else:
	   Location = country				
	return Location
   except Exception, e:
	return 'Unfound'				# Catch all for IP's if not found in database, counted as unregistered

##Analyzes the Pcap file, organizes it, then prints out the Source and Destination, IP Address and location##
def AnalyzePcap(pcap):					# The function which creates packets and the interaction of the 
   for (ts, buf) in pcap:				# pcap file for network monitoring
       try:
	   eth = dpkt.ethernet.Ethernet(buf)
	   ip = eth.data
	   source = socket.inet_ntoa(ip.src)					# retrieves the source IP address
	   destination = socket.inet_ntoa(ip.dst)				# retrieves the destination IP address
	   print ' Source IP : ' + source + '--> Destination IP: ' + destination	# How it is printed within the file, with the IP, then geographical destination
	   print 'Source IP Location: ' + retrieveGeographicSource(source) + '--> Destination IP Location: ' + retrieveGeographicSource(destination)
       except:
	   pass

## The beginning of the main, grabs the user's input for which pcap file to analyze ##
def main():
   parser = optparse.OptionParser('Usages For Program: -r <pcap file>')	# The inclusiong of the optparse 
   parser.add_option('-r', '--Read', dest='pcapFile', type='string', help='specify pcap filename')
   (options, args) = parser.parse_args()
   if options.pcapFile == None:
	print parser.usage
	exit(0)
   if not os.geteuid() == 0:
    	sys.exit('Must Be Root!')				# Checks to see if a user is root
   pcapFile = options.pcapFile
   f = open(pcapFile)						# The opening of the pcapFile
   pcap = dpkt.pcap.Reader(f)					
   AnalyzePcap(pcap)						# references the AnalyzePcap function

if __name__ == '__main__':
	main()