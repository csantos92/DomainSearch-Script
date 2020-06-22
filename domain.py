#!/usr/bin/python3
"""
Created on Mon Jun 22 19:25:05 2020

Script that tells you if a web domain is available to buy or not
You can insert one or more domains at once as arguments

Examples: 

./domain.py example.com 
./domain.py example1.com example2.org example3.net

@author: csantos92
"""
from requests import get, exceptions
import sys

def check_domain(site):
    try:
        get("http://" + site, timeout = 3)
        http = True
    except exceptions.ConnectionError:
        http = False

    try:
        get("https://" + site, timeout = 3)
        https = True
    except exceptions.ConnectionError:
        https = False

    if http or https:
        print("Domain '" + site + "' not available :(")
    else:
        print("Domain '" + site + "' available :)")

for url in range(len(sys.argv) - 1):
    check_domain(sys.argv[url + 1])
