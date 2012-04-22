import os
import os.path
from versionedNode import VersionedNode

class AssetNode(VersionedNode):
	"""
	Concrete. Inherits from Node. Representative of a project category folder.
	
	@author: Morgan Strong
	"""
	
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Define Functions	
	def checkIntegrity(self):
		print ("Checking AssetNode integrity...")
		return True
	
	def _loadChildren(self):
		#Load the src and inst folders here.
		return

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Initialize Node	
	#Constructor
	def __init__(self, path, dirInfoFileName):
		super(AssetNode, self).__init__(path, dirInfoFileName)
		self._loadChildren()
		self.checkIntegrity()
		