import os.path
import ConfigParser

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
		self._nodes = []
		self._projectDir = ""
		self._localDir = ""
	
	def config(self):
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
		if path[0] != '/':
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
	

# >>>>>>>>>>>>>>>>>>>>>>>>>>>> API Functions
	def getName(self):
		return self._name
	
	def setProjectDir(self, path):
		if path[0] != '/':
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