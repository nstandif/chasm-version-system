# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI2.ui'
#
# Created: Mon May  7 16:38:31 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import controller

try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

def test():
    print "This was run."

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(900, 654)
        icon = QIcon()
        icon.addPixmap(QPixmap(_fromUtf8("../resources/PNG_Files/Network/Disconnected.PNG")), QIcon.Normal, QIcon.Off)
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
        self.projectFilesTreeWidget = QTreeWidget(self.projectFilesTab)
        self.projectFilesTreeWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.projectFilesTreeWidget.setObjectName(_fromUtf8("projectFilesTreeWidget"))
        self.projectFilesTreeWidget.header().setDefaultSectionSize(120)
        self.projectFilesTreeWidget.setIndentation(12)
        self.verticalLayout.addWidget(self.projectFilesTreeWidget)
        self.fileTabs.addTab(self.projectFilesTab, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.fileTabs)
        
        MainWindow.setCentralWidget(self.mainWidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
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
        self.actionSettings = QAction(MainWindow)
        icon1 = QIcon()
        icon1.addPixmap(QPixmap(_fromUtf8("../resources/PNG_Files/Hardware/Computer.PNG")), QIcon.Normal, QIcon.Off)
        self.actionSettings.setIcon(icon1)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionCheckout = QAction(MainWindow)
        self.actionCheckout.setEnabled(True)
        icon2 = QIcon()
        icon2.addPixmap(QPixmap(_fromUtf8("../resources/PNG_Files/Misc/Download.PNG")), QIcon.Normal, QIcon.Off)
        self.actionCheckout.setIcon(icon2)
        self.actionCheckout.setObjectName(_fromUtf8("actionCheckout"))
        self.actionCheckin = QAction(MainWindow)
        icon3 = QIcon()
        icon3.addPixmap(QPixmap(_fromUtf8("../resources/PNG_Files/Misc/Upload.PNG")), QIcon.Normal, QIcon.Off)
        self.actionCheckin.setIcon(icon3)
        self.actionCheckin.setObjectName(_fromUtf8("actionCheckin"))
        self.actionCache_to_Alembic = QAction(MainWindow)
        icon4 = QIcon()
        icon4.addPixmap(QPixmap(_fromUtf8("../resources/PNG_Files/Misc/alembic_logo_Darkest.png")), QIcon.Normal, QIcon.Off)
        self.actionCache_to_Alembic.setIcon(icon4)
        self.actionCache_to_Alembic.setObjectName(_fromUtf8("actionCache_to_Alembic"))
        self.actionInstall = QAction(MainWindow)
        icon5 = QIcon()
        icon5.addPixmap(QPixmap(_fromUtf8("../resources/PNG_Files/Folders/Favourites.PNG")), QIcon.Normal, QIcon.Off)
        self.actionInstall.setIcon(icon5)
        self.actionInstall.setObjectName(_fromUtf8("actionInstall"))
        self.actionUpdate_Plugins = QAction(MainWindow)
        icon6 = QIcon()
        icon6.addPixmap(QPixmap(_fromUtf8("../resources/PNG_Files/Misc/Search.PNG")), QIcon.Normal, QIcon.Off)
        self.actionUpdate_Plugins.setIcon(icon6)
        self.actionUpdate_Plugins.setObjectName(_fromUtf8("actionUpdate_Plugins"))
        self.actionOpen_File = QAction(MainWindow)
        icon7 = QIcon()
        icon7.addPixmap(QPixmap(_fromUtf8("../resources/PNG_Files/File_Formats/format.PNG")), QIcon.Normal, QIcon.Off)
        self.actionOpen_File.setIcon(icon7)
        self.actionOpen_File.setObjectName(_fromUtf8("actionOpen_File"))
        self.toolbar.addAction(self.actionCheckout)
        self.toolbar.addAction(self.actionInstall)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.actionCheckin)
        self.toolbar.addAction(self.actionOpen_File)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.actionCache_to_Alembic)
        self.toolbar.addAction(self.actionUpdate_Plugins)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.actionSettings)

        self.retranslateUi(MainWindow)
        self.fileTabs.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QApplication.translate("MainWindow", "Chasm Project Utility", None, QApplication.UnicodeUTF8))
        self.localFilesTreeWidget.headerItem().setText(0, QApplication.translate("MainWindow", "File Name", None, QApplication.UnicodeUTF8))
        self.localFilesTreeWidget.headerItem().setText(1, QApplication.translate("MainWindow", "Check Out Time", None, QApplication.UnicodeUTF8))
        self.localFilesTreeWidget.headerItem().setText(2, QApplication.translate("MainWindow", "Last Opened", None, QApplication.UnicodeUTF8))
        self.fileTabs.setTabText(self.fileTabs.indexOf(self.localFilesTab), QApplication.translate("MainWindow", "My Checked Out Files", None, QApplication.UnicodeUTF8))
        
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
    
    def populateLocalTree(self, MainWindow):
        pass
    
    def populateProjectTree(self, MainWindow):
        root = QTreeWidgetItem(ui.projectFilesTreeWidget)
        root.setText(0, "Chasm")
        assetItem = QTreeWidgetItem(root)
        assetItem.setText(0, "assets")
        enviroItem = QTreeWidgetItem(assetItem)
        enviroItem.setText(0, "environment")
        cliffItem = QTreeWidgetItem(enviroItem)
        cliffItem.setText(0, "cliff_face")
        cliffItem.setText(1, "No")
        cliffItem.setText(2, "Morgan Strong")
        cliffItem.setText(3, "Thu, 28 Jun 2001 4:20:00 PM")
        cliffItem.setText(4, "Yes")
        cliffItem.setText(5, "/grp5/Chasm/assets/environment/cliff_face/inst/stable")
        pass
    
    def connectSignalsAndSlots(self, MainWindow):
        # Toolbar
        QObject.connect(self.actionCache_to_Alembic, SIGNAL("triggered()"), controller.runAlembic)
        QObject.connect(self.actionCheckout, SIGNAL("triggered()"), controller.runCheckout)
        QObject.connect(self.actionCheckin, SIGNAL("triggered()"), controller.runCheckin)
        QObject.connect(self.actionInstall, SIGNAL("triggered()"), controller.runInstall)
        QObject.connect(self.actionOpen_File, SIGNAL("triggered()"), controller.runOpen)
        QObject.connect(self.actionSettings, SIGNAL("triggered()"), controller.runSettings)
        QObject.connect(self.actionUpdate_Plugins, SIGNAL("triggered()"), controller.runUpdatePlugins)
        
        # Tabs
        QObject.connect(self.fileTabs, SIGNAL("currentChanged(int)"), controller.tabSwitch)
        
        # File Selection Widgets
        QObject.connect(self.localFilesTreeWidget, SIGNAL("itemSelectionChanged()"), controller.localItemSelectionChanged)
        QObject.connect(self.localFilesTreeWidget, SIGNAL("customContextMenuRequested(QPoint)"), controller.localFilesContextMenu)
        QObject.connect(self.projectFilesTreeWidget, SIGNAL("itemSelectionChanged()"), controller.projectItemSelectionChanged)
        QObject.connect(self.projectFilesTreeWidget, SIGNAL("customContextMenuRequested(QPoint)"), controller.projectFilesContextMenu)
        
    
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    ui.connectSignalsAndSlots(MainWindow)
    
    #Create in Memory model Project - looking for .config.ini
    
    ui.populateLocalTree(MainWindow)
    ui.populateProjectTree(MainWindow)
    
    MainWindow.show()
    sys.exit(app.exec_())

