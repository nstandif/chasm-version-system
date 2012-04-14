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
	
	def _loadChildren(self):
		print "Loading Children..."
		
		# If written correctly, this function could be defined in Node.
		# .dirInfo should contain information about the type of folder that
		# contains it.
		for x in os.listdir(self._fullPath):
			path = self._fullPath + "/" + x
			if os.path.isdir(path):
				if not os.path.exists(path + "/.dirInfo"):
					self.addChild(SubNode(path))
	
	def getName(self):
		return self._name
	
	def getParent(self):
		return self._parent
	
	def setParentNone(self):
		self._parent = None
	
	def addChild(self, child):
		if not isinstance(child, Node):
			raise Exception("Cannot add non-Node object to list of node's children.")
		self._children.append(child)
	
	def removeChild(self, notChild):
		if not isinstance(child, Node):
			raise Exception("Cannot remove non-Node object from list of node's children.")
		self._children.remove(notChild)
	
	def getChildren(self):
		return self._children
	
	def preVisit(self, visitor):
		if not isinstance(visitor, Visitor):
			raise Exception("Nodes can only be traversed by a Visitor object")
		visitor.run(self)
		for x in self._children:
			x.preVisit(visitor)
	
	def postVisit(self, visitor):
		if not isinstance(visitor, Visitor):
			raise Exception("Nodes can only be traversed by a Visitor object")
		for x in self._children:
			x.postVisit(visitor)
		visitor.run(self)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Initialize Node	
		#Constructor
	def __init__(self, path):
		if not os.path.exists(path):
			raise Exception("The path does not exist:",path)
			
		self._fullPath = path
		self._name = path.split('/')[-1]
		self._parent = path.split('/')[-2]
		self._children = []

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Prevent Cyclic Dependencies
from subNode import SubNode
from ..visitors.visitor import Visitor