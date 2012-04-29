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
		#RootNode has no restrictions on its children.
		#Recommended folders are assets, sequences, and global.
		return True

	def getErrorList(self):
		return errorList

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Initialize Node	
	#Constructor
	def __init__(self, path):
		super(RootNode, self).__init__(path)
		errorList = self._loadChildren()
		self.checkIntegrity()
		
		if errorList:
			print "\nErrors occurred while loading:"
			for x in errorList:
				print x
