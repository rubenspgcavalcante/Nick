# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'views/chat.ui'
#
# Created: Mon May 28 23:29:28 2012
#      by: PyQt4 UI code generator 4.9.1
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
        MainWindow.resize(449, 387)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(20, 8, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.chatInput = QtGui.QTextEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chatInput.sizePolicy().hasHeightForWidth())
        self.chatInput.setSizePolicy(sizePolicy)
        self.chatInput.setMaximumSize(QtCore.QSize(16777215, 64))
        self.chatInput.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.chatInput.setObjectName(_fromUtf8("chatInput"))
        self.gridLayout.addWidget(self.chatInput, 3, 0, 1, 1)
        self.chatHistory = QtWebKit.QWebView(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chatHistory.sizePolicy().hasHeightForWidth())
        self.chatHistory.setSizePolicy(sizePolicy)
        self.chatHistory.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.chatHistory.setObjectName(_fromUtf8("chatHistory"))
        self.gridLayout.addWidget(self.chatHistory, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 449, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuContacts = QtGui.QMenu(self.menubar)
        self.menuContacts.setObjectName(_fromUtf8("menuContacts"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionConect = QtGui.QAction(MainWindow)
        self.actionConect.setObjectName(_fromUtf8("actionConect"))
        self.menuContacts.addAction(self.actionConect)
        self.menuContacts.addSeparator()
        self.menubar.addAction(self.menuContacts.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.menuContacts.setTitle(QtGui.QApplication.translate("MainWindow", "Contacts", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConect.setText(QtGui.QApplication.translate("MainWindow", "Conect", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
