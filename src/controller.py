from PyQt4.QtGui import *
from PyQt4.QtCore import *
import os, glob, types
from project import Project
import utilities
from utilities import *

_tabNum = 0

def setup(ui):
    #TODO change to .config.ini to match utilities
    if not os.path.exists(".myConfig.ini"):
        parms = []
        parms.append("Chasm")
        ui.messageBox.setText("Please choose the root project directory")
        ui.messageBox.exec_()
        parms.append(ui.setupDirsDialog.getExistingDirectory(ui._MainWindow, "Choose Project Dir", os.environ['HOME']))
        #TODO ask for user name?
        parms.append(os.getlogin())
        ui.messageBox.setText("Please choose your local directory")
        ui.messageBox.exec_()
        parms.append(ui.setupDirsDialog.getExistingDirectory(ui._MainWindow, "Choose Local Directory", os.environ['HOME']))
        
        utilities._configureProject(parms, '.myConfig.ini')
    else:
        configureProject('.myConfig.ini')
    populateLocalTree(ui)
    populateProjectTree(ui)
    enableComponents(ui)
    
def runAlembic():
    print "Alembic"

def runCheckout(ui):
    tabNum = ui.fileTabs.currentIndex()
    if tabNum == 1:
        curItem = ui.projectFilesTreeWidget.currentItem()
        print curItem.text(0)
        coPath = os.path.join(getProjectDir(), ui.getTreeItemPath(curItem, ""), )
        print coPath
        try:
            #TODO ask about locking?
            checkout(coPath, True)
            populateLocalTree(ui)
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
            populateLocalTree(ui)
            populateProjectTree(ui)
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
            populateProjectTree(ui)
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

def tabSwitch(ui, tabNum):
    enableComponents(ui)

def localItemSelectionChanged(ui):
    enableComponents(ui)

def localFilesContextMenu(point1):
    print "Local Item Context Menu", str(point1)

def projectItemSelectionChanged(ui):
    enableComponents(ui)

def projectFilesContextMenu(point1):
    print "Project Item Context Menu", str(point1)

def fileDialogAccept():
    print "Accepted"
def fileDialogRejected():
    print "Rejected"

def populateProjectTree(ui):
    ui.projectFilesTreeWidget.clear()
    recurseProjectFiles(ui, ui.projectFilesTreeWidget, getProjectDir())

def recurseProjectFiles(ui, parent, curDir):
    if isVersionedFolder(curDir):
        info = getVersionedFolderInfo(curDir)
        parent.setText(1, info[0])
        parent.setText(2, info[1])
        parent.setText(3, info[2])
        parent.setText(4, info[3])
        parent.setText(5, info[4])
        return
    
    if os.path.isdir(curDir):
        files = glob.glob(os.path.join(curDir, '*'))
        for f in files:
            item = QTreeWidgetItem(parent)
            item.setText(0, os.path.basename(f))
            recurseProjectFiles(ui, item, f)

def populateLocalTree(ui):
    ui.localFilesTreeWidget.clear()
    files = glob.glob(os.path.join(str(getUserDir()),'*'))
    items = convertToLocalTreeWidgetItems(files)
    ui.localFilesTreeWidget.addTopLevelItems(items)

def convertToLocalTreeWidgetItems(files):
    treeItems = []
    for f in files:
        item = QTreeWidgetItem()
        item.setText(0, os.path.basename(f))
        item.setText(1, getFilesCheckoutTime(f))
        item.setText(2, f) #TODO last opened stuff
        item.setText(3, f)
        treeItems.append(item)
    return treeItems

def enableComponents(ui):
    # Project Tab Open
    if ui.fileTabs.currentIndex():
        ui.actionNew.setEnabled(False)
        ui.actionRename.setEnabled(False)
        ui.actionRemove.setEnabled(False)
        
        curItem = ui.projectFilesTreeWidget.currentItem()
        ui.actionCheckin.setEnabled(False)
        ui.actionOpen_File.setEnabled(False)
        if not type(curItem) == types.NoneType:
            if curItem.text(2):
                ui.actionCheckout.setEnabled(True)
                ui.actionInstall.setEnabled(True)
                ui.actionCache_to_Alembic.setEnabled(True)
            else:
                ui.actionCheckout.setEnabled(False)
                ui.actionInstall.setEnabled(False)
                ui.actionCache_to_Alembic.setEnabled(False)
    # Local Tab Open
    else:
        ui.actionNew.setEnabled(False)
        ui.actionRename.setEnabled(False)
        ui.actionRemove.setEnabled(False)
        
        curItem = ui.localFilesTreeWidget.currentItem()
        ui.actionCheckout.setEnabled(False)
        ui.actionInstall.setEnabled(False)
        ui.actionCache_to_Alembic.setEnabled(False)
        if not type(curItem) == types.NoneType:
            if curItem.text(2):
                ui.actionCheckin.setEnabled(True)
                ui.actionOpen_File.setEnabled(True)
            else:
                ui.actionCheckin.setEnabled(False)
                ui.actionOpen_File.setEnabled(False)