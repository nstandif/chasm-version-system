import os
import os.path
from node import Node
from subNode import SubNode

class RootNode(Node):
	"""
	Concrete. Inherits from Node. Represents the root Project Folder.
	Folder contains at least: "assets","globals","sequences"
	
	@author: Morgan Strong
	"""
	
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Define Functions	
	def checkIntegrity(self):
		print "Checking RootNode integrity..."
		return True

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Initialize Node	
	#Constructor
	def __init__(self, path):
		super(RootNode, self).__init__(path)
		self._loadChildren()
		self.checkIntegrity()
		