import os.path
import ConfigParser

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
		dirInfoFileName = '.nodeInfo'
		parser = ConfigParser.ConfigParser()
		
		for x in os.listdir(self._fullPath):
			try:
				child_path = self._fullPath + "/" + x
				if os.path.isdir(child_path):
					if not os.path.exists(child_path + "/.nodeInfo"):
						self.addChild(SubNode(child_path))
					else:
						parser.read(child_path + "/" + dirInfoFileName)
						
						#Check integrity of metaData file.
						if not parser.has_section("Node") or not parser.has_option("Node", "Type"):
							raise Exception("File corrupted: " + child_path + "/" + dirInfoFileName)
						
						#Switch on "Type" attribute to create type of node.
						if parser.get("Node", "Type") == "asset":
							self.addChild(AssetNode(child_path, dirInfoFileName))
						#elif parser.get("Node", "Type") == "shot":
						#	self.addChild(ShotNode(child_path, dirInfoFileName))
						#elif parser.get("Node", "Type") == "animation":
						#	self.addChild(AnimationNode(child_path, dirInfoFileName))
						#elif parser.get("Node", "Type") == "fx":
						#	self.addChild(FxNode(child_path, dirInfoFileName))
						#elif parser.get("Node", "Type") == "charfx":
						#	self.addChild(CharfxNode(child_path, dirInfoFileName))
						#elif parser.get("Node", "Type") == "lighting":
						#	self.addChild(LightingNode(child_path, dirInfoFileName))
						#elif parser.get("Node", "Type") == "compositing":
						#	self.addChild(CompositingNode(child_path, dirInfoFileName))
						#elif parser.get("Node", "Type") == "custom":
						#	self.addChild(CustomNode(child_path, dirInfoFileName))
						else:
							raise Exception("Unrecognized Node Type.")
							
						#Add different types of nodes based on the .dirInfo config
						#file, which should contain information about the type.
			except Exception as e:
				print "Failed to load folder:", self._fullPath + x
				print "Error Message:", e
	
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
#from versionedNode import VersionedNode
from subNode import SubNode
from assetNode import AssetNode
from ..visitors.visitor import Visitor