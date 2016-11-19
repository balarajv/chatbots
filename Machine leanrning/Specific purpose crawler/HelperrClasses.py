class AgentDetails(object):

	def __init__(self, name, details, phone_no, location, houses_sold, ratings,  active_listings, url):
		
		self.name = name
		self.details = details
		self.phone_no = phone_no
		self.location = location
		self.houses_sold = houses_sold
		self.ratings = ratings
		self.active_listings = active_listings
		self.url = url

	def __str__(self):
		print "name :"+self.name,
		print " details :"+self.details
		print " phone_no :"+self.phone_no
		print " location :"+self.location
		print " houses sold :"+self.houses_sold
		print " ratings :"+self.ratings
		print " active_listings :"+self.active_listings
		print " url "+self.url

class OpenHouseDetails(object):
	pass

class mortgageAgentDetails(object):
	pass
