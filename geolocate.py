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

    country_name = response.text.split(';')[3]

    if country_name == 'Reserved':
        sys.stderr.write('Could not retrieve any geolocation for IP {} - it looks like a private address\n'.format(ip))
        return False

    country_code = response.text.split(';')[1]

    return {
        'country_name': country_name, 
        'country_code': country_code
    }


ip_list = read_ip_list()
for ip in ip_list:
    result = get_ip_country(ip)
    if result:
        print("{},{},{}".format(ip, result['country_code'], result['country_name']))
