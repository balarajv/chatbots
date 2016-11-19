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

members = soup.find("ul", {"class", "listBorderedHover mvn"})
members_list = members.findAll("li")


for member in members_list:	

	url = member.find("a", {"class", "mediaImg frameThumb"})[1]['href']
	name = member.find("a", {"class", "mediaImg frameThumb"})[1].string
	details = member.find("p", {"class", "mvn h7"})[0].string
	phone_number = member.find("p", {"class", "mvn h7"})[0].string
	rating  = member.find("div", {"class", "narrowIcon"})[0]['title']
	no_rating = member.find("span", {"class", "reviewCount"})[0].string
	location = member.find("div", "h7 typeLowlight mvn ptm")[0].string
	active_listings = member.find("div", "typeDeemphasize mvn")[0].string

	#def __init__(self, name, phone_no, location, houses_sold, ratings,  active_listings, url):
	x = AgentDetails(name, phone_no, location, houses_sold, rating+"/"+no_rating, active_listings, url)
	print x

	#print member
	#url = member.find("a", {"class", "mediaImg frameThumb"})[0]['href']

	#print member.first("img")["alt"]


