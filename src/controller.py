def runAlembic():
    print "Alembic"

def runCheckout():
    print "Checkout"

def runCheckin():
    print "Checkin"

def runInstall():
    print "Install"

def runOpen():
    print "Open"

def runUpdatePlugins():
    print "Update Plugins"

def runSettings():
    print "Settings"

def tabSwitch(tabNum):
    print "Switched tab to", str(tabNum)

def localItemSelectionChanged():
    print "Local Item Selection Changed"

def localFilesContextMenu(point1):
    print "Local Item Context Menu", str(point1)

def projectItemSelectionChanged():
    print "Project Item Selection Changed"

def projectFilesContextMenu(point1):
    print "Project Item Context Menu", str(point1)