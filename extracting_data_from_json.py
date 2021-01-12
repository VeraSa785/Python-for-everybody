# Extracting Data from JSON

# In this assignment you will write a Python program.
# The program will prompt for a URL, read the JSON data from that URL
# using urllib and then parse and extract the comment counts from the
# JSON data, compute the sum of the numbers in the file.

# We provide two files for this assignment.
# One is a sample file where we give you the sum for your testing and the other
# is the actual data you need to process for the assignment.

# Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1100424.json (Sum ends with 79)

import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
#url = 'http://py4e-data.dr-chuck.net/comments_42.json'
#url = 'http://py4e-data.dr-chuck.net/comments_1100424.json'
fhand = urllib.request.urlopen(url, context=ctx)
print('Enter location:', url)
print('Retrieving:', url)

data = fhand.read().decode()
print('Retrieved:', len(data), 'characters')

info = json.loads(data)
print ('Count:', len (info['comments']))

sum_comment = 0
x=0
for count in info['comments']:
    count = int(info['comments'][x]['count'])
    sum_comment = sum_comment + count
    x = x+1
print('Sum:', sum_comment)
