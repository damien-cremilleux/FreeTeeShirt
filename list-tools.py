import urllib2
import re

#Grab source code
url = 'http://www.umadbro.pw/pages/'
response = urllib2.urlopen(url)
html = response.read()
 
#Parse source code to find links
links = re.findall('href=[a-z\"A-Z0-9]+\"', html)

#Print out just the name of the commands
for cur_link in links:
    end_substr_len = (len(cur_link) - 1)
    print cur_link[6:end_substr_len]
