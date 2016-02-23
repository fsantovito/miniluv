from PySide import QtCore, QtGui
from allwidgets_template import Ui_Dialog

class AllWidgetsView(QtGui.QDialog):

    def __init__(self, *args, **kwargs):
        super(AllWidgetsView, self).__init__(*args, **kwargs)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)        

        self.ui.dial.valueChanged.connect(self.ui.slider.setValue)
        self.ui.slider.valueChanged.connect(self.ui.dial.setValue)

        self.ui.slider.valueChanged.connect(self.ui.lcd.display)
        self.ui.slider.valueChanged.connect(self.ui.progress.setValue)
        
        self.ui.combobox.insertItems(0, ['zero', 'one', 'two', 'three'])

if __name__ == "__main__":

    import sys
    app = QtGui.QApplication(sys.argv)
    view = AllWidgetsView()
    view.show()
    sys.exit(app.exec_())

