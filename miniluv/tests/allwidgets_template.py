# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'allwidgets_template.ui'
#
# Created: Mon Feb 22 15:57:47 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 484)
        self.gridLayout_2 = QtGui.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.calendar = QtGui.QCalendarWidget(Dialog)
        self.calendar.setObjectName("calendar")
        self.gridLayout_2.addWidget(self.calendar, 5, 3, 1, 1)
        self.progress = QtGui.QProgressBar(Dialog)
        self.progress.setProperty("value", 0)
        self.progress.setObjectName("progress")
        self.gridLayout_2.addWidget(self.progress, 11, 3, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 6, 3, 1, 1)
        self.dateedit = QtGui.QDateEdit(Dialog)
        self.dateedit.setObjectName("dateedit")
        self.gridLayout_2.addWidget(self.dateedit, 11, 1, 1, 1)
        self.dial = QtGui.QDial(Dialog)
        self.dial.setMaximum(100)
        self.dial.setObjectName("dial")
        self.gridLayout_2.addWidget(self.dial, 7, 3, 1, 1)
        self.textedit = QtGui.QTextEdit(Dialog)
        self.textedit.setObjectName("textedit")
        self.gridLayout_2.addWidget(self.textedit, 5, 0, 3, 1)
        self.spinbox = QtGui.QSpinBox(Dialog)
        self.spinbox.setObjectName("spinbox")
        self.gridLayout_2.addWidget(self.spinbox, 8, 0, 1, 1)
        self.combobox = QtGui.QComboBox(Dialog)
        self.combobox.setObjectName("combobox")
        self.gridLayout_2.addWidget(self.combobox, 3, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 13, 1, 1, 3)
        self.datetimeedit = QtGui.QDateTimeEdit(Dialog)
        self.datetimeedit.setObjectName("datetimeedit")
        self.gridLayout_2.addWidget(self.datetimeedit, 8, 1, 1, 1)
        self.lineedit = QtGui.QLineEdit(Dialog)
        self.lineedit.setObjectName("lineedit")
        self.gridLayout_2.addWidget(self.lineedit, 4, 1, 1, 1)
        self.timeedit = QtGui.QTimeEdit(Dialog)
        self.timeedit.setObjectName("timeedit")
        self.gridLayout_2.addWidget(self.timeedit, 9, 1, 1, 1)
        self.plaintextedit = QtGui.QPlainTextEdit(Dialog)
        self.plaintextedit.setObjectName("plaintextedit")
        self.gridLayout_2.addWidget(self.plaintextedit, 5, 1, 3, 1)
        self.doublespinbox = QtGui.QDoubleSpinBox(Dialog)
        self.doublespinbox.setObjectName("doublespinbox")
        self.gridLayout_2.addWidget(self.doublespinbox, 9, 0, 1, 1)
        self.lcd = QtGui.QLCDNumber(Dialog)
        self.lcd.setObjectName("lcd")
        self.gridLayout_2.addWidget(self.lcd, 11, 0, 1, 1)
        self.slider = QtGui.QSlider(Dialog)
        self.slider.setMaximum(100)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName("slider")
        self.gridLayout_2.addWidget(self.slider, 9, 3, 1, 1)
        self.checkbox = QtGui.QCheckBox(Dialog)
        self.checkbox.setObjectName("checkbox")
        self.gridLayout_2.addWidget(self.checkbox, 2, 1, 1, 1)
        self.groupbox = QtGui.QGroupBox(Dialog)
        self.groupbox.setCheckable(True)
        self.groupbox.setChecked(False)
        self.groupbox.setObjectName("groupbox")
        self.gridLayout = QtGui.QGridLayout(self.groupbox)
        self.gridLayout.setObjectName("gridLayout")
        self.radiobutton1 = QtGui.QRadioButton(self.groupbox)
        self.radiobutton1.setObjectName("radiobutton1")
        self.gridLayout.addWidget(self.radiobutton1, 0, 0, 1, 1)
        self.radiobutton2 = QtGui.QRadioButton(self.groupbox)
        self.radiobutton2.setObjectName("radiobutton2")
        self.gridLayout.addWidget(self.radiobutton2, 1, 0, 1, 1)
        self.radiobutton3 = QtGui.QRadioButton(self.groupbox)
        self.radiobutton3.setObjectName("radiobutton3")
        self.gridLayout.addWidget(self.radiobutton3, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupbox, 2, 0, 3, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.radiobutton1, self.radiobutton2)
        Dialog.setTabOrder(self.radiobutton2, self.radiobutton3)
        Dialog.setTabOrder(self.radiobutton3, self.checkbox)
        Dialog.setTabOrder(self.checkbox, self.combobox)
        Dialog.setTabOrder(self.combobox, self.lineedit)
        Dialog.setTabOrder(self.lineedit, self.textedit)
        Dialog.setTabOrder(self.textedit, self.plaintextedit)
        Dialog.setTabOrder(self.plaintextedit, self.spinbox)
        Dialog.setTabOrder(self.spinbox, self.doublespinbox)
        Dialog.setTabOrder(self.doublespinbox, self.datetimeedit)
        Dialog.setTabOrder(self.datetimeedit, self.timeedit)
        Dialog.setTabOrder(self.timeedit, self.dateedit)
        Dialog.setTabOrder(self.dateedit, self.buttonBox)
        Dialog.setTabOrder(self.buttonBox, self.calendar)
        Dialog.setTabOrder(self.calendar, self.dial)
        Dialog.setTabOrder(self.dial, self.slider)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.checkbox.setText(QtGui.QApplication.translate("Dialog", "CheckBox", None, QtGui.QApplication.UnicodeUTF8))
        self.groupbox.setTitle(QtGui.QApplication.translate("Dialog", "GroupBox", None, QtGui.QApplication.UnicodeUTF8))
        self.radiobutton1.setText(QtGui.QApplication.translate("Dialog", "RadioButton 1", None, QtGui.QApplication.UnicodeUTF8))
        self.radiobutton2.setText(QtGui.QApplication.translate("Dialog", "RadioButton 2", None, QtGui.QApplication.UnicodeUTF8))
        self.radiobutton3.setText(QtGui.QApplication.translate("Dialog", "RadioButton 3", None, QtGui.QApplication.UnicodeUTF8))

