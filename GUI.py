# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created: Thu Apr 26 01:01:32 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Chasm Project Utility", None, QtGui.QApplication.UnicodeUTF8))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/chasm/ICO_Files/Network/Disconnected.ICO")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setIconSize(QtCore.QSize(48, 48))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.RightToolBarArea, self.toolBar)
        self.actionSettings = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/chasm/ICO_Files/Hardware/Computer.ICO")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettings.setIcon(icon1)
        self.actionSettings.setText(QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setToolTip(QtGui.QApplication.translate("MainWindow", "Configure Your Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionCheckout = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/chasm/ICO_Files/Misc/Download.ICO")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCheckout.setIcon(icon2)
        self.actionCheckout.setText(QtGui.QApplication.translate("MainWindow", "Checkout", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCheckout.setToolTip(QtGui.QApplication.translate("MainWindow", "Checkout Project File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCheckout.setObjectName(_fromUtf8("actionCheckout"))
        self.actionCheckin = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/chasm/ICO_Files/Misc/Upload.ICO")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCheckin.setIcon(icon3)
        self.actionCheckin.setText(QtGui.QApplication.translate("MainWindow", "Checkin", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCheckin.setToolTip(QtGui.QApplication.translate("MainWindow", "Checkin a Local File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCheckin.setObjectName(_fromUtf8("actionCheckin"))
        self.actionCache_to_Alembic = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/chasm/ICO_Files/Misc/Favourites.ICO")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCache_to_Alembic.setIcon(icon4)
        self.actionCache_to_Alembic.setText(QtGui.QApplication.translate("MainWindow", "Cache to Alembic", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCache_to_Alembic.setObjectName(_fromUtf8("actionCache_to_Alembic"))
        self.actionInstall = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/chasm/ICO_Files/Folders/Favourites.ICO")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInstall.setIcon(icon5)
        self.actionInstall.setText(QtGui.QApplication.translate("MainWindow", "Install", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInstall.setToolTip(QtGui.QApplication.translate("MainWindow", "Install / Flatten a File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInstall.setObjectName(_fromUtf8("actionInstall"))
        self.actionUpdate_Plugins = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/chasm/ICO_Files/Misc/Search.ICO")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUpdate_Plugins.setIcon(icon6)
        self.actionUpdate_Plugins.setText(QtGui.QApplication.translate("MainWindow", "Update Plugins", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpdate_Plugins.setToolTip(QtGui.QApplication.translate("MainWindow", "Update Project Plugins", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpdate_Plugins.setObjectName(_fromUtf8("actionUpdate_Plugins"))
        self.toolBar.addAction(self.actionSettings)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCheckout)
        self.toolBar.addAction(self.actionCheckin)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionInstall)
        self.toolBar.addAction(self.actionCache_to_Alembic)
        self.toolBar.addAction(self.actionUpdate_Plugins)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        pass

import chasm_resources_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

