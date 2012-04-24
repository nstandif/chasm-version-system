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
		proj.config()
		print ("Loading Project...")
		proj.load()
	
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
			print("checkout not yet implemented.")
		
		elif raw == 'checkin':
			print("checkin not yet implemented.")
		
		elif raw == 'stats':
			root = proj.getRootNode()
			root.preVisit(InfoVisitor())
		
		elif raw == 'clear':
			os.system("clear")
		
		else:
			print("Unrecognized Input.  Please try again")

if __name__ == "__main__":
	# Someone is launching this directly
	# Enter the main loop
	run()
