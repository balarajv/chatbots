from bs4 import BeautifulSoup
import urllib2
from HelperrClasses import *
import sys
reload(sys)
import re
sys.setdefaultencoding('utf-8')

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

def scrapeAgents(self, response):
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
		
		agent_info = AgentDetails(name, detail, phone_no, location, houses_sold, 
			rating+"/"+no_rating, active_listings, url, index)
		agents.append(agent_info)
	return agents
		
def scrapeMAgents(self, response):
	soup = BeautifulSoup(response, "html.parser")

	agents = soup.find_all("div", {"class", "ld-lender-card ld-lender-card_bank"})
	for agent in agents:
		agent_image_helper = agent.find("zsg-lg-1-4 ld-lender-image-column").first("a").first("div")["style"]
		agent_image_url = re.search(r'url\(\"(.*?)\"\);', agent_image_helper).group(1)
		company_details = agent.find("div", {"class", "ld-lender-info-column"}).find("h5")
		agent_company = company_details.find("a").string
		company_url = company_details.find("a")["href"]
		agent_details = agent.find("div", {"class","ld-lender-info-column"}).find("h2")
		agent_name = agent.details.find("a").string
		agent_url = agent_details.find("a")["href"]
		agent_reviews = agent.find("div", {"class", "zsg-md-hide zsg-sm-hide ld-lender-review-column"})
		agent_rating = int(agent_reviews.find("h2").find("span")["class"][-3:])/100
		agent_review_count = agent_reviews.string
		
		





