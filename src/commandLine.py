#!/usr/bin/env python

""" Author: Morgan Strong	Date: 4/12/12
	
	This is a test driver used for developing the chasm file versioning system.
"""

import os, sys, traceback
from project import Project
from utilities import *
#from project.visitors.infoVisitor import InfoVisitor

def run():
	"""
	* Initialize the Chasm Project.
	* Continually process input from the user for testing purposes.
	"""
	
	try:
		print ("Creating New Project...")
		proj = Project()
		print ("Configuring Project...")
		if len(sys.argv) == 2 and os.path.exists(str(sys.argv[1])):
			configureProject(str(sys.argv[1]))
		else:
			configureProject('.config.ini')
	except Exception as e:
		print "Error:", e
		print "Stacktrace:"
		traceback.print_tb(sys.exc_info()[2], 20)
		return

	while(True):
		print("\nWelcome to the Chasm File Manager.")
		print("Type 'e' at this command prompt to quit.")
		raw = raw_input()
		
		if raw == 'e':
			break
		
		elif raw == 'checkout':
			print("Specify the path, starting from the root directory:")
			temp = raw_input()
			coPath = os.path.join(getProjectDir(), temp)
			if os.path.exists(coPath):
				print("Do you want to lock this folder? (y/n):")
				resp = raw_input()
				#TODO
				#except OSError as exc:
				#	if exc.errno == errno.EEXIST:
				try:
					if resp == "y":
						checkout(coPath, True)
					elif resp == "n":
						checkout(coPath, False)
				except Exception as e:
					print "Error:", e
			else:
				print("The specified path does not exist.")
				
		
		elif raw == 'checkin':
			print("Specify the folder you wish to checkin:")
			temp = raw_input()
			toCheckin = os.path.join(getUserDir(), temp)
			if os.path.exists(toCheckin):
				#TODO catch exception and add override functionality
				if(canCheckin(toCheckin)):
					checkin(toCheckin)
				else:
					print("Can not checkin: file is locked or newer verion is available")
			else:
				print("The specified path does not exist.")
		
		elif raw == 'new':
			print ("Specify the path, starting from the root directory:")
			temp = raw_input()
			if os.path.exists(os.path.join(getProjectDir(), temp)):
				print ("What do you want to name the folder?")
				temp2 = raw_input()
				print ("Is this a versioned folder?")
				temp3 = raw_input()
				if temp3 == "y":
					addVersionedFolder(os.path.join(getProjectDir(),temp), temp2)
				else:
					addProjectFolder(os.path.join(getProjectDir(),temp), temp2)
			else:
				print ("The specified path does not exist.")
		
		elif raw == 'stats':
			try:
				proj.load()
				root = proj.getRootNode()
				root.preVisit(InfoVisitor())
			except Exception as e:
				print e
		
		elif raw == 'clear':
			os.system("clear")
			
		else:
			print("e, checkout, checkin, new, stats, clear")

if __name__ == "__main__":
	# Someone is launching this directly
	# Enter the main loop
	run()
