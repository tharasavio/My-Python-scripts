import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#view-source:http://py4e-data.dr-chuck.net/comments_42.html
#<tr><td>Romina</td><td><span class="comments">97</span></td></tr>

# Retrieve all of the anchor tags
tags = soup('span')
sum=0
for tag in tags:
    #print(tag.get('comments', None))
    #print('Attrs:', tag.attrs)
    #print(tag.get('text', None))
    sum=sum+int(tag.text)
    #print (tag.text)
print (sum)
    
