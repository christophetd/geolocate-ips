# IP geolocation script

This repository contains a small script that you can use when you need to geolocate a bunch of IP addresses. It uses the [IP2C](http://about.ip2c.org/) API, which is free and doesn't require any registration or API key.

It takes a file containing a list of IPs as an input, and outputs a CSV friendly format.

Usage: 

```
$ cat ip_file
216.58.205.3
128.178.50.12
185.75.143.24
104.16.109.41

$ python geolocate.py ip_file > geolocalized_ips

$ cat geolocalized_ips
216.58.205.3,United States
128.178.50.12,Switzerland
185.75.143.24,France
104.16.109.41,United States
```
