# -*- coding: utf-8 -*-
import argparse
import sys

parser = argparse.ArgumentParser(description='A simple python script to convert Exchange Receive Connector IP Lists to F5 External Data Group Lists.')
parser.add_argument("-i","--in",help="input file")
parser.add_argument("-o","--out",help="output file")
args = parser.parse_args()

def ipRange(start_ip, end_ip):
	start = list(map(int, start_ip.split(".")))
	end = list(map(int, end_ip.split(".")))
	temp = start
	ip_range = []

	ip_range.append(start_ip)
	while temp != end:
		start[3] += 1
		for i in (3, 2, 1):
 			if temp[i] == 256:
				temp[i] = 0
				temp[i-1] += 1
		ip_range.append(".".join(map(str, temp)))

	return ip_range

infile = open(sys.argv[2], 'r+')
outfile = open(sys.argv[4], 'a')
for line in infile:
	if "SingleAddress" in line:
		first,second,third,fourth = line.split(';')
		outfile.write("host " + first + ",\n")
	elif "LoHi" in line:
		first,second,third,fourth = line.split(';')
		ip_range = ipRange(first, second)
		for ip in ip_range:
			outfile.write("host " + ip + ",\n")
	else:
		continue
infile.close()
outfile.close()