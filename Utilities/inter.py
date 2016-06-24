# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Mon Mar 21 07:13:39 2016
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Music Composer"))
        Dialog.resize(768, 479)
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(90, 10, 591, 111))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(230, 20, 102, 28))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(200, 70, 171, 20))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.frame_2 = QtGui.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(90, 140, 181, 161))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.pushButton_2 = QtGui.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 100, 121, 41))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_2 = QtGui.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 69, 18))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.frame_3 = QtGui.QFrame(Dialog)
        self.frame_3.setGeometry(QtCore.QRect(280, 140, 201, 161))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.pushButton_3 = QtGui.QPushButton(self.frame_3)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 100, 121, 41))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.label_3 = QtGui.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 161, 18))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.frame_4 = QtGui.QFrame(Dialog)
        self.frame_4.setGeometry(QtCore.QRect(490, 140, 191, 161))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.pushButton_4 = QtGui.QPushButton(self.frame_4)
        self.pushButton_4.setGeometry(QtCore.QRect(40, 100, 121, 41))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.label_4 = QtGui.QLabel(self.frame_4)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 161, 18))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.frame_5 = QtGui.QFrame(Dialog)
        self.frame_5.setGeometry(QtCore.QRect(90, 320, 591, 80))
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.label = QtGui.QLabel(self.frame_5)
        self.label.setGeometry(QtCore.QRect(70, 30, 430, 30))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton_5 = QtGui.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(330, 430, 102, 28))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton.setText(_translate("Dialog", "Choose File", None))
        self.label_5.setText(_translate("Dialog", "Selected File", None))
        self.pushButton_2.setText(_translate("Dialog", "Play file", None))
        self.label_2.setText(_translate("Dialog", "Play file", None))
        self.pushButton_3.setText(_translate("Dialog", "Compare", None))
        self.label_3.setText(_translate("Dialog", "Select and compare", None))
        self.pushButton_4.setText(_translate("Dialog", "Merge", None))
        self.label_4.setText(_translate("Dialog", "Select a file to merge ", None))
        self.label.setText(_translate("Dialog", "Output", None))
        self.pushButton_5.setText(_translate("Dialog", "Exit", None))

