# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'slice.ui'
#
# Created: Thu Jul 21 12:56:44 2011
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_slice(object):
    def setupUi(self, slice):
        slice.setObjectName("slice")
        slice.resize(400, 445)
        slice.setFrameShape(QtGui.QFrame.StyledPanel)
        slice.setFrameShadow(QtGui.QFrame.Raised)
        self.verticalLayout = QtGui.QVBoxLayout(slice)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_2 = QtGui.QGroupBox(slice)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.xposLine = QtGui.QLineEdit(self.groupBox_2)
        self.xposLine.setMaximumSize(QtCore.QSize(75, 16777215))
        self.xposLine.setObjectName("xposLine")
        self.gridLayout.addWidget(self.xposLine, 0, 1, 1, 1)
        self.yposLine = QtGui.QLineEdit(self.groupBox_2)
        self.yposLine.setMaximumSize(QtCore.QSize(75, 16777215))
        self.yposLine.setObjectName("yposLine")
        self.gridLayout.addWidget(self.yposLine, 0, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.angleLine = QtGui.QLineEdit(self.groupBox_2)
        self.angleLine.setMaximumSize(QtCore.QSize(75, 16777215))
        self.angleLine.setObjectName("angleLine")
        self.gridLayout.addWidget(self.angleLine, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.pointsLine = QtGui.QLineEdit(self.groupBox_2)
        self.pointsLine.setMaximumSize(QtCore.QSize(75, 16777215))
        self.pointsLine.setObjectName("pointsLine")
        self.gridLayout.addWidget(self.pointsLine, 2, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox = QtGui.QGroupBox(slice)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.gridoutLine = QtGui.QLineEdit(self.groupBox)
        self.gridoutLine.setObjectName("gridoutLine")
        self.gridLayout_2.addWidget(self.gridoutLine, 0, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)
        self.upslicesLine = QtGui.QLineEdit(self.groupBox)
        self.upslicesLine.setObjectName("upslicesLine")
        self.gridLayout_2.addWidget(self.upslicesLine, 1, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 2, 1, 1)
        self.downslicesLine = QtGui.QLineEdit(self.groupBox)
        self.downslicesLine.setObjectName("downslicesLine")
        self.gridLayout_2.addWidget(self.downslicesLine, 1, 3, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)
        self.spaceLine = QtGui.QLineEdit(self.groupBox)
        self.spaceLine.setObjectName("spaceLine")
        self.gridLayout_2.addWidget(self.spaceLine, 2, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(slice)
        QtCore.QMetaObject.connectSlotsByName(slice)

    def retranslateUi(self, slice):
        slice.setWindowTitle(QtGui.QApplication.translate("slice", "Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("slice", "Line", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("slice", "POSITION", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("slice", "ANGLE", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("slice", "DEG", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("slice", "POINTS", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("slice", "Output Options", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("slice", "GRIDOUT", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("slice", "UP SLICES", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("slice", "DOWN SLICES", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("slice", "SPACE", None, QtGui.QApplication.UnicodeUTF8))

