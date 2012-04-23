import os
import os.path
from node import Node

class SubNode(Node):
	"""
	ABSTRACT. Inherits from Node. Representative of a project category folder.
	
	@author: Morgan Strong
	"""
	
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Define Functions	
	def checkIntegrity(self):
		print "Checking SubNode integrity..."
		return True

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Initialize Node	
	#Constructor
	def __init__(self, path, errorList):
		super(SubNode, self).__init__(path)
		errorList.extend(self._loadChildren())
		self.checkIntegrity()
		