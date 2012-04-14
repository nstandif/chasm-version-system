import os.path
from ..projectNodes.node import Node

class Visitor(object):
	"""
	ABSTRACT. Representative of a per Node algorithm. A Visitor type object may
	be instantiated and passed to the root node, traversing the tree through a
	pre-order or post-order traversal.
	
	@author: Morgan Strong
	"""

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Define Functions	
	def run(self, curNode):
		raise NotImplementedError

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Initialize Visitor	
	#Constructor
	def __init__(self):
		raise NotImplementedError