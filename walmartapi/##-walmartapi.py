#!/usr/bin/env python3
import urllib.request
import json
#import webbrowser
import time

## Define Walmart A 
walmarturl = 'http://api.walmartlabs.com/v1/items?'
mykey = 'apiKey=d7hjdvye4sky5cdwmmmtf3bf'    ## your key goes in place of DEMO_KEY

#upc = input('\n Please Enter UPC Code: ')
upc = '190198511270'
upckey = "&upc=" + upc

print("Walmart Query URL is:", walmarturl, mykey, upckey)

## Call the webservice
walmarturlobj = urllib.request.urlopen(walmarturl + mykey + upckey)

## read the file-like object
walmartread = walmarturlobj.read()

## decode json to python data structure
decodewalmart = json.loads(walmartread.decode('utf-8'))

## display our pythonic data
print("\n\nConverted python data")
print(decodewalmart)

print("\n Walmart Price on", time.ctime(), ": $" + str(decodewalmart['items'][0]['salePrice']))


