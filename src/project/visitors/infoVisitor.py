from visitor import Visitor
from ..projectNodes.versionedNode import VersionedNode

class InfoVisitor(Visitor):
	"""
	CONCRETE. Prints information about each node that is passed to it.
	
	@author: Morgan Strong
	"""

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Define Functions	
	def run(self, curNode):
		print "Name:", curNode.getName()
		print "Type:", curNode.__class__
		print "Children:"
		for x in curNode.getChildren():
			print ("\t" + x.getName())
		
		if isinstance(curNode, VersionedNode):
			print ("Version Info:")
			print ("\tLatest Version: %s" % curNode.getLatestVersion())
			print ("\tLocked: %s" % curNode.isLocked())
			print ("\tLastCheckoutTime: %s" % curNode.getLastCheckoutTime())
			print ("\tLastCheckoutUser: %s" % curNode.getLastCheckoutUser())
			print ("\tLastCheckinTime: %s" % curNode.getLastCheckinTime())
			print ("\tLastCheckinUser: %s" % curNode.getLastCheckinUser())
			
		print ("-----")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Initialize Visitor	
	#Constructor
	def __init__(self):
		pass
