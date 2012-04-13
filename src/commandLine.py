#!/usr/bin/env python

""" Author: Morgan Strong	Date: 4/12/12
	
	This is a test driver used for developing the chasm file versioning system.
"""

from project.project import Project

def run():
	"""
	Initialize the Chasm Project.
	Continually process input from the user for testing purposes.
	"""
	try:
		proj = Project()
		proj.config()
		print proj.getName()
		print proj.getProjectDir()
		print proj.getLocalDir()
		
	
	except Exception as e:
		print e
		return
	
	while(True):
		print("Welcome to the Chasm File Manager.")
		print("Type 'e' at this command prompt to quit.")
		raw = raw_input()
		
		if raw == 'e':
			break
		
		elif raw == 'checkout':
			print("checkout not yet implemented.")
		
		elif raw == 'checkin':
			print("checkin not yet implemented.")
		
		elif raw == 'status':
			print("status not yet implemented.")
		
		else:
			print("Unrecognized Input.  Please try again")

if __name__ == "__main__":
	# Someone is launching this directly
	# Enter the main loop
	run()
