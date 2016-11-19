from elasticsearch import Elasticsearch

class ElasticSearchHelper(object):
<<<<<<< HEAD
	
=======
	def __init__ (self, indexname = None, docType = None):
		self.indexname = indexname
		self.docType = docType

		self.instance  =  Elasticsearch()
		
>>>>>>> chatbots/master
