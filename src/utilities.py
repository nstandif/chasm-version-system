"""
This module contains functionality to manage the animation project.
"""

import os, time, shutil, project
from ConfigParser import ConfigParser

# The project object is just a container to store persistent
# project information.
project = project.Project()
def getProjectName():
	return project._name
def getProjectDir():
	return project._project_dir
def getUsername():
	return project._username
def getUserDir():
	return project._local_dir
def getNullReference():
	"""@returns: The path to the .nullReference file used for symlinks"""
	if not os.path.exists(os.path.join(getProjectDir(), '.nullReference')):
		nullRef = open(os.path.join(getProjectDir(), '.nullReference'), "w")
		nullRef.write("#This is a null reference for symlinks.\n#Nothing has been installed.")
		nullRef.close()
	return os.path.join(getProjectDir(), '.nullReference')

def _writeConfigFile(filePath, configParser):
	"""
	Will update the config file specified by filePath with the contents of configParser
	@precondition: filePath is a valid path
	@precondition: confgParser is an instance of ConfigParser()
	"""
	with open(filePath, 'wb') as configFile:
		configParser.write(configFile)
def _configureProject(parms, file_name):
	project._name = parms[0]
	project._project_dir = parms[1]
	project._username = parms[2]
	project._local_dir = parms[3]
	
	cp = ConfigParser()
	cp.add_section("Project")
	cp.add_section("User")
	cp.set("Project", "Name", getProjectName())
	cp.set("Project", "Directory", getProjectDir())
	cp.set("User", "Name", getUsername())
	cp.set("User", "Directory", getUserDir())
	
	_writeConfigFile(file_name, cp)
def configureProject(file_name):
	"""
	Configures the Project based on the .config.ini file found in the
	program's root directory. This function uses the ConfigParser python
	module for functionality.
	
	@precondition: .config.ini file exists in the program's root directory.
	@precondition: .config.ini file contains complete [Project], [User], and [Misc] sections.
	
	@postcondition: The project is configured with the given information:
		Name, User's Name, Project Directory, and Local Directory.
	"""
	cp = ConfigParser()
	cp.read(file_name)
	
	parms = []
	parms.append(cp.get("Project", "Name"))
	parms.append(cp.get("Project", "Directory"))
	parms.append(cp.get("User", "Name"))
	parms.append(cp.get("User", "Directory"))
	
	_configureProject(parms, file_name)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Folder Management
def createNodeInfoFile(dirPath):
	"""
	Creates the .nodeInfo file in the directory specified by dirPath.
	The Node:Type must be set by concrete nodes
	@precondition: dirPath is a valid directory
	@postcondition: All sections/tags are created and set except "Type".
		"Type" must be set by concrete nodes.
	"""
	username = getUsername()
	timestamp = time.strftime("%a, %d %b %Y %I:%M:%S %p", time.localtime())
	
	nodeInfo = ConfigParser()
	nodeInfo.add_section('Node')
	nodeInfo.set('Node', 'Type', '')
	
	nodeInfo.add_section('Versioning')
	nodeInfo.set('Versioning', 'LatestVersion', '0')
	nodeInfo.set('Versioning', 'Locked', 'False')
	nodeInfo.set('Versioning', 'LastCheckoutTime', timestamp)
	nodeInfo.set('Versioning', 'LastCheckoutUser', username)
	nodeInfo.set('Versioning', 'LastCheckinTime', timestamp)
	nodeInfo.set('Versioning', 'LastCheckinUser', username)
	
	_writeConfigFile(os.path.join(dirPath, ".nodeInfo"), nodeInfo)
def addVersionedFolder(parent, name):
	new_dir = os.path.join(parent, name)
	os.makedirs(os.path.join(new_dir, "src", "v0"))
	os.makedirs(os.path.join(new_dir, "inst"))
	os.symlink(os.path.join(new_dir, 'inst', getNullReference()), os.path.join(new_dir, 'inst','stable'))
	createNodeInfoFile(new_dir)
def addProjectFolder(parent, name):
	os.makedirs(os.path.join(parent, name))
def removeFolder(name):
	pass
def renameFolder(oldName, newName):
	pass

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Checkout
def _createCheckoutInfoFile(dirPath, coPath, version, timestamp, lock):
	"""
	Creates a .checkoutInfo file in the directory specified by dirPath
	@precondition: dirPath is a valid path
	@postcondition: dirPath/.checkoutInfo contains complete [Checkout] section
	"""
	chkoutInfo = ConfigParser()
	chkoutInfo.add_section("Checkout")
	chkoutInfo.set("Checkout", "checkedoutfrom", coPath)
	chkoutInfo.set("Checkout", "checkouttime", timestamp)
	chkoutInfo.set("Checkout", "version", version)
	chkoutInfo.set("Checkout", "lockedbyme", str(lock))
	
	_writeConfigFile(os.path.join(dirPath, ".checkoutInfo"), chkoutInfo)
def checkout(coPath, lock):
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
	
	nodeInfo = ConfigParser()
	nodeInfo.read(os.path.join(coPath, ".nodeInfo"))
	if nodeInfo.get("Versioning", "locked") == "False":
		version = nodeInfo.get("Versioning", "latestversion")
		toCopy = os.path.join(coPath, "src", "v"+version)
		dest = os.path.join(getUserDir(), os.path.basename(coPath))
		
		if(os.path.exists(toCopy)):
			try:
				shutil.copytree(toCopy, dest) # Make the copy
			except Exception as e:
				raise Exception("Could not copy files.")
			timestamp = time.strftime("%a, %d %b %Y %I:%M:%S %p", time.localtime())
			nodeInfo.set("Versioning", "lastcheckoutuser", getUsername())
			nodeInfo.set("Versioning", "lastcheckouttime", timestamp)
			nodeInfo.set("Versioning", "locked", str(lock))
			
			_writeConfigFile(os.path.join(coPath, ".nodeInfo"), nodeInfo)
			_createCheckoutInfoFile(dest, coPath, version, timestamp, lock)
		else:
			raise Exception("Version doesn't exist "+toCopy)
	else:
		whoLocked = nodeInfo.get("Versioning", "lastcheckoutuser")
		whenLocked = nodeInfo.get("Versioning", "lastcheckouttime")
		raise Exception("Can not checkout. Folder is locked by "+whoLocked+" at "+whenLocked)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Checkin
def canCheckin(toCheckin):
	"""
	@returns: True if destination is not locked by another user
		AND this checkin will not overwrite a newer version
	"""
	chkoutInfo = ConfigParser()
	chkoutInfo.read(os.path.join(toCheckin, ".checkoutInfo"))
	chkInDest = chkoutInfo.get("Checkout", "checkedoutfrom")
	version = chkoutInfo.getint("Checkout", "version")
	lockedbyme = chkoutInfo.getboolean("Checkout", "lockedbyme")
	
	nodeInfo = ConfigParser()
	nodeInfo.read(os.path.join(chkInDest, ".nodeInfo"))
	locked = nodeInfo.getboolean("Versioning", "locked")
	latestVersion = nodeInfo.getint("Versioning", "latestversion")
	
	#TODO raise different exceptions to give override options to the user
	result = True
	if lockedbyme == False:
		if locked == True:
			result = False
		if version < latestVersion:
			result = False
	
	return result
def checkin(toCheckin):
	"""
	Checks a folder back in as the newest version
	@precondition: toCheckin is a valid path
	@precondition: canCheckin() == True OR all conflicts have been resolved
	"""
	chkoutInfo = ConfigParser()
	chkoutInfo.read(os.path.join(toCheckin, ".checkoutInfo"))
	chkInDest = chkoutInfo.get("Checkout", "checkedoutfrom")
	lockedbyme = chkoutInfo.getboolean("Checkout", "lockedbyme")
	
	nodeInfo = ConfigParser()
	nodeInfo.read(os.path.join(chkInDest, ".nodeInfo"))
	locked = nodeInfo.getboolean("Versioning", "locked")
	newVersion = nodeInfo.getint("Versioning", "latestversion") + 1
	newVersionPath = os.path.join(chkInDest, "src", "v"+str(newVersion))
	
	if not canCheckin(toCheckin):
		raise Exception("Can not overwrite locked folder.")
	
	# Checkin
	shutil.copytree(toCheckin, newVersionPath)
	
	timestamp = time.strftime("%a, %d %b %Y %I:%M:%S %p", time.localtime())
	nodeInfo.set("Versioning", "lastcheckintime", timestamp)
	nodeInfo.set("Versioning", "lastcheckinuser", getUsername())
	nodeInfo.set("Versioning", "latestversion", str(newVersion))
	nodeInfo.set("Versioning", "locked", "False")
	_writeConfigFile(os.path.join(chkInDest, ".nodeInfo"), nodeInfo)
	
	# Clean up
	shutil.rmtree(toCheckin)
	os.remove(os.path.join(newVersionPath, ".checkoutInfo"))

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Install
def install(path):
	pass