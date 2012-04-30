import os, sys, traceback, shutil
from project.project import Project
from project.visitors.infoVisitor import InfoVisitor

def nodeCreationTest():
    """
    Test the creation of each concreat node type
    @author Brian Kingery
    """
    try:
        print ("Creating New Project...")
        proj = Project()
        print ("Configuring Project...")
        if len(sys.argv) == 2 and os.path.exists(str(sys.argv[1])):
            proj.config(str(sys.argv[1]))
        else:
            proj.config('.config.ini')

    except Exception as e:
    	print "Error:", e
    	print "Stacktrace:"
    	traceback.print_tb(sys.exc_info()[2], 20)
    	return
    
    testfolder = os.path.join(proj.getProjectDir(), "nodeCreationTest")

    #Delete old nodeCreationTest folder
    if os.path.exists(testfolder):
        shutil.rmtree(testfolder)
    
    #Create nodeCreationTest folder
    proj.mkDir("", "nodeCreationTest", "1")
    
    #Create an instance of all node types
    proj.mkDir(testfolder, "asset", "2")
    proj.mkDir(testfolder, "shot", "3")
    proj.mkDir(testfolder, "animation", "4")
    proj.mkDir(testfolder, "charfx", "5")
    proj.mkDir(testfolder, "fx", "6")
    proj.mkDir(testfolder, "lighting", "7")
    proj.mkDir(testfolder, "compositing", "8")
    
    #TODO test the .nodeInfo files
    
    #Print results
    try:
        proj.load()
        root = proj.getRootNode()
        root.preVisit(InfoVisitor())
    except Exception as e:
        print e
    
    #TODO fix this
    #errors = root.getErrorList()
    #if errorList:
    #    print ("\nCreation Failed!!!\nErrors occurre while loading")

if __name__ == '__main__':
    # Someone is launching this directly
    nodeCreationTest()