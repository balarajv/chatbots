from bs4 import BeautifulSoup
import urllib2
from HelperrClasses import *

def openUrl(url):
		try: 
			response =  urllib2.urlopen(url)

		except urllib2.HTTPError, e:
		    print 'HTTPError = ' + str(e.code),
		    print url
		    return True
		except urllib2.URLError, e:
		    print 'URLError = ' + str(e.reason),
		    print url
		    return True
		except Exception:
			print "Unknown Exception", 
			print url
			return True
		return response

url = "https://www.trulia.com/directory/Boston-agent--6578/"
response = openUrl(url)	

soup = BeautifulSoup(response, "html.parser")

output = soup.find("ul", {"class", "listBorderedHover mvn"}).li
print output
