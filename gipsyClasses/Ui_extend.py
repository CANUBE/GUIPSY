# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'extend.ui'
#
# Created: Wed Nov  9 13:48:08 2011
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_extend(object):
    def setupUi(self, extend):
        extend.setObjectName("extend")
        extend.resize(425, 431)
        extend.setFrameShape(QtGui.QFrame.NoFrame)
        extend.setFrameShadow(QtGui.QFrame.Raised)
        self.gridLayout = QtGui.QGridLayout(extend)
        self.gridLayout.setObjectName("gridLayout")
        self.ctypeLabel = QtGui.QLabel(extend)
        self.ctypeLabel.setObjectName("ctypeLabel")
        self.gridLayout.addWidget(self.ctypeLabel, 0, 0, 1, 1)
        self.ctypeBox = QtGui.QComboBox(extend)
        self.ctypeBox.setObjectName("ctypeBox")
        self.gridLayout.addWidget(self.ctypeBox, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(172, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.naxisLabel = QtGui.QLabel(extend)
        self.naxisLabel.setObjectName("naxisLabel")
        self.gridLayout.addWidget(self.naxisLabel, 1, 0, 1, 1)
        self.naxisLine = QtGui.QLineEdit(extend)
        self.naxisLine.setObjectName("naxisLine")
        self.gridLayout.addWidget(self.naxisLine, 1, 1, 1, 1)
        self.crpixLabel = QtGui.QLabel(extend)
        self.crpixLabel.setObjectName("crpixLabel")
        self.gridLayout.addWidget(self.crpixLabel, 2, 0, 1, 1)
        self.crpixLine = QtGui.QLineEdit(extend)
        self.crpixLine.setObjectName("crpixLine")
        self.gridLayout.addWidget(self.crpixLine, 2, 1, 1, 1)
        self.cunitLabel = QtGui.QLabel(extend)
        self.cunitLabel.setObjectName("cunitLabel")
        self.gridLayout.addWidget(self.cunitLabel, 3, 0, 1, 1)
        self.cunitBox = QtGui.QComboBox(extend)
        self.cunitBox.setObjectName("cunitBox")
        self.gridLayout.addWidget(self.cunitBox, 3, 1, 1, 1)
        self.crvalLabel = QtGui.QLabel(extend)
        self.crvalLabel.setObjectName("crvalLabel")
        self.gridLayout.addWidget(self.crvalLabel, 4, 0, 1, 1)
        self.crvalLine = QtGui.QLineEdit(extend)
        self.crvalLine.setObjectName("crvalLine")
        self.gridLayout.addWidget(self.crvalLine, 4, 1, 1, 1)
        self.cdeltLabel = QtGui.QLabel(extend)
        self.cdeltLabel.setObjectName("cdeltLabel")
        self.gridLayout.addWidget(self.cdeltLabel, 5, 0, 1, 1)
        self.cdeltLine = QtGui.QLineEdit(extend)
        self.cdeltLine.setObjectName("cdeltLine")
        self.gridLayout.addWidget(self.cdeltLine, 5, 1, 1, 1)
        self.crotaLabel = QtGui.QLabel(extend)
        self.crotaLabel.setObjectName("crotaLabel")
        self.gridLayout.addWidget(self.crotaLabel, 6, 0, 1, 1)
        self.crotaLine = QtGui.QLineEdit(extend)
        self.crotaLine.setObjectName("crotaLine")
        self.gridLayout.addWidget(self.crotaLine, 6, 1, 1, 1)
        self.dunitLabel = QtGui.QLabel(extend)
        self.dunitLabel.setObjectName("dunitLabel")
        self.gridLayout.addWidget(self.dunitLabel, 7, 0, 1, 1)
        self.dunitLine = QtGui.QLineEdit(extend)
        self.dunitLine.setObjectName("dunitLine")
        self.gridLayout.addWidget(self.dunitLine, 7, 1, 1, 1)
        self.drvalLabel = QtGui.QLabel(extend)
        self.drvalLabel.setObjectName("drvalLabel")
        self.gridLayout.addWidget(self.drvalLabel, 8, 0, 1, 1)
        self.drvalLine = QtGui.QLineEdit(extend)
        self.drvalLine.setObjectName("drvalLine")
        self.gridLayout.addWidget(self.drvalLine, 8, 1, 1, 1)
        self.freqLabel = QtGui.QLabel(extend)
        self.freqLabel.setObjectName("freqLabel")
        self.gridLayout.addWidget(self.freqLabel, 9, 0, 1, 1)
        self.freqLine = QtGui.QLineEdit(extend)
        self.freqLine.setObjectName("freqLine")
        self.gridLayout.addWidget(self.freqLine, 9, 1, 1, 1)

        self.retranslateUi(extend)
        QtCore.QMetaObject.connectSlotsByName(extend)

    def retranslateUi(self, extend):
        extend.setWindowTitle(QtGui.QApplication.translate("extend", "Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.ctypeLabel.setText(QtGui.QApplication.translate("extend", "CTYPE", None, QtGui.QApplication.UnicodeUTF8))
        self.naxisLabel.setText(QtGui.QApplication.translate("extend", "NAXIS", None, QtGui.QApplication.UnicodeUTF8))
        self.crpixLabel.setText(QtGui.QApplication.translate("extend", "CRPIX", None, QtGui.QApplication.UnicodeUTF8))
        self.cunitLabel.setText(QtGui.QApplication.translate("extend", "CUNIT", None, QtGui.QApplication.UnicodeUTF8))
        self.crvalLabel.setText(QtGui.QApplication.translate("extend", "CRVAL", None, QtGui.QApplication.UnicodeUTF8))
        self.cdeltLabel.setText(QtGui.QApplication.translate("extend", "CDELT", None, QtGui.QApplication.UnicodeUTF8))
        self.crotaLabel.setText(QtGui.QApplication.translate("extend", "CROTA", None, QtGui.QApplication.UnicodeUTF8))
        self.dunitLabel.setText(QtGui.QApplication.translate("extend", "DUNIT", None, QtGui.QApplication.UnicodeUTF8))
        self.drvalLabel.setText(QtGui.QApplication.translate("extend", "DRVAL", None, QtGui.QApplication.UnicodeUTF8))
        self.freqLabel.setText(QtGui.QApplication.translate("extend", "FREQ0", None, QtGui.QApplication.UnicodeUTF8))
