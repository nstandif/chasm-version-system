import os
import os.path
import versionedNode
import ConfigParser
from versionedNode import VersionedNode

#TODO shotNode stuff

class AnimationNode(VersionedNode):
	"""
	Concrete. Inherits from Node. Representative of a project animation folder.
	
	@author: Morgan Strong, Brian Kingery
	"""
	
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Define Functions	
	def checkIntegrity(self):
		super(AnimationNode, self).checkIntegrity()
		if not os.path.exists(os.path.join(self._fullPath, "cache")):
			raise Exception("Animation Folder: " + self._fullPath + " is missing its cache folder.")
		return True

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Initialize Node	
	#Constructor
	def __init__(self, path, dirInfoFileName):
		super(AnimationNode, self).__init__(path, dirInfoFileName)
		self.checkIntegrity()
		self._loadChildren()

"""
Methods not bound to an instance of the class:
"""
def createOnDisk(path, name):
	versionedNode.createOnDisk(path, name)
	
	os.mkdir(os.path.join(path, name, 'cache'))
	
	#Set the node type in .nodeInfo
	nodeInfo = ConfigParser.ConfigParser()
	nodeInfo.read(os.path.join(path, name, ".nodeInfo"))
	nodeInfo.set('Node', 'Type', 'animation')
	
	versionedNode.updateConfigFile(os.path.join(path, name, ".nodeInfo"), nodeInfo)