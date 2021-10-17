
# Author: Muhammad F. Khan
# Date: November 11, 2020
# Description: Lookup a list of ip addresses using ip-api.com and output the result in json

'''
=== How to run? ===
$ ./bulk_ip_lookup.py ips_to_lookup.csv

=== ips_to_lookup.csv ===
192.168.2.1
192.168.2.2
192.168.2.3
127.0.0.1
'''

import os
import sys
import json
import time
import requests

# 45 lookup requests per second
SLEEP_TIMER = 2 # Wait 2 seconds to prevent rate limiting

# Looking up IP
def lookup_ip(ip):
    time.sleep(SLEEP_TIMER)
    print(f"Looking up ip: {ip}")
    url = f"http://ip-api.com/json/{ip}"
    res = requests.get(url) # paring the response to json
    try:
        return res.json()
    except Exception as e:
        if res.status_code == 429:
            print("Rate Limit Enforced, waiting 5 seconds before continuing")
            time.sleep(5)
            return lookup_ip(ip) # recursive call to function to complete lookup
        else:
            print(e)
            return {"error": e, "response": res.text()}


# Driver Code
if __name__ == "__main__":
    print("=== Bulk IP Lookup ===")

    # Checking Args
    if len(sys.argv) != 2:
        print("ERROR: No Input file provided!")
        print("Help: " + sys.argv[0] + " /path/to/ip.csv")
        sys.exit(1)

    # Checking if lookup file exists
    if os.path.isfile(sys.argv[1]):
        # Read ips to array
        with open(sys.argv[1], "r") as f:
            lookups = {}
            ips = f.read().strip().split(',\n')

            print(f"It will take roughly {SLEEP_TIMER * len(ips)} seconds to complete lookup for {len(ips)} ip")
            
            for ip in ips:
                lookups[ip] = lookup_ip(ip)
            
            with open("output.json", "w") as ff:
                json.dump(lookups, ff)
                print("Done writing lookups to output.json")


    else: # file not found
        print("ERROR: File does not exists at " + sys.argv[1])
        sys.exit(1)


# EOF
