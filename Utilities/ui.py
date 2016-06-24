# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new.ui'
#
# Created: Thu Mar 31 00:54:01 2016
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.filelistWidget = QtGui.QListWidget(self.centralwidget)
        self.filelistWidget.setGeometry(QtCore.QRect(30, 40, 291, 261))
        self.filelistWidget.setObjectName(_fromUtf8("filelistWidget"))
        self.Seletedlist = QtGui.QListWidget(self.centralwidget)
        self.Seletedlist.setGeometry(QtCore.QRect(450, 40, 261, 261))
        self.Seletedlist.setObjectName(_fromUtf8("Seletedlist"))
        self.compareBtn = QtGui.QPushButton(self.centralwidget)
        self.compareBtn.setGeometry(QtCore.QRect(450, 320, 102, 28))
        self.compareBtn.setObjectName(_fromUtf8("compareBtn"))
        self.MergeBtn = QtGui.QPushButton(self.centralwidget)
        self.MergeBtn.setGeometry(QtCore.QRect(560, 320, 102, 28))
        self.MergeBtn.setObjectName(_fromUtf8("MergeBtn"))
        self.addBtn = QtGui.QPushButton(self.centralwidget)
        self.addBtn.setGeometry(QtCore.QRect(360, 140, 61, 51))
        self.addBtn.setObjectName(_fromUtf8("addBtn"))
        self.playButton = QtGui.QPushButton(self.centralwidget)
        self.playButton.setGeometry(QtCore.QRect(70, 320, 102, 28))
        self.playButton.setObjectName(_fromUtf8("playButton"))
        self.folderBtn = QtGui.QPushButton(self.centralwidget)
        self.folderBtn.setGeometry(QtCore.QRect(120, 0, 102, 28))
        self.folderBtn.setObjectName(_fromUtf8("folderBtn"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(670, 320, 41, 28))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.outputView = QtGui.QTextBrowser(self.centralwidget)
        self.outputView.setGeometry(QtCore.QRect(30, 360, 681, 192))
        self.outputView.setObjectName(_fromUtf8("outputView"))
        self.stop = QtGui.QPushButton(self.centralwidget)
        self.stop.setGeometry(QtCore.QRect(190, 320, 102, 28))
        self.stop.setObjectName(_fromUtf8("stop"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.compareBtn.setText(_translate("MainWindow", "Compare", None))
        self.MergeBtn.setText(_translate("MainWindow", "Merge", None))
        self.addBtn.setText(_translate("MainWindow", ">>", None))
        self.playButton.setText(_translate("MainWindow", "play", None))
        self.folderBtn.setText(_translate("MainWindow", "Select folder", None))
        self.pushButton.setText(_translate("MainWindow", "x", None))
        self.stop.setText(_translate("MainWindow", "stop", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))

