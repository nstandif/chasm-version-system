# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI2.ui'
#
# Created: Mon May  7 16:38:31 2012
#	  by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import os, types
import controller

try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class DeselectableTreeWidget(QTreeWidget):
    def mousePressEvent(self, event):
        self.clearSelection()
        QTreeWidget.mousePressEvent(self, event)

class FileSelectDialog(QDialog):
    def setup(self):
        self.setObjectName(_fromUtf8("file_select_dialog"))
        self.resize(330, 475)
        self.hl = QHBoxLayout(self)
        self.hl.setObjectName(_fromUtf8("horizontalLayout"))
        self.tw = QTreeWidget(self)
        self.tw.setObjectName(_fromUtf8("treeWidget"))
        self.hl.addWidget(self.tw)
        self.bb = QDialogButtonBox(self)
        self.bb.setOrientation(Qt.Vertical)
        self.bb.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.bb.setObjectName(_fromUtf8("buttonBox"))
        self.hl.addWidget(self.bb)
        self.setModal(True)
        self.setWindowTitle(QApplication.translate("Select a File", "", None, QApplication.UnicodeUTF8))
        self.tw.headerItem().setText(0, QApplication.translate("FileSelectDialog", "File", None, QApplication.UnicodeUTF8))
        QObject.connect(self.bb, SIGNAL(_fromUtf8("accepted()")), self.accept)
        QObject.connect(self.bb, SIGNAL(_fromUtf8("rejected()")), self.reject)
        QMetaObject.connectSlotsByName(self)
    
    def selectFile(self, filesToDisplay):
        self.tw.clear()
        self.tw.addTopLevelItems(filesToDisplay)
        if self.exec_() == 1:
            return self.tw.currentItem()
        else:
            return None

class NewFolderDialog(QDialog):
    def setup(self):
        self.setObjectName(_fromUtf8("newFolderDialog"))
        #self.resize(330, 475)
        self.hl = QHBoxLayout(self)
        self.hl.setObjectName(_fromUtf8("horizontalLayout"))
        self.cb = QComboBox(self)
        self.cb.setObjectName(_fromUtf8("comboBox"))
        self.cb.addItems(QStringList(["Project Folder", "Versioned Folder"]))
        self.hl.addWidget(self.cb)
        self.le = QLineEdit(self)
        self.le.setObjectName(_fromUtf8("lineEdit"))
        self.hl.addWidget(self.le)
        self.bb = QDialogButtonBox(self)
        self.bb.setOrientation(Qt.Vertical)
        self.bb.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.bb.setObjectName(_fromUtf8("buttonBox"))
        self.hl.addWidget(self.bb)
        self.setModal(True)
        self.setWindowTitle(QApplication.translate("New Folder", "", None, QApplication.UnicodeUTF8))
        QObject.connect(self.bb, SIGNAL(_fromUtf8("accepted()")), self.accept)
        QObject.connect(self.bb, SIGNAL(_fromUtf8("rejected()")), self.reject)
        QMetaObject.connectSlotsByName(self)
    
    def getNewFolder(self):
        self.cb.setCurrentIndex(0)
        self.le.setText("NewFolder")
        self.le.selectAll()
        if self.exec_() == 1:
            folderType = self.cb.currentIndex()
            folderName = str(self.le.text())
            return [folderType, folderName]
        else:
            return [None, None]

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self._MainWindow = MainWindow
        
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(900, 654)
        icon = QIcon()
        icon.addPixmap(QPixmap(_fromUtf8(os.path.join("..","resources","PNG_Files","Network","Disconnected.PNG"))), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.mainWidget = QWidget(MainWindow)
        self.mainWidget.setObjectName(_fromUtf8("mainWidget"))
        self.horizontalLayout = QHBoxLayout(self.mainWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        
        #Tree Widgets and Tabs
        self.fileTabs = QTabWidget(self.mainWidget)
        self.fileTabs.setObjectName(_fromUtf8("fileTabs"))
        self.localFilesTab = QWidget()
        self.localFilesTab.setObjectName(_fromUtf8("localFilesTab"))
        self.verticalLayout_2 = QVBoxLayout(self.localFilesTab)
        self.verticalLayout_2.setMargin(5)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.localFilesTreeWidget = QTreeWidget(self.localFilesTab)
        self.localFilesTreeWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.localFilesTreeWidget.setObjectName(_fromUtf8("localFilesTreeWidget"))
        self.localFilesTreeWidget.header().setDefaultSectionSize(200)
        self.localFilesTreeWidget.setIndentation(12)
        self.verticalLayout_2.addWidget(self.localFilesTreeWidget)
        self.fileTabs.addTab(self.localFilesTab, _fromUtf8(""))
        
        self.projectFilesTab = QWidget()
        self.projectFilesTab.setObjectName(_fromUtf8("projectFilesTab"))
        self.verticalLayout = QVBoxLayout(self.projectFilesTab)
        self.verticalLayout.setMargin(5)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        #self.projectFilesTreeWidget = QTreeWidget(self.projectFilesTab)
        self.projectFilesTreeWidget = DeselectableTreeWidget(self.projectFilesTab)
        self.projectFilesTreeWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.projectFilesTreeWidget.setObjectName(_fromUtf8("projectFilesTreeWidget"))
        self.projectFilesTreeWidget.header().setDefaultSectionSize(120)
        self.projectFilesTreeWidget.setIndentation(12)
        self.verticalLayout.addWidget(self.projectFilesTreeWidget)
        self.fileTabs.addTab(self.projectFilesTab, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.fileTabs)
        
        # Status Bar
        MainWindow.setCentralWidget(self.mainWidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        
        # Tool Bar
        self.toolbar = QToolBar(MainWindow)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolbar.sizePolicy().hasHeightForWidth())
        self.toolbar.setSizePolicy(sizePolicy)
        self.toolbar.setContextMenuPolicy(Qt.NoContextMenu)
        self.toolbar.setAllowedAreas(Qt.AllToolBarAreas)
        self.toolbar.setIconSize(QSize(48, 48))
        self.toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.toolbar.setObjectName(_fromUtf8("toolbar"))
        MainWindow.addToolBar(Qt.RightToolBarArea, self.toolbar)
        
        # Define Actions
        self.actionSettings = QAction(MainWindow)
        icon1 = QIcon()
        icon1.addPixmap(QPixmap(_fromUtf8(os.path.join("..","resources","PNG_Files","Hardware","Computer.PNG"))), QIcon.Normal, QIcon.Off)
        self.actionSettings.setIcon(icon1)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        
        self.actionCheckout = QAction(MainWindow)
        self.actionCheckout.setEnabled(True)
        icon2 = QIcon()
        icon2.addPixmap(QPixmap(_fromUtf8(os.path.join("..","resources","PNG_Files","Misc","Download.PNG"))), QIcon.Normal, QIcon.Off)
        self.actionCheckout.setIcon(icon2)
        self.actionCheckout.setObjectName(_fromUtf8("actionCheckout"))
        
        self.actionCheckin = QAction(MainWindow)
        icon3 = QIcon()
        icon3.addPixmap(QPixmap(_fromUtf8(os.path.join("..","resources","PNG_Files","Misc","Upload.PNG"))), QIcon.Normal, QIcon.Off)		
        self.actionCheckin.setIcon(icon3)
        self.actionCheckin.setObjectName(_fromUtf8("actionCheckin"))
        
        self.actionCache_to_Alembic = QAction(MainWindow)
        icon4 = QIcon()
        icon4.addPixmap(QPixmap(_fromUtf8(os.path.join("..","resources","PNG_Files","Misc","alembic_logo_Darkest.png"))), QIcon.Normal, QIcon.Off)
        self.actionCache_to_Alembic.setIcon(icon4)
        self.actionCache_to_Alembic.setObjectName(_fromUtf8("actionCache_to_Alembic"))
        
        self.actionInstall = QAction(MainWindow)
        icon5 = QIcon()
        icon5.addPixmap(QPixmap(_fromUtf8(os.path.join("..","resources","PNG_Files","Folders","Favourites.PNG"))), QIcon.Normal, QIcon.Off)
        self.actionInstall.setIcon(icon5)
        self.actionInstall.setObjectName(_fromUtf8("actionInstall"))
        
        self.actionUpdate_Plugins = QAction(MainWindow)
        icon6 = QIcon()
        icon6.addPixmap(QPixmap(_fromUtf8(os.path.join("..","resources","PNG_Files","Misc","Search.PNG"))), QIcon.Normal, QIcon.Off)
        self.actionUpdate_Plugins.setIcon(icon6)
        self.actionUpdate_Plugins.setObjectName(_fromUtf8("actionUpdate_Plugins"))
        
        self.actionOpen_File = QAction(MainWindow)
        icon7 = QIcon()
        icon7.addPixmap(QPixmap(_fromUtf8(os.path.join("..","resources","PNG_Files","File_Formats","format.PNG"))), QIcon.Normal, QIcon.Off)
        self.actionOpen_File.setIcon(icon7)
        self.actionOpen_File.setObjectName(_fromUtf8("actionOpen_File"))
        
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        
        self.actionRename = QAction(MainWindow)
        self.actionRename.setObjectName(_fromUtf8("actionRename"))
        
        self.actionRemove = QAction(MainWindow)
        self.actionRemove.setObjectName(_fromUtf8("actionRemove"))
        
        # Add Actions to Tool Bar
        self.toolbar.addAction(self.actionCheckout)
        self.toolbar.addAction(self.actionInstall)
        self.toolbar.addAction(self.actionCache_to_Alembic)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.actionCheckin)
        self.toolbar.addAction(self.actionOpen_File)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.actionUpdate_Plugins)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.actionSettings)
        
        # Housekeeping...
        self.retranslateUi(MainWindow)
        self.fileTabs.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(MainWindow)
        
        # Popup Menus
        self.localPopMenu = QMenu(MainWindow)
        self.localPopMenu.addAction(self.actionCheckin)
        self.localPopMenu.addSeparator()
        self.localPopMenu.addAction(self.actionOpen_File)
        
        self.projectPopMenu = QMenu(MainWindow)
        self.projectPopMenu.addAction(self.actionCheckout)
        self.projectPopMenu.addAction(self.actionInstall)
        self.projectPopMenu.addSeparator()
        self.projectPopMenu.addAction(self.actionNew)
        self.projectPopMenu.addAction(self.actionRename)
        self.projectPopMenu.addAction(self.actionRemove)
        
        # Dialog Menus
        ## File Dialog
        self.file_select_dialog = FileSelectDialog(MainWindow)
        self.file_select_dialog.setup()
        
        ## Error Message
        self.errorMessage = QErrorMessage(MainWindow)
        
        ## Message Box
        self.messageBox = QMessageBox(MainWindow)
        
        ## Setup Directory Dialog
        self.setupDirsDialog = QFileDialog(MainWindow)
        
        ## New Folder Dialog
        self.newFolderDialog = NewFolderDialog(MainWindow)
        self.newFolderDialog.setup()
    
    def retranslateUi(self, MainWindow):
        #Set Titles
        MainWindow.setWindowTitle(QApplication.translate("MainWindow", "Chasm Project Utility", None, QApplication.UnicodeUTF8))
        self.localFilesTreeWidget.headerItem().setText(0, QApplication.translate("MainWindow", "File Name", None, QApplication.UnicodeUTF8))
        self.localFilesTreeWidget.headerItem().setText(1, QApplication.translate("MainWindow", "Check Out Time", None, QApplication.UnicodeUTF8))
        self.localFilesTreeWidget.headerItem().setText(2, QApplication.translate("MainWindow", "Last Opened", None, QApplication.UnicodeUTF8))
        self.fileTabs.setTabText(self.fileTabs.indexOf(self.localFilesTab), QApplication.translate("MainWindow", "My Checked Out Files", None, QApplication.UnicodeUTF8))
        
        #Set Section Sizes
        #self.projectFilesTreeWidget.setStyleSheet("QTreeView::item{border-right: 1px solid #d9d9d9;border-bottom: 1px solid #d9d9d9;}")
        self.projectFilesTreeWidget.headerItem().setText(0, QApplication.translate("MainWindow", "File Name", None, QApplication.UnicodeUTF8))
        self.projectFilesTreeWidget.headerItem().setText(1, QApplication.translate("MainWindow", "Locked", None, QApplication.UnicodeUTF8))
        self.projectFilesTreeWidget.headerItem().setText(2, QApplication.translate("MainWindow", "Checked In by:", None, QApplication.UnicodeUTF8))
        self.projectFilesTreeWidget.headerItem().setText(3, QApplication.translate("MainWindow", "Check In Time:", None, QApplication.UnicodeUTF8))
        self.projectFilesTreeWidget.headerItem().setText(4, QApplication.translate("MainWindow", "Ready", None, QApplication.UnicodeUTF8))
        self.projectFilesTreeWidget.headerItem().setText(5, QApplication.translate("MainWindow", "File Reference:", None, QApplication.UnicodeUTF8))
        self.projectFilesTreeWidget.header().resizeSection(0, 200)
        self.projectFilesTreeWidget.header().resizeSection(1, 60)
        self.projectFilesTreeWidget.header().resizeSection(2, 120)
        self.projectFilesTreeWidget.header().resizeSection(3, 140)
        self.projectFilesTreeWidget.header().resizeSection(4, 50)
        self.projectFilesTreeWidget.header().resizeSection(5, 200)
        self.fileTabs.setTabText(self.fileTabs.indexOf(self.projectFilesTab), QApplication.translate("MainWindow", "ProjectFiles", None, QApplication.UnicodeUTF8))
        
        #Set Actions Text
        self.toolbar.setWindowTitle(QApplication.translate("MainWindow", "Tool Bar", None, QApplication.UnicodeUTF8))
        self.actionSettings.setText(QApplication.translate("MainWindow", "Settings", None, QApplication.UnicodeUTF8))
        self.actionSettings.setToolTip(QApplication.translate("MainWindow", "Configure Your Settings", None, QApplication.UnicodeUTF8))
        self.actionCheckout.setText(QApplication.translate("MainWindow", "Checkout", None, QApplication.UnicodeUTF8))
        self.actionCheckout.setToolTip(QApplication.translate("MainWindow", "Checkout Project File", None, QApplication.UnicodeUTF8))
        self.actionCheckin.setText(QApplication.translate("MainWindow", "Checkin", None, QApplication.UnicodeUTF8))
        self.actionCheckin.setToolTip(QApplication.translate("MainWindow", "Checkin a Local File", None, QApplication.UnicodeUTF8))
        self.actionCache_to_Alembic.setText(QApplication.translate("MainWindow", "Alembic", None, QApplication.UnicodeUTF8))
        self.actionInstall.setText(QApplication.translate("MainWindow", "Install", None, QApplication.UnicodeUTF8))
        self.actionInstall.setToolTip(QApplication.translate("MainWindow", "Install / Flatten a File", None, QApplication.UnicodeUTF8))
        self.actionUpdate_Plugins.setText(QApplication.translate("MainWindow", "Update Plugins", None, QApplication.UnicodeUTF8))
        self.actionUpdate_Plugins.setToolTip(QApplication.translate("MainWindow", "Update Project Plugins", None, QApplication.UnicodeUTF8))
        self.actionOpen_File.setText(QApplication.translate("MainWindow", "Open File", None, QApplication.UnicodeUTF8))
        self.actionOpen_File.setToolTip(QApplication.translate("MainWindow", "Open a Local or Project File in Maya or Houdini", None, QApplication.UnicodeUTF8))
        
        self.actionNew.setText(QApplication.translate("MainWindow", "New", None, QApplication.UnicodeUTF8))
        self.actionNew.setToolTip(QApplication.translate("MainWindow", "Create a new folder, asset, or shot.", None, QApplication.UnicodeUTF8))
        self.actionRename.setText(QApplication.translate("MainWindow", "Rename", None, QApplication.UnicodeUTF8))
        self.actionRename.setToolTip(QApplication.translate("MainWindow", "Rename this folder", None, QApplication.UnicodeUTF8))
        self.actionRemove.setText(QApplication.translate("MainWindow", "Remove", None, QApplication.UnicodeUTF8))
        self.actionRemove.setToolTip(QApplication.translate("MainWindow", "Remove this folder and its contents", None, QApplication.UnicodeUTF8))
    
    def connectSignalsAndSlots(self, MainWindow):
        # Action calls
        QObject.connect(self.actionCache_to_Alembic, SIGNAL("triggered()"), controller.runAlembic)
        QObject.connect(self.actionCheckout, SIGNAL("triggered()"), self.checkout)
        QObject.connect(self.actionCheckin, SIGNAL("triggered()"), self.checkin)
        QObject.connect(self.actionInstall, SIGNAL("triggered()"), self.install)
        QObject.connect(self.actionOpen_File, SIGNAL("triggered()"), self.openFile)
        QObject.connect(self.actionSettings, SIGNAL("triggered()"), controller.runSettings)
        QObject.connect(self.actionUpdate_Plugins, SIGNAL("triggered()"), controller.runUpdatePlugins)
        QObject.connect(self.actionNew, SIGNAL("triggered()"), self.newFolder)
        QObject.connect(self.actionRename, SIGNAL("triggered()"), controller.runRename)
        QObject.connect(self.actionRemove, SIGNAL("triggered()"), controller.runRemove)
        
        # Tabs
        QObject.connect(self.fileTabs, SIGNAL("currentChanged(int)"), self.tabSwitch)
        
        # File Selection Widgets
        QObject.connect(self.localFilesTreeWidget, SIGNAL("itemSelectionChanged()"), self.localItemSelectionChanged)
        QObject.connect(self.localFilesTreeWidget, SIGNAL("customContextMenuRequested(QPoint)"), self.localFilesContextMenu)
        QObject.connect(self.projectFilesTreeWidget, SIGNAL("itemSelectionChanged()"), self.projectItemSelectionChanged)
        QObject.connect(self.projectFilesTreeWidget, SIGNAL("customContextMenuRequested(QPoint)"), self.projectFilesContextMenu)
    
    def checkout(self):
        controller.runCheckout(self)
    
    def checkin(self):
        controller.runCheckin(self)
    
    def install(self):
        controller.runInstall(self)
    
    def openFile(self):
        controller.runOpen(self)
    
    def newFolder(self):
        controller.runNew(self)
    
    def tabSwitch(self, tabNum):
        controller.tabSwitch(self, tabNum)
    
    def localItemSelectionChanged(self):
        controller.localItemSelectionChanged(self)
    
    def projectItemSelectionChanged(self):
        controller.projectItemSelectionChanged(self)
    
    def localFilesContextMenu(self, point):
        controller.localFilesContextMenu(self, point)
    
    def projectFilesContextMenu(self, point):
        controller.projectFilesContextMenu(self, point)
    
    def getTreeItemPath(self, treeItem, path):
        if not type(treeItem.parent()) == types.NoneType:
            path = self.getTreeItemPath(treeItem.parent(), path)
        
        path = os.path.join(path, str(treeItem.text(0)))
        return path


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    ui.connectSignalsAndSlots(MainWindow)
    
    #Create in Memory model Project - looking for .config.ini
    controller.setup(ui)
    
    MainWindow.show()
    sys.exit(app.exec_())