#!/usr/bin/env python

import requests
import sys

if len(sys.argv) < 2:
	sys.stderr.write('Usage: python geolocate.py ip_file\n')
	sys.stderr.write('ip_file should be a file containing one IP per line\n')
	exit(1)

def read_ip_list():
	ip_file = sys.argv[1]

	try:
		with open(ip_file) as file:
			return file.read().splitlines()
	except IOError:
		sys.stderr.write('Unable to open IP file {}\n'.format(ip_file))
		exit(1)

def get_ip_country(ip):
	response = requests.get('http://ip2c.org/{}'.format(ip));
	if response.status_code != 200:
		sys.stderr.write('Could not retrieve any geolocation info for IP {} - skipping.\n'.format(ip))
		return False

	country = response.text.split(';')[3]

	if country == 'Reserved':
		sys.stderr.write('Could not retrieve any geolocation for IP {} - it looks like a private address\n'.format(ip))
		return False

	return country


ip_list = read_ip_list()
for ip in ip_list:
	country = get_ip_country(ip)
	if country:
		print("{},{}".format(ip, country))
