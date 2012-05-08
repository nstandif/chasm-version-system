import os
import os.path
import versionedNode
import ConfigParser
from versionedNode import VersionedNode

class AssetNode(VersionedNode):
	"""
	Concrete. Inherits from Node. Representative of a project asset folder.
	
	@author: Morgan Strong, Brian Kingery
	"""
	
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Define Functions	
	def checkIntegrity(self):
		super(AssetNode, self).checkIntegrity()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Initialize Node	
	#Constructor
	def __init__(self, path, dirInfoFileName):
		super(AssetNode, self).__init__(path, dirInfoFileName)
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
	nodeInfo.set('Node', 'Type', 'asset')
	
	versionedNode.updateConfigFile(os.path.join(path, name, ".nodeInfo"), nodeInfo)
	
	#with open(os.path.join(path, name, ".nodeInfo"), 'wb') as configFile:
	#	nodeInfo.write(configFile)
	#nodeInfo.write()
	