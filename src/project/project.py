import os.path
import ConfigParser
from projectNodes import rootNode

##TODO: define __all__ in the __init__.py for projectNodes.
##TODO: Perhaps refactor the path stuff into a "PathFactory" of sorts.  This could also handle path validation

class Project:
	"""
	This class represents the entirety of an animation project. It contains a
	list of folder nodes, project properties, etc.
	
	@author: Morgan Strong
	"""
	
	#Constructor
	def __init__(self):
		self._name = ""
		self._username = ""
		self._node = None
		self._projectDir = ""
		self._localDir = ""
	
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Project Prep Functions
	
	def config(self):
		"""
		Configures the Project based on the .config.ini file found in the
		program's root directory. This function uses the ConfigParser python
		module for functionality.
		
		@precondition: .config.ini file exists in the program's root directory.
		@precondition: .config.ini file contains complete [Project], [User], and [Misc] sections.
		
		@postcondition: The project is configured with the given information:
			Name, User's Name, Project Directory, and Local Directory.
		"""
		
		filename = '.config.ini'
		cp = ConfigParser.ConfigParser()
		cp.read(filename)
		
		if not (cp.has_section("Project") and cp.has_section("User") \
				and cp.has_section("Misc")):
			print cp.sections()
			raise Exception("Config file is missing one or more necessary sections")
		
		#Parse Project Name
		self._name = cp.get("Project", "Name")
		
		#Parse Project Directory
		path = cp.get("Project", "Directory")
		
		if path[0] != '/': #TODO This wont work on windows
			raise Exception("Project Directory must be an absolute path.")
		if not os.path.exists(path):
			raise Exception("Project Directory does not exist.")
		else:
			self._projectDir = path
		
		#Parse User Name
		self._username = cp.get("User", "Name")
		
		#Parse User Directory
		path = cp.get("User", "Directory")
		if not os.path.exists(os.path.expanduser(path)):
			raise Exception("Local Project Directory does not exist.")
		else:
			self._localDir = os.path.expanduser(path)
	
	
	
	def load(self):
		"""
		Loads a project into memory by building a node network based on the
		project directory's folder structure.  Creation of nodes can raise
		Exceptions if the folder structure is corrupt.
		
		@precondition: config needs to be run successfully before load can be
			run successfully.
		
		@postcondition: The node network is loaded into memory.
		"""
		
		self._node = rootNode.RootNode(self._projectDir)
	

# >>>>>>>>>>>>>>>>>>>>>>>>>>>> API Functions
	def getName(self):
		return self._name
	
	def setProjectDir(self, path):
		if path[0] != '/': #TODO this wont work on windows
			raise Exception("Project Directory must be an absolute path.")
		if not os.path.exists(path):
			raise Exception("Project Directory does not exist.")
		else:
			self._projectDir = path
	
	def getProjectDir(self):
		return self._projectDir
	
	def setLocalDir(self, path):
		if not os.path.exists(os.path.expanduser(path)):
			raise Exception("Local Project Directory does not exist.")
		else:
			self._localDir = os.path.expanduser(path)
			self.config()
	
	def getLocalDir(self):
		return self._localDir
	
	def getRootNode(self):
		return self._node
	
	def mkDir(self, path, name):
		#
		return