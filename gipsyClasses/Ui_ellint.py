# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ellint.ui'
#
# Created: Thu Apr 25 10:58:18 2013
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ellint(object):
    def setupUi(self, ellint):
        ellint.setObjectName("ellint")
        ellint.resize(719, 450)
        ellint.setFrameShape(QtGui.QFrame.StyledPanel)
        ellint.setFrameShadow(QtGui.QFrame.Raised)
        self.gridLayout = QtGui.QGridLayout(ellint)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtGui.QLabel(ellint)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_8 = QtGui.QLabel(ellint)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)
        self.radiiLine = QtGui.QLineEdit(ellint)
        self.radiiLine.setObjectName("radiiLine")
        self.gridLayout.addWidget(self.radiiLine, 3, 1, 1, 4)
        self.label_9 = QtGui.QLabel(ellint)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 1)
        self.widthLine = QtGui.QLineEdit(ellint)
        self.widthLine.setObjectName("widthLine")
        self.gridLayout.addWidget(self.widthLine, 4, 1, 1, 4)
        self.label_10 = QtGui.QLabel(ellint)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 5, 0, 1, 1)
        self.paLine = QtGui.QLineEdit(ellint)
        self.paLine.setObjectName("paLine")
        self.gridLayout.addWidget(self.paLine, 5, 1, 1, 4)
        self.label_11 = QtGui.QLabel(ellint)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 6, 0, 1, 1)
        self.inclLine = QtGui.QLineEdit(ellint)
        self.inclLine.setObjectName("inclLine")
        self.gridLayout.addWidget(self.inclLine, 6, 1, 1, 4)
        self.loadParamsButton = QtGui.QPushButton(ellint)
        self.loadParamsButton.setObjectName("loadParamsButton")
        self.gridLayout.addWidget(self.loadParamsButton, 10, 1, 1, 1)
        self.label_3 = QtGui.QLabel(ellint)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_5 = QtGui.QLabel(ellint)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.optionBox = QtGui.QComboBox(ellint)
        self.optionBox.setObjectName("optionBox")
        self.optionBox.addItem("")
        self.optionBox.addItem("")
        self.optionBox.addItem("")
        self.gridLayout.addWidget(self.optionBox, 2, 1, 1, 2)
        self.label_6 = QtGui.QLabel(ellint)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 3, 1, 1)
        self.orderBox = QtGui.QComboBox(ellint)
        self.orderBox.setObjectName("orderBox")
        self.orderBox.addItem("")
        self.orderBox.addItem("")
        self.gridLayout.addWidget(self.orderBox, 2, 4, 1, 2)
        self.widthButton = QtGui.QPushButton(ellint)
        self.widthButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/table.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.widthButton.setIcon(icon)
        self.widthButton.setIconSize(QtCore.QSize(20, 20))
        self.widthButton.setObjectName("widthButton")
        self.gridLayout.addWidget(self.widthButton, 4, 5, 1, 1)
        self.paButton = QtGui.QPushButton(ellint)
        self.paButton.setText("")
        self.paButton.setIcon(icon)
        self.paButton.setIconSize(QtCore.QSize(20, 20))
        self.paButton.setObjectName("paButton")
        self.gridLayout.addWidget(self.paButton, 5, 5, 1, 1)
        self.inclButton = QtGui.QPushButton(ellint)
        self.inclButton.setText("")
        self.inclButton.setIcon(icon)
        self.inclButton.setIconSize(QtCore.QSize(20, 20))
        self.inclButton.setObjectName("inclButton")
        self.gridLayout.addWidget(self.inclButton, 6, 5, 1, 1)
        self.radiiButton = QtGui.QPushButton(ellint)
        self.radiiButton.setText("")
        self.radiiButton.setIcon(icon)
        self.radiiButton.setIconSize(QtCore.QSize(20, 20))
        self.radiiButton.setObjectName("radiiButton")
        self.gridLayout.addWidget(self.radiiButton, 3, 5, 1, 1)
        self.label = QtGui.QLabel(ellint)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 7, 0, 1, 1)
        self.massLabel = QtGui.QLabel(ellint)
        self.massLabel.setEnabled(False)
        self.massLabel.setObjectName("massLabel")
        self.gridLayout.addWidget(self.massLabel, 8, 0, 1, 1)
        self.massLine = QtGui.QLineEdit(ellint)
        self.massLine.setEnabled(False)
        self.massLine.setMaximumSize(QtCore.QSize(100, 16777215))
        self.massLine.setObjectName("massLine")
        self.gridLayout.addWidget(self.massLine, 8, 1, 1, 1)
        self.distanceLabel = QtGui.QLabel(ellint)
        self.distanceLabel.setEnabled(False)
        self.distanceLabel.setObjectName("distanceLabel")
        self.gridLayout.addWidget(self.distanceLabel, 9, 0, 1, 1)
        self.saveParamsButton = QtGui.QPushButton(ellint)
        self.saveParamsButton.setObjectName("saveParamsButton")
        self.gridLayout.addWidget(self.saveParamsButton, 10, 0, 1, 1)
        self.moLabel = QtGui.QLabel(ellint)
        self.moLabel.setEnabled(False)
        self.moLabel.setObjectName("moLabel")
        self.gridLayout.addWidget(self.moLabel, 8, 2, 1, 1)
        self.distanceLine = QtGui.QLineEdit(ellint)
        self.distanceLine.setEnabled(False)
        self.distanceLine.setMaximumSize(QtCore.QSize(100, 16777215))
        self.distanceLine.setObjectName("distanceLine")
        self.gridLayout.addWidget(self.distanceLine, 9, 1, 1, 1)
        self.mpcLabel = QtGui.QLabel(ellint)
        self.mpcLabel.setEnabled(False)
        self.mpcLabel.setObjectName("mpcLabel")
        self.gridLayout.addWidget(self.mpcLabel, 9, 2, 1, 1)
        self.label_15 = QtGui.QLabel(ellint)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 8, 3, 1, 1)
        self.xsubpixLine = QtGui.QLineEdit(ellint)
        self.xsubpixLine.setMaximumSize(QtCore.QSize(75, 16777215))
        self.xsubpixLine.setObjectName("xsubpixLine")
        self.gridLayout.addWidget(self.xsubpixLine, 8, 4, 1, 1)
        self.ysubpixLine = QtGui.QLineEdit(ellint)
        self.ysubpixLine.setMaximumSize(QtCore.QSize(75, 16777215))
        self.ysubpixLine.setObjectName("ysubpixLine")
        self.gridLayout.addWidget(self.ysubpixLine, 8, 5, 1, 1)
        self.overlapCheck = QtGui.QCheckBox(ellint)
        self.overlapCheck.setChecked(True)
        self.overlapCheck.setObjectName("overlapCheck")
        self.gridLayout.addWidget(self.overlapCheck, 9, 3, 1, 1)
        self.segmentList = QtGui.QListWidget(ellint)
        self.segmentList.setObjectName("segmentList")
        QtGui.QListWidgetItem(self.segmentList)
        item = QtGui.QListWidgetItem(self.segmentList)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.gridLayout.addWidget(self.segmentList, 7, 1, 1, 4)
        self.rangeLabel = QtGui.QLabel(ellint)
        self.rangeLabel.setEnabled(False)
        self.rangeLabel.setText("")
        self.rangeLabel.setObjectName("rangeLabel")
        self.gridLayout.addWidget(self.rangeLabel, 1, 3, 1, 1)
        self.xrangeLine = QtGui.QLineEdit(ellint)
        self.xrangeLine.setEnabled(False)
        self.xrangeLine.setMinimumSize(QtCore.QSize(125, 0))
        self.xrangeLine.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.xrangeLine.setObjectName("xrangeLine")
        self.gridLayout.addWidget(self.xrangeLine, 1, 1, 1, 1)
        self.xcentreLine = QtGui.QLineEdit(ellint)
        self.xcentreLine.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.xcentreLine.setObjectName("xcentreLine")
        self.gridLayout.addWidget(self.xcentreLine, 0, 1, 1, 1)
        self.ycentreLine = QtGui.QLineEdit(ellint)
        self.ycentreLine.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ycentreLine.setObjectName("ycentreLine")
        self.gridLayout.addWidget(self.ycentreLine, 0, 2, 1, 1)
        self.yrangeLine = QtGui.QLineEdit(ellint)
        self.yrangeLine.setEnabled(False)
        self.yrangeLine.setMinimumSize(QtCore.QSize(125, 0))
        self.yrangeLine.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.yrangeLine.setObjectName("yrangeLine")
        self.gridLayout.addWidget(self.yrangeLine, 1, 2, 1, 1)
        self.checkSampCentre = QtGui.QCheckBox(ellint)
        self.checkSampCentre.setEnabled(False)
        self.checkSampCentre.setStyleSheet("QCheckBox { color: green }")
        self.checkSampCentre.setChecked(True)
        self.checkSampCentre.setObjectName("checkSampCentre")
        self.gridLayout.addWidget(self.checkSampCentre, 0, 3, 1, 1)
        self.checkSampRadii = QtGui.QCheckBox(ellint)
        self.checkSampRadii.setEnabled(False)
        self.checkSampRadii.setStyleSheet("QCheckBox { color: green }")
        self.checkSampRadii.setObjectName("checkSampRadii")
        self.gridLayout.addWidget(self.checkSampRadii, 3, 6, 1, 1)

        self.retranslateUi(ellint)
        QtCore.QMetaObject.connectSlotsByName(ellint)

    def retranslateUi(self, ellint):
        ellint.setWindowTitle(QtGui.QApplication.translate("ellint", "Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ellint", "CENTRE", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("ellint", "RADII", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("ellint", "WIDTH", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("ellint", "PA", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("ellint", "INCL", None, QtGui.QApplication.UnicodeUTF8))
        self.loadParamsButton.setText(QtGui.QApplication.translate("ellint", "LOAD PARAMS", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ellint", "RANGE", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ellint", "OPTION", None, QtGui.QApplication.UnicodeUTF8))
        self.optionBox.setItemText(0, QtGui.QApplication.translate("ellint", "Stats", None, QtGui.QApplication.UnicodeUTF8))
        self.optionBox.setItemText(1, QtGui.QApplication.translate("ellint", "Surface brightness", None, QtGui.QApplication.UnicodeUTF8))
        self.optionBox.setItemText(2, QtGui.QApplication.translate("ellint", "Mass surface density", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("ellint", "ORDER", None, QtGui.QApplication.UnicodeUTF8))
        self.orderBox.setItemText(0, QtGui.QApplication.translate("ellint", "Segments in rings", None, QtGui.QApplication.UnicodeUTF8))
        self.orderBox.setItemText(1, QtGui.QApplication.translate("ellint", "Rings in segments", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ellint", "SEGMENTS", None, QtGui.QApplication.UnicodeUTF8))
        self.massLabel.setText(QtGui.QApplication.translate("ellint", "MASS", None, QtGui.QApplication.UnicodeUTF8))
        self.distanceLabel.setText(QtGui.QApplication.translate("ellint", "DISTANCE", None, QtGui.QApplication.UnicodeUTF8))
        self.saveParamsButton.setText(QtGui.QApplication.translate("ellint", "SAVE PARAMS", None, QtGui.QApplication.UnicodeUTF8))
        self.moLabel.setText(QtGui.QApplication.translate("ellint", "Mo", None, QtGui.QApplication.UnicodeUTF8))
        self.mpcLabel.setText(QtGui.QApplication.translate("ellint", "Mpc", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("ellint", "SUBPIX", None, QtGui.QApplication.UnicodeUTF8))
        self.overlapCheck.setText(QtGui.QApplication.translate("ellint", "OVERLAP", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.segmentList.isSortingEnabled()
        self.segmentList.setSortingEnabled(False)
        self.segmentList.item(0).setText(QtGui.QApplication.translate("ellint", "0 360", None, QtGui.QApplication.UnicodeUTF8))
        self.segmentList.setSortingEnabled(__sortingEnabled)
        self.checkSampCentre.setText(QtGui.QApplication.translate("ellint", "SAMP", None, QtGui.QApplication.UnicodeUTF8))
        self.checkSampRadii.setText(QtGui.QApplication.translate("ellint", "SAMP", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
