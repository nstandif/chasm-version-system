import os
import os.path
import node
from node import Node

#TODO should this inherit from versionedNode instead?  It has a .nodeInfo file associated with it

class ShotNode(Node):
	"""
	Concrete. Inherits from Node. Representative of a project shot folder.
	
	@author: Morgan Strong
	"""
	
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Define Functions	
	def checkIntegrity(self):		
		children = os.listdir(self._fullPath)
		validChildren = ["animation", "fx", "charfx", "lighting", "compositing", "custom"]
		
		toRemove = []
		for x in children:
			if x in validChildren:
				toRemove.append(x)
			elif not os.path.isdir(os.path.join(self._fullPath, x)):
				toRemove.append(x)
		for x in toRemove:
			children.remove(x)
		
		if children:
			raise Exception("Shot: " + self._name + " contains invalid folders. \
Valid folders are: animation, fx, charfx, lighting, compositing, and custom.")
		
		return True

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Initialize Node	
	#Constructor
	def __init__(self, path, dirInfoFileName, errorList):
		super(ShotNode, self).__init__(path)
		self.checkIntegrity()
		errorList.extend(self._loadChildren())

"""
Methods not bound to an instance of the class:
"""
def createOnDisk(path, name):
	#TODO .nodeInfo ???
	node.createOnDisk(path, name)