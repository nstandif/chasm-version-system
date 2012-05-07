import os
import os.path
import ConfigParser
import versionedNode
from versionedNode import VersionedNode

#TODO shotNode Stuff???

class CompositingNode(VersionedNode):
    """
    Concrete. Inherits from VersionedNode. Representative of a compositing folder.
    
    @author: Brian Kingery, Morgan Strong
    """

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Define Functions	
    def checkIntegrity(self):
        super(CompositingNode, self).checkIntegrity()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Initialize Node	
    #Constructor
    def __init__(self, path, dirInfoFileName):
    	super(CompositingNode, self).__init__(path, dirInfoFileName)
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
	nodeInfo.set('Node', 'Type', 'compositing')
	
	versionedNode.updateConfigFile(os.path.join(path, name, ".nodeInfo"), nodeInfo)