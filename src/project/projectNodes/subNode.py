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
	
	def _loadChildren(self):
		print "Loading SubNode Children..."
		
		for x in os.listdir(self._fullPath):
			path = self._fullPath + "/" + x
			if os.path.isdir(path):
				if not os.path.exists(path + "/.dirInfo"):
					self.addChild(SubNode(path))
		

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Initialize Node	
	#Constructor
	def __init__(self, path):
		super(SubNode, self).__init__(path)
		self._loadChildren()
		self.checkIntegrity()
		