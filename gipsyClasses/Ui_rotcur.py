# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rotcur.ui'
#
# Created: Thu Apr 25 11:01:28 2013
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_rotcur(object):
    def setupUi(self, rotcur):
        rotcur.setObjectName("rotcur")
        rotcur.resize(626, 573)
        rotcur.setFrameShape(QtGui.QFrame.NoFrame)
        rotcur.setFrameShadow(QtGui.QFrame.Raised)
        self.verticalLayout = QtGui.QVBoxLayout(rotcur)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtGui.QFrame(rotcur)
        self.frame_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtGui.QGridLayout(self.frame_2)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtGui.QLabel(self.frame_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.bunitLine = QtGui.QLineEdit(self.frame_2)
        self.bunitLine.setMaximumSize(QtCore.QSize(70, 16777215))
        self.bunitLine.setObjectName("bunitLine")
        self.gridLayout.addWidget(self.bunitLine, 0, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.frame_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.centreCheck = QtGui.QCheckBox(self.frame_2)
        self.centreCheck.setObjectName("centreCheck")
        self.gridLayout.addWidget(self.centreCheck, 1, 3, 1, 1)
        self.label_5 = QtGui.QLabel(self.frame_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.vsysLine = QtGui.QLineEdit(self.frame_2)
        self.vsysLine.setObjectName("vsysLine")
        self.gridLayout.addWidget(self.vsysLine, 2, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.frame_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 2, 1, 1)
        self.vsysCheck = QtGui.QCheckBox(self.frame_2)
        self.vsysCheck.setObjectName("vsysCheck")
        self.gridLayout.addWidget(self.vsysCheck, 2, 3, 1, 1)
        self.label_8 = QtGui.QLabel(self.frame_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)
        self.radiiLine = QtGui.QLineEdit(self.frame_2)
        self.radiiLine.setObjectName("radiiLine")
        self.gridLayout.addWidget(self.radiiLine, 3, 1, 1, 3)
        self.radiiButton = QtGui.QPushButton(self.frame_2)
        self.radiiButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/table.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radiiButton.setIcon(icon)
        self.radiiButton.setIconSize(QtCore.QSize(20, 20))
        self.radiiButton.setObjectName("radiiButton")
        self.gridLayout.addWidget(self.radiiButton, 3, 5, 1, 1)
        self.label = QtGui.QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 5, 0, 1, 1)
        self.widthsLine = QtGui.QLineEdit(self.frame_2)
        self.widthsLine.setObjectName("widthsLine")
        self.gridLayout.addWidget(self.widthsLine, 5, 1, 1, 3)
        self.widthsButton = QtGui.QPushButton(self.frame_2)
        self.widthsButton.setText("")
        self.widthsButton.setIcon(icon)
        self.widthsButton.setIconSize(QtCore.QSize(20, 20))
        self.widthsButton.setObjectName("widthsButton")
        self.gridLayout.addWidget(self.widthsButton, 5, 5, 1, 1)
        self.label_9 = QtGui.QLabel(self.frame_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 7, 0, 1, 1)
        self.vexpLine = QtGui.QLineEdit(self.frame_2)
        self.vexpLine.setObjectName("vexpLine")
        self.gridLayout.addWidget(self.vexpLine, 7, 1, 1, 3)
        self.vexpButton = QtGui.QPushButton(self.frame_2)
        self.vexpButton.setText("")
        self.vexpButton.setIcon(icon)
        self.vexpButton.setIconSize(QtCore.QSize(20, 20))
        self.vexpButton.setObjectName("vexpButton")
        self.gridLayout.addWidget(self.vexpButton, 7, 5, 1, 1)
        self.vexpCheck = QtGui.QCheckBox(self.frame_2)
        self.vexpCheck.setObjectName("vexpCheck")
        self.gridLayout.addWidget(self.vexpCheck, 7, 6, 1, 1)
        self.label_10 = QtGui.QLabel(self.frame_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 8, 0, 1, 1)
        self.paLine = QtGui.QLineEdit(self.frame_2)
        self.paLine.setObjectName("paLine")
        self.gridLayout.addWidget(self.paLine, 8, 1, 1, 3)
        self.paButton = QtGui.QPushButton(self.frame_2)
        self.paButton.setText("")
        self.paButton.setIcon(icon)
        self.paButton.setIconSize(QtCore.QSize(20, 20))
        self.paButton.setObjectName("paButton")
        self.gridLayout.addWidget(self.paButton, 8, 5, 1, 1)
        self.paCheck = QtGui.QCheckBox(self.frame_2)
        self.paCheck.setObjectName("paCheck")
        self.gridLayout.addWidget(self.paCheck, 8, 6, 1, 1)
        self.label_11 = QtGui.QLabel(self.frame_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 9, 0, 1, 1)
        self.inclLine = QtGui.QLineEdit(self.frame_2)
        self.inclLine.setObjectName("inclLine")
        self.gridLayout.addWidget(self.inclLine, 9, 1, 1, 3)
        self.inclButton = QtGui.QPushButton(self.frame_2)
        self.inclButton.setText("")
        self.inclButton.setIcon(icon)
        self.inclButton.setIconSize(QtCore.QSize(20, 20))
        self.inclButton.setObjectName("inclButton")
        self.gridLayout.addWidget(self.inclButton, 9, 5, 1, 1)
        self.inclCheck = QtGui.QCheckBox(self.frame_2)
        self.inclCheck.setObjectName("inclCheck")
        self.gridLayout.addWidget(self.inclCheck, 9, 6, 1, 1)
        self.label_12 = QtGui.QLabel(self.frame_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 10, 0, 1, 1)
        self.freeangleLine = QtGui.QLineEdit(self.frame_2)
        self.freeangleLine.setObjectName("freeangleLine")
        self.gridLayout.addWidget(self.freeangleLine, 10, 1, 1, 1)
        self.label_13 = QtGui.QLabel(self.frame_2)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 10, 2, 1, 1)
        self.label_14 = QtGui.QLabel(self.frame_2)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 10, 3, 1, 1)
        self.fittoleranceLine = QtGui.QLineEdit(self.frame_2)
        self.fittoleranceLine.setObjectName("fittoleranceLine")
        self.gridLayout.addWidget(self.fittoleranceLine, 10, 5, 1, 1)
        self.saveParamsButton = QtGui.QPushButton(self.frame_2)
        self.saveParamsButton.setObjectName("saveParamsButton")
        self.gridLayout.addWidget(self.saveParamsButton, 12, 0, 1, 1)
        self.loadParamsButton = QtGui.QPushButton(self.frame_2)
        self.loadParamsButton.setObjectName("loadParamsButton")
        self.gridLayout.addWidget(self.loadParamsButton, 12, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.frame_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)
        self.label_15 = QtGui.QLabel(self.frame_2)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 11, 0, 1, 1)
        self.weightBox = QtGui.QComboBox(self.frame_2)
        self.weightBox.setObjectName("weightBox")
        self.weightBox.addItem("")
        self.weightBox.addItem("")
        self.weightBox.addItem("")
        self.gridLayout.addWidget(self.weightBox, 11, 1, 1, 1)
        self.sideBox = QtGui.QComboBox(self.frame_2)
        self.sideBox.setObjectName("sideBox")
        self.sideBox.addItem("")
        self.sideBox.addItem("")
        self.sideBox.addItem("")
        self.gridLayout.addWidget(self.sideBox, 0, 3, 1, 1)
        self.frame = QtGui.QFrame(self.frame_2)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Plain)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.xcentreLine = QtGui.QLineEdit(self.frame)
        self.xcentreLine.setMaximumSize(QtCore.QSize(60, 16777215))
        self.xcentreLine.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.xcentreLine.setObjectName("xcentreLine")
        self.horizontalLayout.addWidget(self.xcentreLine)
        self.ycentreLine = QtGui.QLineEdit(self.frame)
        self.ycentreLine.setMinimumSize(QtCore.QSize(60, 0))
        self.ycentreLine.setMaximumSize(QtCore.QSize(60, 16777215))
        self.ycentreLine.setObjectName("ycentreLine")
        self.horizontalLayout.addWidget(self.ycentreLine)
        self.gridLayout.addWidget(self.frame, 1, 1, 1, 1)
        self.checkSampCentre = QtGui.QCheckBox(self.frame_2)
        self.checkSampCentre.setEnabled(False)
        self.checkSampCentre.setStyleSheet("QCheckBox { color: green }")
        self.checkSampCentre.setChecked(True)
        self.checkSampCentre.setObjectName("checkSampCentre")
        self.gridLayout.addWidget(self.checkSampCentre, 1, 5, 1, 1)
        self.checkSampVsys = QtGui.QCheckBox(self.frame_2)
        self.checkSampVsys.setEnabled(False)
        self.checkSampVsys.setStyleSheet("QCheckBox { color: green }")
        self.checkSampVsys.setChecked(True)
        self.checkSampVsys.setObjectName("checkSampVsys")
        self.gridLayout.addWidget(self.checkSampVsys, 2, 5, 1, 1)
        self.checkSampRadii = QtGui.QCheckBox(self.frame_2)
        self.checkSampRadii.setEnabled(False)
        self.checkSampRadii.setStyleSheet("QCheckBox { color: green }")
        self.checkSampRadii.setObjectName("checkSampRadii")
        self.gridLayout.addWidget(self.checkSampRadii, 3, 6, 1, 1)
        self.vrotLine = QtGui.QLineEdit(self.frame_2)
        self.vrotLine.setObjectName("vrotLine")
        self.gridLayout.addWidget(self.vrotLine, 4, 1, 1, 3)
        self.label_2 = QtGui.QLabel(self.frame_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.vrotButton = QtGui.QPushButton(self.frame_2)
        self.vrotButton.setText("")
        self.vrotButton.setIcon(icon)
        self.vrotButton.setIconSize(QtCore.QSize(20, 20))
        self.vrotButton.setObjectName("vrotButton")
        self.gridLayout.addWidget(self.vrotButton, 4, 5, 1, 1)
        self.vrotCheck = QtGui.QCheckBox(self.frame_2)
        self.vrotCheck.setObjectName("vrotCheck")
        self.gridLayout.addWidget(self.vrotCheck, 4, 6, 1, 1)
        self.checkSampVrot = QtGui.QCheckBox(self.frame_2)
        self.checkSampVrot.setEnabled(False)
        self.checkSampVrot.setToolTip("")
        self.checkSampVrot.setWhatsThis("")
        self.checkSampVrot.setStyleSheet("QCheckBox { color: green }")
        self.checkSampVrot.setObjectName("checkSampVrot")
        self.gridLayout.addWidget(self.checkSampVrot, 4, 7, 1, 1)
        self.verticalLayout.addWidget(self.frame_2)

        self.retranslateUi(rotcur)
        QtCore.QMetaObject.connectSlotsByName(rotcur)

    def retranslateUi(self, rotcur):
        rotcur.setWindowTitle(QtGui.QApplication.translate("rotcur", "Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("rotcur", "BUNIT", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("rotcur", "CENTRE", None, QtGui.QApplication.UnicodeUTF8))
        self.centreCheck.setText(QtGui.QApplication.translate("rotcur", "Fixed", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("rotcur", "VSYS", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("rotcur", "KM/S", None, QtGui.QApplication.UnicodeUTF8))
        self.vsysCheck.setText(QtGui.QApplication.translate("rotcur", "Fixed", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("rotcur", "RADII", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("rotcur", "WIDTHS", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("rotcur", "VEXP", None, QtGui.QApplication.UnicodeUTF8))
        self.vexpCheck.setText(QtGui.QApplication.translate("rotcur", "Fixed", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("rotcur", "PA", None, QtGui.QApplication.UnicodeUTF8))
        self.paCheck.setText(QtGui.QApplication.translate("rotcur", "Fixed", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("rotcur", "INCL", None, QtGui.QApplication.UnicodeUTF8))
        self.inclCheck.setText(QtGui.QApplication.translate("rotcur", "Fixed", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("rotcur", "FREEANGLE", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("rotcur", "DEG", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("rotcur", "FIT TOLERANCE", None, QtGui.QApplication.UnicodeUTF8))
        self.saveParamsButton.setText(QtGui.QApplication.translate("rotcur", "SAVE PARAMS", None, QtGui.QApplication.UnicodeUTF8))
        self.loadParamsButton.setText(QtGui.QApplication.translate("rotcur", "LOAD PARAMS", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("rotcur", "SIDE", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("rotcur", "WEIGHT", None, QtGui.QApplication.UnicodeUTF8))
        self.weightBox.setItemText(0, QtGui.QApplication.translate("rotcur", "COSINE", None, QtGui.QApplication.UnicodeUTF8))
        self.weightBox.setItemText(1, QtGui.QApplication.translate("rotcur", "UNIFORM", None, QtGui.QApplication.UnicodeUTF8))
        self.weightBox.setItemText(2, QtGui.QApplication.translate("rotcur", "COS-SQUARED", None, QtGui.QApplication.UnicodeUTF8))
        self.sideBox.setItemText(0, QtGui.QApplication.translate("rotcur", "Both", None, QtGui.QApplication.UnicodeUTF8))
        self.sideBox.setItemText(1, QtGui.QApplication.translate("rotcur", "Approaching", None, QtGui.QApplication.UnicodeUTF8))
        self.sideBox.setItemText(2, QtGui.QApplication.translate("rotcur", "Receding", None, QtGui.QApplication.UnicodeUTF8))
        self.checkSampCentre.setText(QtGui.QApplication.translate("rotcur", "SAMP", None, QtGui.QApplication.UnicodeUTF8))
        self.checkSampVsys.setText(QtGui.QApplication.translate("rotcur", "SAMP", None, QtGui.QApplication.UnicodeUTF8))
        self.checkSampRadii.setText(QtGui.QApplication.translate("rotcur", "SAMP", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("rotcur", "VROT", None, QtGui.QApplication.UnicodeUTF8))
        self.vrotCheck.setText(QtGui.QApplication.translate("rotcur", "Fixed", None, QtGui.QApplication.UnicodeUTF8))
        self.checkSampVrot.setText(QtGui.QApplication.translate("rotcur", "SAMP", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
