# to use: python3 CountMinSketchTester.py <data.dat> 


import sys
import countMinSketch

class countMinSketchTester():

	def __init__(self):
		self.data = list()
		self.filter = countMinSketch.countMinSketch()
		self.goodDataLen = 0

	def load(self, filename):
		with open(filename) as infile:
			line = infile.readline()
			line = line.replace("\n","")
			while (line):
				self.data.append(line)
				line = infile.readline()
				line = line.replace("\n","").replace("\r","")
		self.goodDataLen = len(self.data)

	def train(self):
		lineCount = 0
		print("Evaluating {0} lines\n".format(self.goodDataLen))
		for item in self.data:
			lineCount += 1
			self.filter.increment(item)
			if lineCount % round(self.goodDataLen*0.25) == 0:
				print("{0}%".format(round((lineCount/self.goodDataLen)*100)))



	def count(self, query, verbose = True):

		result = self.filter.count(query)
		if (verbose):
			print("Query '{0}' appeared no more than {1} time(s).".format(query, result))
		return(result)


# run
tester = countMinSketchTester()
tester.load(sys.argv[1])
tester.train()
tester.count("cytendulrmmkgt_1")
tester.count("swhvjljiqnrlsmtnsejvqhcr_32")
tester.count("gjigqvhwyfwgobmmsxbybirmldfuxuujdqgsqqizugcodfznfljki_23") # data3
tester.count("guimpsssgusjdkebvdocgcvzoxyfrrmlztqxjxvlosgpjygup_32") #data5_CMS.dta

