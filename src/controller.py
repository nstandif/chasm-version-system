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

def localItemSelectionChanged(item1, item2):
    print "Local Item Selection Changed", str(item2)

def localFilesContextMenu(point1):
    print "Local Item Context Menu", str(point1)

def projectItemSelectionChanged(item1, item2):
    print "Project Item Selection Changed", str(item2)

def projectFilesContextMenu(point1):
    print "Project Item Context Menu", str(point1)