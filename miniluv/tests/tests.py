import sys
import unittest
from datetime import datetime, date, time, timedelta
from PySide import QtCore, QtGui
from miniluv.viewmodel import ViewModel
from allwidgets_view import AllWidgetsView
from model import Model

app = QtGui.QApplication(sys.argv)
view = AllWidgetsView()
model = Model()
vm = ViewModel(model)
vm.add_view(view)


class TestViewModel(unittest.TestCase):

    def test_checkbox(self):

        model.checkbox = False
        self.assertEqual(view.ui.checkbox.isChecked(), model.checkbox)
        view.ui.checkbox.setChecked(True)
        self.assertEqual(view.ui.checkbox.isChecked(), model.checkbox)

    def test_groupbox(self):

        model.groupbox = False
        self.assertEqual(view.ui.groupbox.isChecked(), model.groupbox)
        view.ui.groupbox.setChecked(True)
        self.assertEqual(view.ui.groupbox.isChecked(), model.groupbox)

    def test_combobox(self):
        model.combobox = 1
        self.assertEqual(view.ui.combobox.currentIndex(), model.combobox)
        view.ui.combobox.setCurrentIndex(2)
        self.assertEqual(view.ui.combobox.currentIndex(), model.combobox)

    def test_lineedit(self):
        model.lineedit = 'other'
        self.assertEqual(view.ui.lineedit.text(), model.lineedit)
        view.ui.lineedit.setText('test')
        self.assertEqual(view.ui.lineedit.text(), model.lineedit)

    def test_datetimeedit(self):
        dt = datetime(2016, 1, 1, 12, 13, 15)
        self.assertEqual(model.datetimeedit, None)
        view.ui.datetimeedit.setDateTime(dt)
        self.assertEqual(model.datetimeedit, dt)
        model.datetimeedit = dt + timedelta(days=1)
        self.assertEqual(view.ui.datetimeedit.dateTime(), model.datetimeedit)

    def test_dateedit(self):
        dt = datetime(2016, 1, 1, 0, 0, 0)
        self.assertEqual(model.dateedit, None)
        view.ui.dateedit.setDate(dt)
        self.assertEqual(model.dateedit, dt)
        model.dateedit = dt + timedelta(days=1)
        self.assertEqual(view.ui.dateedit.date(), model.dateedit)

    def test_timeedit(self):
        dt = time(11, 12, 13)
        self.assertEqual(model.timeedit, None)
        view.ui.timeedit.setTime(dt)
        self.assertEqual(model.timeedit, dt)

        dt = datetime.combine(date.today(), dt) + timedelta(minutes=30)
        dt = dt.time()
        model.timeedit = dt
        self.assertEqual(view.ui.timeedit.time(), model.timeedit)

    def test_spinbox(self):
        model.spinbox = 6
        self.assertEqual(model.spinbox, view.ui.spinbox.value())
        view.ui.spinbox.setValue(5)
        self.assertEqual(model.spinbox, view.ui.spinbox.value())

    def test_doublespinbox(self):
        model.doublespinbox = 6.81
        self.assertEqual(model.doublespinbox, view.ui.doublespinbox.value())
        view.ui.doublespinbox.setValue(5.75)
        self.assertEqual(model.doublespinbox, view.ui.doublespinbox.value())

    def test_dial(self):
        model.dial = 6
        self.assertEqual(model.dial, view.ui.dial.value())
        view.ui.dial.setValue(5)
        self.assertEqual(model.dial, view.ui.dial.value())

    def test_slider(self):
        model.slider = 6
        self.assertEqual(model.slider, view.ui.slider.value())
        view.ui.slider.setValue(5)
        self.assertEqual(model.slider, view.ui.slider.value())

    def test_calendar(self):
        dt = date(2016, 1, 1)
        model.calendar = dt
        self.assertEqual(model.calendar, view.ui.calendar.selectedDate().toPython())
        dt = date(2016, 1, 1) + timedelta(days=1)
        view.ui.calendar.setSelectedDate(dt)
        self.assertEqual(model.calendar, view.ui.calendar.selectedDate().toPython())

    def test_lcd(self):
        model.lcd = 15
        self.assertEqual(model.lcd, view.ui.lcd.value())

    def test_progress(self):
        model.progress = 20
        self.assertEqual(model.progress, view.ui.progress.value())

    def test_radiobutton(self):
        # initial state for radio buttons
        model.radiobutton1 = True
        model.radiobutton2 = False
        model.radiobutton3 = False

        self.assertEqual(model.radiobutton1, view.ui.radiobutton1.isChecked())
        self.assertEqual(model.radiobutton2, False)
        self.assertEqual(model.radiobutton2, view.ui.radiobutton2.isChecked())
        self.assertEqual(model.radiobutton3, False)
        self.assertEqual(model.radiobutton3, view.ui.radiobutton3.isChecked())

        model.radiobutton2 = True
        self.assertEqual(model.radiobutton2, view.ui.radiobutton2.isChecked())
        self.assertEqual(model.radiobutton1, False)
        self.assertEqual(model.radiobutton1, view.ui.radiobutton1.isChecked())
        self.assertEqual(model.radiobutton3, False)
        self.assertEqual(model.radiobutton3, view.ui.radiobutton3.isChecked())

        model.radiobutton3 = True
        self.assertEqual(model.radiobutton3, view.ui.radiobutton3.isChecked())
        self.assertEqual(model.radiobutton1, False)
        self.assertEqual(model.radiobutton1, view.ui.radiobutton1.isChecked())
        self.assertEqual(model.radiobutton2, False)
        self.assertEqual(model.radiobutton2, view.ui.radiobutton2.isChecked())

    def test_textedit(self):
        model.textedit = "foo"
        self.assertEqual(model.textedit, view.ui.textedit.toPlainText())
        view.ui.textedit.setText("bar")
        self.assertEqual(model.textedit, view.ui.textedit.toPlainText())

    def test_plaintextedit(self):
        model.plaintextedit = "foo"
        self.assertEqual(model.plaintextedit, view.ui.plaintextedit.toPlainText())
        view.ui.plaintextedit.setPlainText("bar")
        self.assertEqual(model.plaintextedit, view.ui.plaintextedit.toPlainText())

    def test_fix_exception_on_field_not_observed(self):
        model.missing_field = 'missing'
        del model.missing_field

    def test_observed_should_not_share_observers(self):
        
        model2 = Model()
        self.assertFalse(model._Observable__observers is model2._Observable__observers)


if __name__ == '__main__':
    unittest.main()
