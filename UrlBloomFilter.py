
import mmh3
import BitVector as bv

class UrlBloomFilter:
	# Setup useful variables in here
	def __init__(self):
		self.bitSize = 10**8
		self.filter = bv.BitVector(size=self.bitSize)

	# Called once for all good URLs
	def train(self, url):
		index = mmh3.hash(url) % self.bitSize
		self.filter[index] = 1
		
	# Should return true if the URL is good, otherwise false.
	def classify(self, url):
		index = mmh3.hash(url) % self.bitSize
		if self.filter[index] == 1:
			return True
		else:
			return False

		#return True