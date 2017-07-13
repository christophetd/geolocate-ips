# IP geolocation script

This repository contains a small script that you can use when you need to geolocate a bunch of IP addresses. It uses the [IP2C](http://about.ip2c.org/) API, which is free and doesn't require any registration or API key.

It takes a file containing a list of IPs as an input, and outputs a CSV friendly format.

**Input file format**: a file containing one IPv4 address per line, in dotted notation (e.g. 8.8.8.8)

**Output file format**: IP, ISO2 country code, Country name

**Usage**:

``` 
python geolocate.py ip_file > geolocalized_ips
```

**Sample result:**

```
216.58.205.3,US,United States
128.178.50.12,CH,Switzerland
185.75.143.24,FR,France
104.16.109.41,US,United States
```
