
"""https://www.trulia.com/directory/Boston-agent--6578/"""
from bs4 import BeautifulSoup
import threading
import urllib2
from HelperrClasses import *
import pickle
import time

class archiveRealEstateAgents(object):
	
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
						
	def scrapeAgentsPerPage(self, url):
		respose = self.openUrl(url)
		soup = BeautifulSoup(response, "html.parser")

		members = soup.find("ul", {"class", "listBorderedHover mvn"})
		members_list = members.findAll("li")

		index = 1
		agents = []
		for member in members_list:	
			
			url = member.find("a", {"class", "mediaImg frameThumb"})['href']
			name = member.find("h5", {"class","typeEmphasize ellipsis_overflow mvn agent_name_link pan man"}).find("a").string
			details = member.findAll("p", {"class": re.compile('mvn h7.*')})

			if len(details) == 1:
				phone_no = details[0].string
				detail = None
			if len(details) == 2:
				detail = details[0].string
				phone_no = details[1].string

			rating  = member.find("div", {"class", "narrowIcon"})['title']
			no_rating = member.find("span", {"class", "reviewCount"}).string
			location = member.find("div", {"class", "h7 typeLowlight mvn ptm"}).string
			houses_sold = member.find("div", {"class", "typeDeemphasize mvs"}).string
			active_listings = member.find("div", {"class", "typeDeemphasize mvn"}).string
			active_listings = "0"
			
			x = AgentDetails(name, detail, phone_no, location, houses_sold, 
				rating+"/"+no_rating, active_listings, url, index)
			agents.append(x)
		return agents

	def getAgents(self):
		url = "https://www.trulia.com/directory/Boston-agent--6578/"
		all_members = []
		members = self.scrapeAgentsFromUrl(url)
		all_members = all_members + members

		for page in xrange(2,250):
			#delaying so that they don't ban me
			time.sleep(5)
			url = url + str(page) + "_p" 
			members = self.scrapeAgentsFromUrl(url)
			all_members = all_members + members
		return all_members


if __name__ == '__main__':
	members = archiveRealEstateAgents()
	agents  = members.getAgents()
	with open("agents.pickle", "wb") as output_file:
		pickle.dump(agents, output_file)

	
			

