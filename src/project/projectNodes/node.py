import os.path

class Node(object):
	"""
	ABSTRACT. Representative of a project folder. It contains its name, a
	reference to a parent, a list of children, and common methods needed for
	other node types.
	
	@author: Morgan Strong
	"""

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Define Functions	
	def checkIntegrity(self):
		raise NotImplementedError
	
	def getName(self):
		return self._name
	
	def getParent(self):
		return self._parent
	
	def setParentNone(self):
		self._parent = None
	
	def addChild(self, child):
		if not isInstance(child, Node):
			raise Exception("Cannot add non-Node object to list of node's children.")
		self._children.append(child)
	
	def removeChild(self, notChild):
		if not isInstance(child, Node):
			raise Exception("Cannot remove non-Node object from list of node's children.")
		self._children.remove(notChild)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Initialize Node	
		#Constructor
	def __init__(self, path):
		if not os.path.exists(path):
			raise Exception("The path does not exist:",path)
			
		self._fullPath = path
		self._name = path.split('/')[-1]
		self._parent = path.split('/')[-2]
		self._children = []