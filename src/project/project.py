
import sys, os, os.path
import ConfigParser
import time
import shutil, errno

##TODO: define __all__ in the __init__.py for projectNodes.
##TODO: Perhaps refactor the path stuff into a "PathFactory" of sorts.  This could also handle path validation

class _Project:
	"""
	Singleton: Use project.Project() to instantiate this class
	This class represents the entirety of an animation project. It contains a
	list of folder nodes, project properties, etc.
	
	@author: Morgan Strong, Brian Kingery
	"""
	
	#Constructor
	def __init__(self):
		self._name = ""
		self._username = ""
		self._node = None
		self._projectDir = ""
		self._localDir = ""
	
	# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Project Prep Functions
	
	def config(self, configfile):
		"""
		Configures the Project based on the .config.ini file found in the
		program's root directory. This function uses the ConfigParser python
		module for functionality.
		
		@precondition: .config.ini file exists in the program's root directory.
		@precondition: .config.ini file contains complete [Project], [User], and [Misc] sections.
		
		@postcondition: The project is configured with the given information:
			Name, User's Name, Project Directory, and Local Directory.
		"""
		
		filename = configfile
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
		
		if path[0] != os.path.sep:
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
		if path[0] != os.path.sep:
			raise Exception("Project Directory must be an absolute path.")
		if not os.path.exists(path):
			raise Exception("Project Directory does not exist.")
		else:
			self._projectDir = path
	
	def getProjectDir(self):
		return self._projectDir
	
	def setUserName(self, userName):
		raise NotImplementedError

	def getUserName(self):
		return self._username
	
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
	
	def writeConfigFile(self, filePath, configParser):
		"""
		Will update the config file specified by filePath with the contents of configParser
		@precondition: filePath is a valid path
		@precondition: confgParser is an instance of ConfigParser()
		"""
		with open(filePath, 'wb') as configFile:
			configParser.write(configFile)
	
	def mkDir(self, relPath, name, nodeType):
		#print ("1 - Sub Folder")
		#print ("2 - Asset Folder")
		#print ("3 - Shot Folder")
		#print ("4 - Animation Folder")
		#print ("5 - CharFX Folder")
		#print ("6 - FX Folder")
		#print ("7 - Lighting Folder")
		#print ("8 - Compositing Folder")
		#print os.path.join(self.getProjectDir(), relPath)
		if nodeType == "1":
			subNode.createOnDisk(os.path.join(self.getProjectDir(), relPath), name)
		elif nodeType == "2":
			assetNode.createOnDisk(os.path.join(self.getProjectDir(), relPath), name)
		elif nodeType == "3":
			shotNode.createOnDisk(os.path.join(self.getProjectDir(), relPath), name)
		elif nodeType == "4":
			animationNode.createOnDisk(os.path.join(self.getProjectDir(), relPath), name)
		elif nodeType == "5":
			charfxNode.createOnDisk(os.path.join(self.getProjectDir(), relPath), name)
		elif nodeType == "6":
			fxNode.createOnDisk(os.path.join(self.getProjectDir(), relPath), name)
		elif nodeType == "7":
			lightingNode.createOnDisk(os.path.join(self.getProjectDir(), relPath), name)
		elif nodeType == "8":
			compositingNode.createOnDisk(os.path.join(self.getProjectDir(), relPath), name)
		else:
			raise Exception("Please enter a number 1-8. ")
		return
	
	def _createCheckoutInfoFile(self, dirPath, coPath, version, timestamp, lock):
		"""
		Creates a .checkoutInfo file in the directory specified by dirPath
		@precondition: dirPath is a valid path
		@postcondition: dirPath/.checkoutInfo contains complete [Checkout] section
		"""
		chkoutInfo = ConfigParser.ConfigParser()
		chkoutInfo.add_section("Checkout")
		chkoutInfo.set("Checkout", "checkedoutfrom", coPath)
		chkoutInfo.set("Checkout", "checkouttime", timestamp)
		chkoutInfo.set("Checkout", "version", version)
		chkoutInfo.set("Checkout", "lockedbyme", str(lock))
		
		self.writeConfigFile(os.path.join(dirPath, ".checkoutInfo"), chkoutInfo)
		
	
	def checkout(self, coPath, lock):
		"""
		Copies the 'latest version' from the src folder into the local directory
		@precondition: coPath is a path to a versioned folder
		@precondition: lock is a boolean value
		
		@postcondition: A copy of the 'latest version' will be placed in the local directory
			with the name of the versioned folder
		@postdondition: If lock == True coPath will be locked until it is released by checkin
		"""
		if not os.path.exists(os.path.join(coPath, ".nodeInfo")):
			raise Exception("Not a versioned folder.")
		
		nodeInfo = ConfigParser.ConfigParser()
		nodeInfo.read(os.path.join(coPath, ".nodeInfo"))
		
		if nodeInfo.get("Versioning", "locked") == "False":
			
			version = nodeInfo.get("Versioning", "latestversion")
			toCopy = os.path.join(coPath, "src", "v"+version)
			dest = os.path.join(self.getLocalDir(), os.path.basename(coPath))
			
			if(os.path.exists(toCopy)):
				
				shutil.copytree(toCopy, dest) # Make the copy
				
				timestamp = time.strftime("%a, %d %b %Y %I:%M:%S %p", time.gmtime())
				nodeInfo.set("Versioning", "lastcheckoutuser",self.getUserName())
				nodeInfo.set("Versioning", "lastcheckouttime", timestamp)
				nodeInfo.set("Versioning", "locked", str(lock))
				
				self.writeConfigFile(os.path.join(coPath, ".nodeInfo"), nodeInfo)
				self._createCheckoutInfoFile(dest, coPath, version, timestamp, lock)
			else:
				raise Exception("Version doesn't exist "+toCopy)
		else:
			whoLocked = nodeInfo.get("Versioning", "lastcheckoutuser")
			whenLocked = nodeInfo.get("Versioning", "lastcheckouttime")
			raise Exception("Can not checkout. Folder is locked by "+whoLocked+" at "+whenLocked)
	
	def canCheckin(self, toCheckin):
		"""
		@returns: True if destination is not locked by another user
			AND this checkin will not overwrite a newer version
		"""
		chkoutInfo = ConfigParser.ConfigParser()
		chkoutInfo.read(os.path.join(toCheckin, ".checkoutInfo"))
		chkInDest = chkoutInfo.get("Checkout", "checkedoutfrom")
		version = chkoutInfo.getint("Checkout", "version")
		lockedbyme = chkoutInfo.get("Checkout", "lockedbyme")
		
		nodeInfo = ConfigParser.ConfigParser()
		nodeInfo.read(os.path.join(chkInDest, ".nodeInfo"))
		locked = nodeInfo.getboolean("Versioning", "locked")
		latestVersion = nodeInfo.getint("Versioning", "latestversion")
		
		#TODO raise different exceptions to give override options to the user
		result = True
		if lockedbyme == False:
			if locked == True:
				result = False
			if verion < latestVersion:
				result = False
			
		
		return result
	
	def checkin(self, toCheckin):
		"""
		Checks a folder back in as the newest version
		@precondition: toCheckin is a valid path
		@precondition: canCheckin() == True OR all conflicts have been resolved
		"""
		chkoutInfo = ConfigParser.ConfigParser()
		chkoutInfo.read(os.path.join(toCheckin, ".checkoutInfo"))
		chkInDest = chkoutInfo.get("Checkout", "checkedoutfrom")
		lockedbyme = chkoutInfo.getboolean("Checkout", "lockedbyme")
		
		nodeInfo = ConfigParser.ConfigParser()
		nodeInfo.read(os.path.join(chkInDest, ".nodeInfo"))
		locked = nodeInfo.getboolean("Versioning", "locked")
		newVersion = nodeInfo.getint("Versioning", "latestversion") + 1
		newVersionPath = os.path.join(chkInDest, "src", "v"+str(newVersion))
		
		if locked == True and lockedbyme == False:
			raise Exception("Can not overwrite locked folder")
		
		# Checkin
		shutil.copytree(toCheckin, newVersionPath)
		
		timestamp = time.strftime("%a, %d %b %Y %I:%M:%S %p", time.gmtime())
		nodeInfo.set("Versioning", "lastcheckintime", timestamp)
		nodeInfo.set("Versioning", "lastcheckinuser", self.getUserName)
		nodeInfo.set("Versioning", "latestversion", str(newVersion))
		nodeInfo.set("Versioning", "locked", "False")
		self.writeConfigFile(os.path.join(chkInDest, ".nodeInfo"), nodeInfo)
		
		# Clean up
		shutil.rmtree(toCheckin)
		os.remove(os.path.join(newVersionPath, ".checkoutInfo"))
		
		

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Sudo Singleton
#Creates and stores an instance of the project
_project = _Project()
def Project():
	"""
	Use this function to get the project.
	@returns: The one and only instance of the Project
	"""
	return _project

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Prevent Cyclic Dependencies
from projectNodes import rootNode
from projectNodes import subNode
from projectNodes import assetNode
from projectNodes import shotNode
from projectNodes import animationNode
from projectNodes import charfxNode
from projectNodes import fxNode
from projectNodes import lightingNode
from projectNodes import compositingNode