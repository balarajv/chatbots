from elasticsearch import Elasticsearch

class ElasticSearchHelper(object):
	def __init__ (self, indexname = None, docType = None):
		self.indexname = indexname
		self.docType = docType

		self.instance  =  Elasticsearch()
		