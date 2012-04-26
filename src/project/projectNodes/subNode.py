import os
import os.path
import node

class SubNode(node.Node):
	"""
	ABSTRACT. Inherits from Node. Representative of a project category folder.
	
	@author: Morgan Strong
	"""
	
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Define Functions	
	def checkIntegrity(self):
		#SubNode has no restrictions on its children.
		return True

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Initialize Node	
	#Constructor
	def __init__(self, path, errorList):
		super(SubNode, self).__init__(path)
		errorList.extend(self._loadChildren())
		self.checkIntegrity()


"""
Methods not bound to an instance of the class:
"""
def createOnDisk(path, name):
	node.createOnDisk(path, name)