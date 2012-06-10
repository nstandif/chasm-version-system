from PyQt4.QtGui import *
from PyQt4.QtCore import *
import os, glob, types, subprocess
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
        parms.append(str(ui.setupDirsDialog.getExistingDirectory(ui._MainWindow, "Choose Project Dir", os.environ['HOME'])))
        #TODO ask for user name?
        parms.append(os.getlogin())
        ui.messageBox.setText("Please choose your local directory")
        ui.messageBox.exec_()
        parms.append(str(ui.setupDirsDialog.getExistingDirectory(ui._MainWindow, "Choose Local Directory", os.environ['HOME'])))
        
        utilities._configureProject(parms, '.myConfig.ini')
    else:
        configureProject('.myConfig.ini')
    populateLocalTree(ui)
    populateProjectTree(ui)
    enableComponents(ui)
    
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Common User Actions

def runAlembic():
    print "Alembic"

def runCheckout(ui):
    tabNum = ui.fileTabs.currentIndex()
    if tabNum == 1:
        curItem = ui.projectFilesTreeWidget.currentItem()
        coPath = ui.getTreeItemPath(curItem, getProjectDir())
        try:
            #TODO ask about locking?
            checkout(coPath, True)
            setProjectTreeVersionedItemInfo(curItem, coPath)
            populateLocalTree(ui)
        except Exception as e:
            ui.errorMessage.showMessage(str(e))
    else:
        ui.errorMessage.showMessage("You can only checkout project files")

def runCheckin(ui):
    tabNum = ui.fileTabs.currentIndex()
    if tabNum == 0:
        curItem = ui.localFilesTreeWidget.currentItem()
        toCheckin = ui.getTreeItemPath(curItem, getUserDir())
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
        vDirPath = ui.getTreeItemPath(curItem, getProjectDir())
        files = getAvailableInstallFiles(vDirPath)
        srcFilePath = str(ui.file_select_dialog.selectFile(convertToFileSelectionDialogItems(files)).text(1))
        #TODO ask about stable
        try:
            install(vDirPath, srcFilePath, True)
            setProjectTreeVersionedItemInfo(curItem, vDirPath)
            #populateProjectTree(ui)
        except Exception as e:
            ui.errorMessage.showMessage(str(e))
    else:
        ui.errorMessage.showMessage("You can only install project files")

def runNew(ui):
    if ui.fileTabs.currentIndex() == 1:
        curItem = ui.projectFilesTreeWidget.currentItem()
        if curItem.isSelected() and isVersionedFolder(ui.getTreeItemPath(curItem, getProjectDir())):
            return
        folderType, folderName = ui.newFolderDialog.getNewFolder()
        if folderType == None or folderName == None:
            return
        if curItem.isSelected():
            if folderType == 0:
                newPath = addProjectFolder(ui.getTreeItemPath(curItem, getProjectDir()), folderName)
            else:
                newPath = addVersionedFolder(ui.getTreeItemPath(curItem, getProjectDir()), folderName)
            curItem.addChildren(convertToProjectTreeItems([newPath]))
        else:
            if folderType == 0:
                newPath = addProjectFolder(getProjectDir(), folderName)
            else:
                newPath = addVersionedFolder(getProjectDir(), folderName)
            ui.projectFilesTreeWidget.addTopLevelItems(convertToProjectTreeItems([newPath]))
    
def runRename():
    print "Rename"

def runRemove():
    print "Remove"

def runOpen(ui):
    if ui.fileTabs.currentIndex() == 0:
        curItem = ui.localFilesTreeWidget.currentItem()
        dirPath = ui.getTreeItemPath(curItem, getUserDir())
        files = glob.glob(os.path.join(dirPath, "*"))
        toOpen = str(ui.file_select_dialog.selectFile(convertToFileSelectionDialogItems(files)).text(1))
        os.system("xdg-open "+toOpen)

def runUpdatePlugins():
    print "Update Plugins"

def runSettings():
    print "Settings"

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Model to GUI Conversions

def convertToFileSelectionDialogItems(files):
    treeItems = []
    for f in files:
        item = QTreeWidgetItem()
        item.setText(0, os.path.basename(f))
        item.setText(1, f)
        treeItems.append(item)
    return treeItems

def convertToLocalTreeItems(files):
    treeItems = []
    for f in files:
        item = QTreeWidgetItem()
        item.setText(0, os.path.basename(f))
        item.setText(1, getFilesCheckoutTime(f))
        item.setText(2, f) #TODO last opened stuff
        item.setText(3, f)
        treeItems.append(item)
    return treeItems

def convertToProjectTreeItems(files):
    treeItems = []
    for f in files:
        item = QTreeWidgetItem()
        item.setText(0, os.path.basename(f))
        if isVersionedFolder(f):
            setProjectTreeVersionedItemInfo(item, f)
        treeItems.append(item)
    return treeItems

def setProjectTreeVersionedItemInfo(pTreeItem, curDir):
    info = getVersionedFolderInfo(curDir)
    pTreeItem.setText(1, info[0])
    pTreeItem.setText(2, info[1])
    pTreeItem.setText(3, info[2])
    pTreeItem.setText(4, info[3])
    pTreeItem.setText(5, info[4])

def populateProjectTree(ui):
    ui.projectFilesTreeWidget.clear()
    recurseProjectFiles(ui, ui.projectFilesTreeWidget, getProjectDir())

def recurseProjectFiles(ui, parent, curDir):
    if isVersionedFolder(curDir):
        setProjectTreeVersionedItemInfo(parent, curDir)
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
    items = convertToLocalTreeItems(files)
    ui.localFilesTreeWidget.addTopLevelItems(items)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Other Helper Functions

def enableComponents(ui):
    # Project Tab Open
    if ui.fileTabs.currentIndex():
        ui.actionRename.setEnabled(False)
        ui.actionRemove.setEnabled(False)
        
        curItem = ui.projectFilesTreeWidget.currentItem()
        ui.actionCheckin.setEnabled(False)
        ui.actionOpen_File.setEnabled(False)
        if not type(curItem) == types.NoneType and curItem.isSelected():
            if curItem.text(2):
                ui.actionNew.setEnabled(False)
                ui.actionCheckout.setEnabled(True)
                ui.actionInstall.setEnabled(True)
                ui.actionCache_to_Alembic.setEnabled(True)
        else:
            ui.actionNew.setEnabled(True)
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
        if not type(curItem) == types.NoneType and curItem.isSelected():
            if curItem.text(2):
                ui.actionCheckin.setEnabled(True)
                ui.actionOpen_File.setEnabled(True)
        else:
            ui.actionCheckin.setEnabled(False)
            ui.actionOpen_File.setEnabled(False)

def tabSwitch(ui, tabNum):
    enableComponents(ui)

def localItemSelectionChanged(ui):
    enableComponents(ui)
    
def projectItemSelectionChanged(ui):
    enableComponents(ui)

def localFilesContextMenu(ui, point):
    enableComponents(ui)
    ui.localPopMenu.popup(ui.projectFilesTreeWidget.mapToGlobal(point))

def projectFilesContextMenu(ui, point):
    enableComponents(ui)
    ui.projectPopMenu.popup(ui.projectFilesTreeWidget.mapToGlobal(point))

def fileDialogAccept():
    print "Accepted"
def fileDialogRejected():
    print "Rejected"

