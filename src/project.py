
import sys, os, os.path
import ConfigParser
import time
import shutil, errno

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
		self._project_dir = ""
		self._username = ""
		self._local_dir = ""
	
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> pseudo Singleton
#Creates and stores an instance of the project
_project = _Project()
def Project():
	"""
	Use this function to get the project.
	@returns: The one and only instance of the Project
	"""
	return _project