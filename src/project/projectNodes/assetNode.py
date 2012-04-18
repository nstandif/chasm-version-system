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
		print "Checking AssetNode integrity..."
		if not os.path.exists(self._fullPath + "/src") or \
				not os.path.exists(self._fullPath + "/inst") or \
				not os.path.exists(self._fullPath + "/inst/latest") or \
				not os.path.exists(self._fullPath + "/inst/stable"):
			raise Exception("Asset: " + self._name + " is missing a critical folder/link.")
		
		
		
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
		