# Extracting Data from XML

# In this assignment you will write a Python program.
# The program will prompt for a URL, read the XML data from that URL
# using urllib and then parse and extract the comment counts from the
# XML data, compute the sum of the numbers in the file.

# We provide two files for this assignment.
# One is a sample file where we give you the sum for your testing and the other
# is the actual data you need to process for the assignment.

# Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1100423.xml (Sum ends with 83)


import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
#url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
#url = 'http://py4e-data.dr-chuck.net/comments_1100423.xml'
fhand = urllib.request.urlopen(url, context=ctx)
print('Enter location:', url)
print('Retrieving:', url)

data = fhand.read().decode('utf8')
print('Retrieved:', len(data), 'characters')

tree = ET.fromstring(data)
comments = tree.find('comments').findall('comment')
print ('Count:', len (comments))

sum_comment = 0
for comment in comments:
    count = int(comment.find('count').text)
    sum_comment = sum_comment + count
print('Sum:', sum_comment)
