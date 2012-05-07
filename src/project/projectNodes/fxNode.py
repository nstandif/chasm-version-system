import os
import os.path
import ConfigParser
import versionedNode
from versionedNode import VersionedNode

#TODO shotNode stuff???

class FXNode(VersionedNode):
	"""
	Concrete. Inherits from Node. Representative of a project fx folder.
	
	@author: Morgan Strong, Brian Kingery
	"""
	
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Define Functions	
	def checkIntegrity(self):
		super(FXNode, self).checkIntegrity()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Initialize Node	
	#Constructor
	def __init__(self, path, dirInfoFileName):
		super(FXNode, self).__init__(path, dirInfoFileName)
		self.checkIntegrity()
		self._loadChildren()

"""
Methods not bound to an instance of the class:
"""
def createOnDisk(path, name):
	versionedNode.createOnDisk(path, name)
	
	#Set the node type in .nodeInfo
	nodeInfo = ConfigParser.ConfigParser()
	nodeInfo.read(os.path.join(path, name, ".nodeInfo"))
	nodeInfo.set('Node', 'Type', 'fx')
	
	versionedNode.updateConfigFile(os.path.join(path, name, ".nodeInfo"), nodeInfo)