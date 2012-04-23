import os
import os.path
from versionedNode import VersionedNode

class AnimationNode(VersionedNode):
	"""
	Concrete. Inherits from Node. Representative of a project asset folder.
	
	@author: Morgan Strong
	"""
	
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Define Functions	
	def checkIntegrity(self):
		super(AnimationNode, self).checkIntegrity()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Initialize Node	
	#Constructor
	def __init__(self, path, dirInfoFileName):
		super(AnimationNode, self).__init__(path, dirInfoFileName)
		self.checkIntegrity()
		self._loadChildren()
		