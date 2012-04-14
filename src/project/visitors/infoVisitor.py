import os.path
from visitor import Visitor

class InfoVisitor(Visitor):
	"""
	Concrete. Prints information about each node that is passed to it.
	
	@author: Morgan Strong
	"""

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Define Functions	
	def run(self, curNode):
		print "Name:", curNode.getName()
		print "Children:"
		for x in curNode.getChildren():
			print "\t" + x.getName()
		print "-----"

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Initialize Visitor	
	#Constructor
	def __init__(self):
		pass