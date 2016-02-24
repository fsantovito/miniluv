import weakref


class Observer(object):
    def observe(self, observable, enable=True):
        """forza observable a notificare gli eventi"""

        if not enable:
            raise NotImplementedError("")

        observable._Observable__observers[self] = self

    def notify(self, observable, attribute, value):
        # print "[Observer %s] %s.%s=%s" % (id(self), id(observable), attribute, value)
        raise NotImplementedError("")


class Observable(type):

    def __new__(meta, name, bases, classdict):

        def notify(self, attribute, value):
            if attribute in self.observed_fields:
                for observer in self.__observers:
                    observer.notify(self, attribute, value)

        def notify__setattr__(f):
            """ decoratore per __setattr__"""

            # https://bugs.python.org/issue3445
            # from functools import wraps
            # @wraps(f)
            def wrapper(*args, **kwargs):
                instance, attribute, value = args[:3]
                result = f(*args, **kwargs)
                instance.notify(attribute, value)
                return result

            return wrapper

        classdict["notify"] = notify

        instance = super(Observable, meta).__new__(meta, name, bases, classdict)
        instance.__setattr__ = notify__setattr__(instance.__setattr__)
        return instance

    def __init__(cls, name, bases, dct):
        super(Observable, cls).__init__(name, bases, dct)
        cls.__observers = weakref.WeakValueDictionary()
