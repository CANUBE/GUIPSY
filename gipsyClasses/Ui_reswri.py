# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reswri.ui'
#
# Created: Thu Apr 25 11:00:39 2013
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_reswri(object):
    def setupUi(self, reswri):
        reswri.setObjectName("reswri")
        reswri.resize(662, 590)
        reswri.setFrameShape(QtGui.QFrame.NoFrame)
        reswri.setFrameShadow(QtGui.QFrame.Raised)
        self.verticalLayout = QtGui.QVBoxLayout(reswri)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtGui.QFrame(reswri)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtGui.QGridLayout(self.frame)
        self.gridLayout_2.setMargin(9)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.HIBoxButton = QtGui.QPushButton(self.frame)
        self.HIBoxButton.setObjectName("HIBoxButton")
        self.gridLayout_2.addWidget(self.HIBoxButton, 1, 0, 1, 1)
        self.HISetButton = QtGui.QPushButton(self.frame)
        self.HISetButton.setObjectName("HISetButton")
        self.gridLayout_2.addWidget(self.HISetButton, 0, 0, 1, 1)
        self.HISetHeaderButton = QtGui.QPushButton(self.frame)
        self.HISetHeaderButton.setObjectName("HISetHeaderButton")
        self.gridLayout_2.addWidget(self.HISetHeaderButton, 0, 2, 1, 1)
        self.HISetLabel = QtGui.QLabel(self.frame)
        self.HISetLabel.setText("")
        self.HISetLabel.setObjectName("HISetLabel")
        self.gridLayout_2.addWidget(self.HISetLabel, 0, 1, 1, 1)
        self.HIBoxLabel = QtGui.QLabel(self.frame)
        self.HIBoxLabel.setText("")
        self.HIBoxLabel.setObjectName("HIBoxLabel")
        self.gridLayout_2.addWidget(self.HIBoxLabel, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtGui.QFrame(reswri)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtGui.QGridLayout(self.frame_2)
        self.gridLayout.setMargin(9)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtGui.QLabel(self.frame_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.bunitLine = QtGui.QLineEdit(self.frame_2)
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
        self.gridLayout.addWidget(self.radiiButton, 3, 4, 1, 1)
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
        self.gridLayout.addWidget(self.widthsButton, 5, 4, 1, 1)
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
        self.gridLayout.addWidget(self.vexpButton, 7, 4, 1, 1)
        self.vexpCheck = QtGui.QCheckBox(self.frame_2)
        self.vexpCheck.setObjectName("vexpCheck")
        self.gridLayout.addWidget(self.vexpCheck, 7, 5, 1, 1)
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
        self.gridLayout.addWidget(self.paButton, 8, 4, 1, 1)
        self.paCheck = QtGui.QCheckBox(self.frame_2)
        self.paCheck.setObjectName("paCheck")
        self.gridLayout.addWidget(self.paCheck, 8, 5, 1, 1)
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
        self.gridLayout.addWidget(self.inclButton, 9, 4, 1, 1)
        self.inclCheck = QtGui.QCheckBox(self.frame_2)
        self.inclCheck.setObjectName("inclCheck")
        self.gridLayout.addWidget(self.inclCheck, 9, 5, 1, 1)
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
        self.gridLayout.addWidget(self.fittoleranceLine, 10, 4, 1, 1)
        self.label_15 = QtGui.QLabel(self.frame_2)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 12, 0, 1, 3)
        self.kinematicLine = QtGui.QLineEdit(self.frame_2)
        self.kinematicLine.setObjectName("kinematicLine")
        self.gridLayout.addWidget(self.kinematicLine, 12, 3, 1, 2)
        self.kinematicButton = QtGui.QPushButton(self.frame_2)
        self.kinematicButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/fileopen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kinematicButton.setIcon(icon1)
        self.kinematicButton.setIconSize(QtCore.QSize(20, 20))
        self.kinematicButton.setObjectName("kinematicButton")
        self.gridLayout.addWidget(self.kinematicButton, 12, 5, 1, 1)
        self.surfaceLabel = QtGui.QLabel(self.frame_2)
        self.surfaceLabel.setEnabled(False)
        self.surfaceLabel.setObjectName("surfaceLabel")
        self.gridLayout.addWidget(self.surfaceLabel, 13, 0, 1, 3)
        self.surfaceLine = QtGui.QLineEdit(self.frame_2)
        self.surfaceLine.setEnabled(False)
        self.surfaceLine.setObjectName("surfaceLine")
        self.gridLayout.addWidget(self.surfaceLine, 13, 3, 1, 2)
        self.surfaceButton = QtGui.QPushButton(self.frame_2)
        self.surfaceButton.setEnabled(False)
        self.surfaceButton.setText("")
        self.surfaceButton.setIcon(icon1)
        self.surfaceButton.setIconSize(QtCore.QSize(20, 20))
        self.surfaceButton.setObjectName("surfaceButton")
        self.gridLayout.addWidget(self.surfaceButton, 13, 5, 1, 1)
        self.saveParamsButton = QtGui.QPushButton(self.frame_2)
        self.saveParamsButton.setObjectName("saveParamsButton")
        self.gridLayout.addWidget(self.saveParamsButton, 14, 0, 1, 1)
        self.loadParamsButton = QtGui.QPushButton(self.frame_2)
        self.loadParamsButton.setObjectName("loadParamsButton")
        self.gridLayout.addWidget(self.loadParamsButton, 14, 1, 1, 1)
        self.label_16 = QtGui.QLabel(self.frame_2)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 11, 3, 1, 1)
        self.fitorderLine = QtGui.QLineEdit(self.frame_2)
        self.fitorderLine.setObjectName("fitorderLine")
        self.gridLayout.addWidget(self.fitorderLine, 11, 4, 1, 1)
        self.frame_3 = QtGui.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_3.setLineWidth(0)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.xcentreLine = QtGui.QLineEdit(self.frame_3)
        self.xcentreLine.setMaximumSize(QtCore.QSize(60, 16777215))
        self.xcentreLine.setObjectName("xcentreLine")
        self.horizontalLayout.addWidget(self.xcentreLine)
        self.ycentreLine = QtGui.QLineEdit(self.frame_3)
        self.ycentreLine.setMaximumSize(QtCore.QSize(60, 16777215))
        self.ycentreLine.setObjectName("ycentreLine")
        self.horizontalLayout.addWidget(self.ycentreLine)
        self.gridLayout.addWidget(self.frame_3, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.frame_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.vrotLine = QtGui.QLineEdit(self.frame_2)
        self.vrotLine.setObjectName("vrotLine")
        self.gridLayout.addWidget(self.vrotLine, 4, 1, 1, 3)
        self.vrotButton = QtGui.QPushButton(self.frame_2)
        self.vrotButton.setText("")
        self.vrotButton.setIcon(icon)
        self.vrotButton.setIconSize(QtCore.QSize(20, 20))
        self.vrotButton.setObjectName("vrotButton")
        self.gridLayout.addWidget(self.vrotButton, 4, 4, 1, 1)
        self.vrotCheck = QtGui.QCheckBox(self.frame_2)
        self.vrotCheck.setObjectName("vrotCheck")
        self.gridLayout.addWidget(self.vrotCheck, 4, 5, 1, 1)
        self.checkSampCentre = QtGui.QCheckBox(self.frame_2)
        self.checkSampCentre.setEnabled(False)
        self.checkSampCentre.setStyleSheet("QCheckBox { color: green }")
        self.checkSampCentre.setChecked(True)
        self.checkSampCentre.setObjectName("checkSampCentre")
        self.gridLayout.addWidget(self.checkSampCentre, 1, 4, 1, 1)
        self.checkSampVsys = QtGui.QCheckBox(self.frame_2)
        self.checkSampVsys.setEnabled(False)
        self.checkSampVsys.setStyleSheet("QCheckBox { color: green }")
        self.checkSampVsys.setObjectName("checkSampVsys")
        self.gridLayout.addWidget(self.checkSampVsys, 2, 4, 1, 1)
        self.checkSampVrot = QtGui.QCheckBox(self.frame_2)
        self.checkSampVrot.setEnabled(False)
        self.checkSampVrot.setStyleSheet("QCheckBox { color: green }")
        self.checkSampVrot.setObjectName("checkSampVrot")
        self.gridLayout.addWidget(self.checkSampVrot, 4, 6, 1, 1)
        self.checkSampRadii = QtGui.QCheckBox(self.frame_2)
        self.checkSampRadii.setEnabled(False)
        self.checkSampRadii.setStyleSheet("QCheckBox { color: green }")
        self.checkSampRadii.setObjectName("checkSampRadii")
        self.gridLayout.addWidget(self.checkSampRadii, 3, 5, 1, 1)
        self.sideBox = QtGui.QComboBox(self.frame_2)
        self.sideBox.setObjectName("sideBox")
        self.sideBox.addItem("")
        self.sideBox.addItem("")
        self.sideBox.addItem("")
        self.gridLayout.addWidget(self.sideBox, 0, 5, 1, 1)
        self.label_6 = QtGui.QLabel(self.frame_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 4, 1, 1)
        self.verticalLayout.addWidget(self.frame_2)

        self.retranslateUi(reswri)
        QtCore.QMetaObject.connectSlotsByName(reswri)

    def retranslateUi(self, reswri):
        reswri.setWindowTitle(QtGui.QApplication.translate("reswri", "Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.HIBoxButton.setText(QtGui.QApplication.translate("reswri", "BOX", None, QtGui.QApplication.UnicodeUTF8))
        self.HISetButton.setText(QtGui.QApplication.translate("reswri", "HI", None, QtGui.QApplication.UnicodeUTF8))
        self.HISetHeaderButton.setText(QtGui.QApplication.translate("reswri", "HEADER", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("reswri", "BUNIT", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("reswri", "CENTRE", None, QtGui.QApplication.UnicodeUTF8))
        self.centreCheck.setText(QtGui.QApplication.translate("reswri", "Fixed", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("reswri", "VSYS", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("reswri", "KM/S", None, QtGui.QApplication.UnicodeUTF8))
        self.vsysCheck.setText(QtGui.QApplication.translate("reswri", "Fixed", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("reswri", "RADII", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("reswri", "WIDTHS", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("reswri", "VEXP", None, QtGui.QApplication.UnicodeUTF8))
        self.vexpCheck.setText(QtGui.QApplication.translate("reswri", "Fixed", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("reswri", "PA", None, QtGui.QApplication.UnicodeUTF8))
        self.paCheck.setText(QtGui.QApplication.translate("reswri", "Fixed", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("reswri", "INCL", None, QtGui.QApplication.UnicodeUTF8))
        self.inclCheck.setText(QtGui.QApplication.translate("reswri", "Fixed", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("reswri", "FREEANGLE", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("reswri", "DEG", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("reswri", "FIT TOLERANCE", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("reswri", "Kinematic harmonic coefficients", None, QtGui.QApplication.UnicodeUTF8))
        self.surfaceLabel.setText(QtGui.QApplication.translate("reswri", "Surface density harmonic coefficients", None, QtGui.QApplication.UnicodeUTF8))
        self.saveParamsButton.setText(QtGui.QApplication.translate("reswri", "SAVE PARAMS", None, QtGui.QApplication.UnicodeUTF8))
        self.loadParamsButton.setText(QtGui.QApplication.translate("reswri", "LOAD PARAMS", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("reswri", "FIT ORDER", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("reswri", "VROT", None, QtGui.QApplication.UnicodeUTF8))
        self.vrotCheck.setText(QtGui.QApplication.translate("reswri", "Fixed", None, QtGui.QApplication.UnicodeUTF8))
        self.checkSampCentre.setText(QtGui.QApplication.translate("reswri", "SAMP", None, QtGui.QApplication.UnicodeUTF8))
        self.checkSampVsys.setText(QtGui.QApplication.translate("reswri", "SAMP", None, QtGui.QApplication.UnicodeUTF8))
        self.checkSampVrot.setText(QtGui.QApplication.translate("reswri", "SAMP", None, QtGui.QApplication.UnicodeUTF8))
        self.checkSampRadii.setText(QtGui.QApplication.translate("reswri", "SAMP", None, QtGui.QApplication.UnicodeUTF8))
        self.sideBox.setItemText(0, QtGui.QApplication.translate("reswri", "Both", None, QtGui.QApplication.UnicodeUTF8))
        self.sideBox.setItemText(1, QtGui.QApplication.translate("reswri", "Approaching", None, QtGui.QApplication.UnicodeUTF8))
        self.sideBox.setItemText(2, QtGui.QApplication.translate("reswri", "Receding", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("reswri", "SIDE", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc