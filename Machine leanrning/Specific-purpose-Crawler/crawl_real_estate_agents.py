
"""https://www.trulia.com/directory/Boston-agent--6578/"""
from bs4 import BeautifulSoup
import threading
import urllib2
from HelperrClasses import *

class gatherRealEstateAgents(object):
	
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
		return respose

	def crawlYourSelf(self):
		url = "https://www.trulia.com/directory/Boston-agent--6578/"
		respose = openUrl(url)
		if respose != True:
			try:
				
			for no in xrange(2,250):
				url = url +  str(no) + "_p"

	def addNewAgent(self, response):
		soup = BeautifulSoup(response, "html.parser")
		for element in soup.find("div" attrs={'id'='findAnAgentContainer'}):
						

