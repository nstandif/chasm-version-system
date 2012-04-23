import os
import os.path
from node import Node

class ShotNode(Node):
	"""
	Concrete. Inherits from Node. Representative of a project shot folder.
	
	@author: Morgan Strong
	"""
	
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Define Functions	
	def checkIntegrity(self):
		print "Checking ShotNode integrity..."
		
		children = os.listdir(self._fullPath)
		validChildren = ["animation", "fx", "charfx", "lighting", "compositing"]
		
		toRemove = []
		for x in children:
			if x in validChildren:
				toRemove.append(x)
			elif not os.path.isdir(self._fullPath + "/" + x):
				toRemove.append(x)
		for x in toRemove:
			children.remove(x)
		
		if children:
			print children
			raise Exception("Shot: " + self._name + " contains invalid folders. \
Valid folders are: animation, fx, charfx, lighting, and compositing")
		
		return True
	
	#def _loadChildren(self):
	#	#Load animation, fx, charfx, lighting, and compositing
	#	for x in os.listdir(self._fullPath):
	#		if os.path.isdir(self._fullPath + "/" + x):
	#			if x == "animation":
	#				self.addChild(AnimationNode())
	#			elif x == "fx":
	#				self.addChild(FxNode())
	#			elif x == "charfx":
	#				self.addChild(CharfxNode())
	#			elif x == "lighting":
	#				self.addChild(LightingNode())
	#			elif x == "compositing":
	#				self.addChild(CompositingNode())
	#	return

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Initialize Node	
	#Constructor
	def __init__(self, path, dirInfoFileName):
		super(ShotNode, self).__init__(path)
		self.checkIntegrity()
		print "this is called."
		self._loadChildren()
		print self._children
		