#!/usr/bin/env python

""" Author: Morgan Strong	Date: 4/12/12
	
	This is a test driver used for developing the chasm file versioning system.
"""

import os, sys, traceback
from project.project import Project
from project.visitors.infoVisitor import InfoVisitor

def run():
	"""
	* Initialize the Chasm Project.
	* Continually process input from the user for testing purposes.
	"""
	
	try:
		print ("Creating New Project...")
		proj = Project()
		print ("Configuring Project...")
		#proj.config()
		if len(sys.argv) == 2 and os.path.exists(str(sys.argv[1])):
			proj.config(str(sys.argv[1]))
		else:
			proj.config('.config.ini')
	
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
			coPath = os.path.join(proj.getProjectDir(), temp)
			if os.path.exists(coPath):
				print("Do you want to lock this folder? (y/n):")
				resp = raw_input()
				#TODO
				#except OSError as exc:
				#	if exc.errno == errno.EEXIST:
				try:
					if resp == "y":
						proj.checkout(coPath, True)
					elif resp == "n":
						proj.checkout(coPath, False)
				except Exception as e:
					print "Error:", e
			else:
				print("The specified path does not exist.")
				
		
		elif raw == 'checkin':
			print("Specify the folder you wish to checkin:")
			temp = raw_input()
			toCheckin = os.path.join(proj.getLocalDir(), temp)
			if os.path.exists(toCheckin):
				#TODO catch exception and add override functionality
				if(proj.canCheckin(toCheckin)):
					proj.checkin(toCheckin)
				else:
					print("Can not checkin: file is locked or newer verion is available")
			else:
				print("The specified path does not exist.")
		
		elif raw == 'new':
			print ("Specify the path, starting from the root directory:")
			temp = raw_input()
			if os.path.exists(os.path.join(proj.getProjectDir(), temp)):
				print ("What do you want to name the folder?")
				temp2 = raw_input()
				print ("What type of folder do you want to create?")
				print ("1 - Sub Folder")
				print ("2 - Asset Folder")
				print ("3 - Shot Folder")
				print ("4 - Animation Folder")
				print ("5 - CharFX Folder")
				print ("6 - FX Folder")
				print ("7 - Lighting Folder")
				print ("8 - Compositing Folder")
				temp3 = raw_input()
				proj.mkDir(temp, temp2, temp3)
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
			print("Unrecognized Input.  Please try again")

if __name__ == "__main__":
	# Someone is launching this directly
	# Enter the main loop
	run()
