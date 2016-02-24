from observer import Observer
from binder import Binder

from miniluv import package_logger
module_logger = package_logger.getChild('viewmodel')


class ViewModel(Observer):

    def __init__(self, model):

        self.logger = module_logger.getChild('ViewModel')
        self._model = model
        self._binders = []
        self.observe(model)

        try:
            self._observed_fields = set(model.observed_fields)
        except AttributeError:
            self._observed_fields = set()

        self.logger.debug("__init__: viewmodel %s is running" % (id(self),))
        self.logger.debug("__init__: observed model id is %s" % (id(self._model),))
        self.logger.debug("__init__: observed fields for model %s are %s" % (id(self._model), str(self._observed_fields),))

        if self._observed_fields == set():
            self.logger.warning("__init__: observed fields for model %s is an empty set!" % (id(self._model)))

    def add_view(self, view):

        b = Binder(self, view, self._observed_fields)
        self.logger.debug("add_view: binder %s working for view %s" % (id(b), id(view),))
        self._binders.append(b)

        for field in self._observed_fields:
            value = getattr(self._model, field)
            if value is not None:
                self.notify(self._model, field, value)

    def notify(self, caller, attribute, value):

        if caller is self._model:
            self.logger.debug("notify: in model %s '%s'=%s now" % (id(caller), attribute, value))

            for b in self._binders:
                self.logger.debug("notify: modelview %s sent to binder %s '%s'=%s" % (id(self), id(b), attribute, value))
                b.set_value(attribute, value)
        else:
            # self.logger.debug("notify: in binder %s '%s'=%s now" % (id(observable), attribute, value))
            self.logger.debug("notify: storing '%s'=%s in model %s" % (attribute, value, id(self._model)))
            setattr(self._model, attribute, value)
