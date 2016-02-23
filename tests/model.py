from miniluv.observer import Observable


class Model(object):
    __metaclass__ = Observable

    checkbox = None
    groupbox = None
    combobox = None
    radiobutton1 = None
    radiobutton2 = None
    radiobutton3 = None

    textedit = None
    lineedit = None
    plaintextedit = None

    datetimeedit = None
    dateedit = None
    timeedit = None
    calendar = None

    lcd = None
    spinbox = None
    doublespinbox = None
    dial = None
    slider = None
    progress = None

    observed_fields = (
                    'checkbox',
                    'groupbox',
                    'combobox',
                    'radiobutton1',
                    'radiobutton2',
                    'radiobutton3',

                    'textedit',
                    'lineedit',
                    'plaintextedit',

                    'datetimeedit',
                    'dateedit',
                    'timeedit',
                    'calendar',

                    'lcd',
                    'spinbox',
                    'doublespinbox',
                    'dial',
                    'slider',
                    'progress'
                )
