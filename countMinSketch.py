
import mmh3
import numpy as np


class countMinSketch():
	"""
	The countMinSketch algorithm. Returns 
	"""

	def __init__(self):
		self.b = 10**5 # buckets
		self.l = 5 # Hash functions
		self.CMS = np.array([[0 for y in range(self.b)] for x in range(self.l)])

	# Setup Hash function
	def getHash(self, item, seed):
		return(mmh3.hash(item, seed, signed = True) % self.b)

	# Training operation
	def increment(self, item):
		for lHash in range(self.l):
			index = self.getHash(item, lHash)
			self.CMS[lHash][index] += 1

	# Return the frequency count of x, 
	def count(self, query):
		bins = []
		for lHash in range(self.l):
			index = self.getHash(query, lHash)
			bins.append(self.CMS[lHash][index])
		return(min(bins))

	# save sketch
	# load sketch



