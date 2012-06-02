from PyQt4.QtGui import *
from PyQt4.QtCore import *
import os
from project import Project
import utilities
from utilities import *

_tabNum = 0

def setup(ui):
    if not os.path.exists(".myConfig.ini"):
        parms = []
        parms.append("Chasm")
        ui.messageBox.setText("Please choose the root project directory")
        ui.messageBox.exec_()
        parms.append(ui.setupDirsDialog.getExistingDirectory(ui._MainWindow, "Choose Project Dir", os.environ['HOME']))
        #parms.append(os.environ['USERNAME'])
        parms.append(os.getlogin())
        ui.messageBox.setText("Please choose your local directory")
        ui.messageBox.exec_()
        parms.append(ui.setupDirsDialog.getExistingDirectory(ui._MainWindow, "Choose Local Directory", os.environ['HOME']))
        
        utilities._configureProject(parms, '.myConfig.ini')
    else:
        configureProject('.myConfig.ini')
    
def runAlembic():
    print "Alembic"

def runCheckout(ui):
    tabNum = ui.fileTabs.currentIndex()
    if tabNum == 1:
        curItem = ui.projectFilesTreeWidget.currentItem()
        print curItem.text(0)
        coPath = os.path.join(getProjectDir(), ui.getTreeItemPath(curItem, ""))
        print coPath
        try:
            #TODO ask about locking?
            checkout(coPath, True)
            ui.populateLocalTree()
        except Exception as e:
            ui.errorMessage.showMessage(str(e))
    else:
        ui.errorMessage.showMessage("You can only checkout project files")

def runCheckin(ui):
    tabNum = ui.fileTabs.currentIndex()
    if tabNum == 0:
        curItem = ui.localFilesTreeWidget.currentItem()
        toCheckin = os.path.join(getUserDir(), ui.getTreeItemPath(curItem, ""))
        if canCheckin(toCheckin):
            checkin(toCheckin)
            ui.populateLocalTree()
        else:
            ui.errorMessage.showMessage("Can not checkin: file is locked or newer verion is available")
    else:
        ui.errorMessage.showMessage("You can only checkin local files")

def runInstall(ui):
    tabNum = ui.fileTabs.currentIndex()
    if tabNum == 1:
        curItem = ui.projectFilesTreeWidget.currentItem()
        vDirPath = os.path.join(getProjectDir(), ui.getTreeItemPath(curItem, ""))
        files = getAvailableInstallFiles(vDirPath)
        srcFilePath = str(ui.showFileDialog(ui.convertToQTreeWidgetItems(files)).text(1))
        #TODO ask about stable
        try:
            install(vDirPath, srcFilePath, True)
        except Exception as e:
            ui.errorMessage.showMessage(str(e))
    else:
        ui.errorMessage.showMessage("You can only install project files")

def runNew():
    print "New"

def runRename():
    print "Rename"

def runRemove():
    print "Remove"

def runOpen():
    guiDriver.showFileDialog("/")

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

def fileDialogAccept():
    print "Accepted"
def fileDialogRejected():
    print "Rejected"