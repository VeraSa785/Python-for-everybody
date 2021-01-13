#Calling a JSON API
#In this assignment you will write a Python program
#The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data,
#and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.
#To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:
#http://py4e-data.dr-chuck.net/json?
#This API uses the same parameter (address) as the Google API. This API also has no rate limit so you can test as often as you like.
#To call the API, you need to include a key= parameter and provide the address that you are requesting as the address= parameter 
#that is properly URL encoded using the urllib.parse.urlencode() function.
#You can test to see if your program is working with a location of "South Federal University" which will have a place_id of "ChIJy0Uc1Zmym4gR3fmAYmWNuac".
#Please run your program to find the place_id for this location: Dnipropetrovsk National University
#Make sure to enter the name and case exactly as above and enter the place_id and your Python code below. Hint: The first seven characters of the place_id 
#are "ChIJg7q ..."
#Make sure to retreive the data from the URL specified above and not the normal Google API. Your program should work with the Google API - but the place_id 
#may not match for this assignment.

import urllib.request, urllib.parse, urllib.error
import json
import ssl

serviceurl = 'http://py4e-data.dr-chuck.net/json?'
api_key = 42

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
#address = 'South Federal University'

parameters = dict()
parameters['address'] = address
parameters['key'] = api_key

url = serviceurl + urllib.parse.urlencode(parameters)
print('Retrieving', url)

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

js = json.loads(data)
print(json.dumps(js, indent=4))

id = js['results'][0]['place_id']
print('Place id', id)
