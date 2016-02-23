from logging import Logger
import PySide
from PySide import QtCore, QtGui

from miniluv import package_logger
import miniluv.connectors as connectors
module_logger = package_logger.getChild('binder')


class Binder(object):

    bound_widgets = {
        PySide.QtGui.QComboBox: connectors.ComboBoxConnector,
        PySide.QtGui.QCheckBox: connectors.CheckBoxConnector,
        PySide.QtGui.QGroupBox: connectors.GroupBoxConnector,
        PySide.QtGui.QRadioButton: connectors.RadioButtonConnector,
        PySide.QtGui.QLineEdit: connectors.LineEditConnector,
        PySide.QtGui.QTextEdit: connectors.TextEditConnector,
        PySide.QtGui.QPlainTextEdit: connectors.PlainTextEditConnector,

        PySide.QtGui.QTimeEdit: connectors.TimeEditConnector,
        PySide.QtGui.QDateEdit: connectors.DateEditConnector,
        PySide.QtGui.QDateTimeEdit: connectors.DateTimeEditConnector,
        PySide.QtGui.QCalendarWidget: connectors.CalendarWidgetConnector,

        PySide.QtGui.QLCDNumber: connectors.LCDNumberConnector,
        PySide.QtGui.QSpinBox: connectors.SpinBoxConnector,
        PySide.QtGui.QDoubleSpinBox: connectors.DoubleSpinBoxConnector,
        PySide.QtGui.QDial: connectors.DialConnector,
        PySide.QtGui.QSlider: connectors.SliderConnector,
        PySide.QtGui.QProgressBar: connectors.ProgressBarConnector,
    }

    def __init__(self, observer, view, fields):

        self._observer = observer
        self._fields = fields
        self._connectors = {}
        self.logger = module_logger.getChild('Binder')

        widgets = {}
        for obj in view.findChildren(QtGui.QWidget):
            if obj.objectName() in fields and isinstance(obj, tuple(self.bound_widgets)):
                try:
                    widgets[obj.__class__].append(obj)
                except KeyError:
                    widgets[obj.__class__] = []
                    widgets[obj.__class__].append(obj)

        try:
            for cls, items in widgets.items():
                cntr = self.bound_widgets[cls]
                for widget in items:
                    self._connectors[widget.objectName()] = cntr(self, widget)
        except KeyError:
            pass

    def set_value(self, field, value):

        old_value = getattr(self, field, None)
        if old_value != value:

            self.logger.debug("set_value: in binder %s '%s'=%s" % (id(self), field, value))
            setattr(self, field, value)
            self._observer.notify(self, field, value)

            connector = self._connectors[field]
            self.logger.debug("set_value: binder %s sent to connector %s '%s'=%s" % (id(self), id(connector), field, value))
            connector.setValue(value)

        else:
            self.logger.debug("set_value: binder %s stops forwarding values. '%s'=%s already" % (id(self), field, value))
