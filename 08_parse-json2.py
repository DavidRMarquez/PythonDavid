# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 18:14:10 2020

@author: CEC
"""

"""

import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Quito"
dest = "Bogotá"
key = "aZJToBi37X6PoQVbEbhnpAOHIEHv6UiR"

url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})

json_data = requests.get(url).json()
#print(json_data)

json_status=json_data["info"]["statuscode"]

if json_status==0:
    print("API Status: " +str(json_status) + " = A successful route call.\n")

"""
import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Quito"
dest = "Guayaquil"
key = "aZJToBi37X6PoQVbEbhnpAOHIEHv6UiR"
url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
print("URL: " + (url))

json_data = requests.get(url).json()
jsonstatus = json_data["info"]["statuscode"]

if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")