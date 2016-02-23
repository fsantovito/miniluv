from logging import Logger
from datetime import datetime
import PySide
from PySide import QtCore

from miniluv import package_logger
module_logger = package_logger.getChild('connectors')


class WidgetConnector(QtCore.QObject):

    signal = None

    def __init__(self, binder, widget, *args, **kwargs):

        super(WidgetConnector, self).__init__(*args, **kwargs)

        self.logger = module_logger.getChild('WidgetConnector')

        self._binder = binder
        self._field = widget.objectName()
        self._widget_id = id(widget)
        self.create_connection(widget)

    def create_connection(self, widget):
        raise NotImplementedError()

    def valueChanged(self, value):
        """slot connesso al widget"""

        try:
            widget_id = id(self.sender())
        except Exception:
            widget_id = None

        self.logger.debug("valueChanged: connector %s received from widget %s '%s'=%s" % (id(self), widget_id, self._field, value))
        self.logger.debug("valueChanged: connector %s sent to binder %s '%s'=%s" % (id(self), id(self._binder), self._field, value))

        self._binder.set_value(self._field, value)

    def setValue(self, value):
        """emette il nuovo valore"""
        self.logger.debug("setValue: connector %s sent to widget %s '%s'='%s' " % (id(self), self._widget_id, self._field, value))
        self.signal.emit(value)


class LineEditConnector(WidgetConnector):

    signal = QtCore.Signal(str)

    def create_connection(self, widget):
        widget.textChanged.connect(self.valueChanged)
        self.signal.connect(widget.setText)


class TextEditConnector(LineEditConnector):

    signal = QtCore.Signal(str)

    def valueChanged(self, value=None):

        try:
            widget = self.sender()
            widget_id = id(widget)
        except Exception:
            widget_id = None

        if widget_id is None and value is None:
            self.logger.warning("valueChanged: connector %s received invalid data from external object.")
            return

        value = widget.toPlainText()
        self.logger.debug("valueChanged: connector %s received from widget %s '%s'=%s" % (id(self), widget_id, self._field, value))
        self.logger.debug("valueChanged: connector %s sent to binder %s '%s'=%s" % (id(self), id(self._binder), self._field, value))

        self._binder.set_value(self._field, value)


class PlainTextEditConnector(TextEditConnector):

    def create_connection(self, widget):
        widget.textChanged.connect(self.valueChanged)
        self.signal.connect(widget.setPlainText)


class SpinBoxConnector(WidgetConnector):

    signal = QtCore.Signal(int)

    def create_connection(self, widget):
        widget.valueChanged.connect(self.valueChanged)
        self.signal.connect(widget.setValue)


class DoubleSpinBoxConnector(SpinBoxConnector):
    signal = QtCore.Signal(float)


class SliderConnector(SpinBoxConnector):
    pass


class ProgressBarConnector(SpinBoxConnector):
    pass


class LCDNumberConnector(SpinBoxConnector):
    def create_connection(self, widget):
        self.signal.connect(widget.display)


class DialConnector(SpinBoxConnector):
    pass


class DateTimeEditConnector(WidgetConnector):

    signal = QtCore.Signal(datetime)

    def create_connection(self, widget):
        widget.dateTimeChanged.connect(self.valueChanged)
        self.signal.connect(widget.setDateTime)

    def valueChanged(self, value):
        """slot connesso al widget"""

        try:
            widget_id = id(self.sender())
        except Exception:
            widget_id = None

        self.logger.debug("valueChanged: connector %s received from widget %s '%s'=%s" % (id(self), widget_id, self._field, value))
        self.logger.debug("valueChanged: connector %s sent to binder %s '%s'=%s" % (id(self), id(self._binder), self._field, value))

        self.logger.debug("valueChanged: --------------------------------------")
        self.logger.debug("valueChanged: value = %s" % (value,))
        self.logger.debug("valueChanged: type = %s" % (type(value),))
        self.logger.debug("valueChanged: converting to python type = %s" % (type(value.toPython()),))
        self.logger.debug("valueChanged: --------------------------------------")

        self._binder.set_value(self._field, value.toPython())


class DateEditConnector(DateTimeEditConnector):
    pass


class TimeEditConnector(DateTimeEditConnector):

    def create_connection(self, widget):
        widget.dateTimeChanged.connect(self.valueChanged)
        self.signal.connect(widget.setTime)

    def valueChanged(self, value):
        """slot connesso al widget"""

        try:
            widget_id = id(self.sender())
        except Exception:
            widget_id = None

        self.logger.debug("valueChanged: connector %s received from widget %s '%s'=%s" % (id(self), widget_id, self._field, value))
        self.logger.debug("valueChanged: connector %s sent to binder %s '%s'=%s" % (id(self), id(self._binder), self._field, value))

        self.logger.debug("valueChanged: --------------------------------------")
        self.logger.debug("valueChanged: value = %s" % (value,))
        self.logger.debug("valueChanged: type = %s" % (type(value),))
        self.logger.debug("valueChanged: converting to python type = %s" % (type(value.toPython()),))
        self.logger.debug("valueChanged: --------------------------------------")

        self._binder.set_value(self._field, value.toPython().time())


class CalendarWidgetConnector(DateEditConnector):

    def create_connection(self, widget):
        widget.clicked.connect(self.valueChanged)
        widget.selectionChanged.connect(self.valueChanged)
        self.signal.connect(widget.setSelectedDate)

    def valueChanged(self, value=None):
        """slot connesso al widget"""

        try:
            widget_id = id(self.sender())
        except Exception:
            widget_id = None

        if value is None:
            calendar = self.sender()
            value = calendar.selectedDate()

        self.logger.debug("valueChanged: connector %s received from widget %s '%s'=%s" % (id(self), widget_id, self._field, value))
        self.logger.debug("valueChanged: connector %s sent to binder %s '%s'=%s" % (id(self), id(self._binder), self._field, value))

        self.logger.debug("valueChanged: --------------------------------------")
        self.logger.debug("valueChanged: value = %s" % (value,))
        self.logger.debug("valueChanged: type = %s" % (type(value),))
        self.logger.debug("valueChanged: converting to python type = %s" % (type(value.toPython()),))
        self.logger.debug("valueChanged: --------------------------------------")

        self._binder.set_value(self._field, value.toPython())


class CheckBoxConnector(WidgetConnector):

    signal = QtCore.Signal(int)

    def create_connection(self, widget):
        widget.stateChanged.connect(self.valueChanged)
        self.signal.connect(widget.setChecked)

    def valueChanged(self, value):
        """slot connesso al widget"""

        try:
            widget_id = id(self.sender())
        except Exception:
            widget_id = None

        self.logger.debug("valueChanged: connector %s received from widget %s '%s'=%s" % (id(self), widget_id, self._field, value))
        self.logger.debug("valueChanged: connector %s sent to binder %s '%s'=%s" % (id(self), id(self._binder), self._field, value))

        self._binder.set_value(self._field, value == PySide.QtCore.Qt.Checked)


class ComboBoxConnector(WidgetConnector):

    signal = QtCore.Signal(int)

    def create_connection(self, widget):
        widget.currentIndexChanged.connect(self.valueChanged)
        self.signal.connect(widget.setCurrentIndex)


class RadioButtonConnector(WidgetConnector):

    signal = QtCore.Signal(bool)

    def create_connection(self, widget):
        widget.toggled.connect(self.valueChanged)
        self.signal.connect(widget.setChecked)


class GroupBoxConnector(WidgetConnector):

    signal = QtCore.Signal(bool)

    def create_connection(self, widget):
        widget.toggled.connect(self.valueChanged)
        self.signal.connect(widget.setChecked)
