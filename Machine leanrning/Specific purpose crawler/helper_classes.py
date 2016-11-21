class AgentDetails(object):

	def __init__(self, name = None, details = None, phone_no = None,]
	 location= None, houses_sold= None, ratings= None, 
	 active_listings= None, url= None, index = None):
		self.name = name
		self.details = details
		self.phone_no = phone_no		
		self.location = location
		self.houses_sold = houses_sold
		self.ratings = ratings
		self.active_listings = active_listings
		self.url = url
		self.index =  index

		if self.name == None:
			self.name = ""
		if self.details == None:
			self.details = ""
		if self.phone_no == None:
			self.phone_no = ""
		if self.location == None:
			self.location = ""
		if self.houses_sold == None:
			self.houses_sold = ""
		if self.ratings == None:
			self.ratings = ""
		if self.active_listings == None:
			self.active_listings = ""
		if self.url == None:
			self.url = ""

	def __str__(self):
		return ("name :"+self.name +
		" details :"+self.details +
		" phone_no :"+self.phone_no +
		" location :"+self.location +
		" houses sold :"+self.houses_sold +
		" ratings :"+self.ratings +
		" active_listings :"+self.active_listings +
		" url "+self.url)

class OpenHouseDetails(object):
	def __init__(self ):
		pass

class MAgentDetails(object):
	def __init__(self, agent_name = None, company_name = None, 
		agent_url = None, compnay_url = None, 
		agent_rating = None, agent_review_count = None, 
		agent_image = None):
		self.agent_name = agent_name
		self.compnay_url = compnay_url
		self.company_name = company_name
		self.agent_url = agent_url
		self.agent_image = agent_image
		self.agent_rating = agent_rating
		self.agent_review_count = agent_review_count

		if self.agent_name == None:
			self.agent_name = ""
		if self.company_name == None:
			self.company_name = ""
		if self.compnay_url == None:
			self.compnay_url = ""
		if self.agent_rating == None:
			self.agent_rating = ""
		if self.agent_review_count == None:
			self.agent_review_count = ""
		if self.agent_url == None:
			self.agent_url = ""
		if self.agent_image ==  None:
			self.agent_image = ""


