# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CarSetup.ui'
#
# Created: Fri Jan 23 12:11:23 2015
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 270)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        self.btnOk = QtGui.QPushButton(Form)
        self.btnOk.setGeometry(QtCore.QRect(290, 240, 91, 23))
        self.btnOk.setObjectName(_fromUtf8("btnOk"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 381, 221))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 131, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 150, 131, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.motoA_CK = QtGui.QLabel(self.groupBox)
        self.motoA_CK.setGeometry(QtCore.QRect(180, 70, 51, 51))
        self.motoA_CK.setStyleSheet(_fromUtf8("     border: 1px solid rgb(67,67,67);\n"
"     border-radius: 4px;"))
        self.motoA_CK.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/stepping_motor-clockwise.png")))
        self.motoA_CK.setObjectName(_fromUtf8("motoA_CK"))
        self.motoB_CK = QtGui.QLabel(self.groupBox)
        self.motoB_CK.setGeometry(QtCore.QRect(180, 130, 51, 51))
        self.motoB_CK.setStyleSheet(_fromUtf8("     border: 1px solid rgb(67,67,67);\n"
"     border-radius: 4px;"))
        self.motoB_CK.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/stepping_motor-clockwise.png")))
        self.motoB_CK.setObjectName(_fromUtf8("motoB_CK"))
        self.motoA_CCK = QtGui.QLabel(self.groupBox)
        self.motoA_CCK.setGeometry(QtCore.QRect(270, 70, 51, 51))
        self.motoA_CCK.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/stepping_motor-anticlockwise.png")))
        self.motoA_CCK.setObjectName(_fromUtf8("motoA_CCK"))
        self.motoB_CCK = QtGui.QLabel(self.groupBox)
        self.motoB_CCK.setGeometry(QtCore.QRect(270, 130, 51, 51))
        self.motoB_CCK.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/stepping_motor-anticlockwise.png")))
        self.motoB_CCK.setObjectName(_fromUtf8("motoB_CCK"))
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(350, 10, 24, 24))
        self.pushButton.setStyleSheet(_fromUtf8(" QPushButton {\n"
"    border-image: url(:/images/help-icon.png) 0;\n"
" }\n"
"\n"
" QPushButton:hover {\n"
"    border-image: url(:/images/help-icon-hover.png) 0;\n"
" }\n"
"\n"
" QPushButton:pressed  {\n"
"    border-image: url(:/images/help-icon-click.png) 0;\n"
" }\n"
""))
        self.pushButton.setText(_fromUtf8(""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(170, 190, 71, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(260, 190, 101, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(20, 30, 151, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.lineScale = QtGui.QLineEdit(self.groupBox)
        self.lineScale.setGeometry(QtCore.QRect(180, 30, 113, 20))
        self.lineScale.setObjectName(_fromUtf8("lineScale"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.btnOk.setText(_translate("Form", "Ok", None))
        self.groupBox.setTitle(_translate("Form", "Car Setups", None))
        self.label_3.setText(_translate("Form", "Stepper A Directoin:", None))
        self.label_4.setText(_translate("Form", "Stepper B Directoin:", None))
        self.label_5.setText(_translate("Form", "ClockWise", None))
        self.label_6.setText(_translate("Form", "Anti ClockWise", None))
        self.label_7.setText(_translate("Form", "Scaler :", None))

import images_rc