import weakref

def observable__setattr__(f):
    """ decoratore per Observable.__setattr__"""

    # https://bugs.python.org/issue3445
    # from functools import wraps
    # @wraps(f)
    def wrapper(*args, **kwargs):
        instance, attribute, value = args[:3]
        result = f(*args, **kwargs)
        instance.notify(attribute, value)
        return result
    return wrapper


def observable__getattribute__(f):
    """ decoratore per Observable.__getattribute__"""

    # https://bugs.python.org/issue3445
    # from functools import wraps
    # @wraps(f)
    def wrapper(*args, **kwargs):
        instance, attribute = args[:2]        
        result = f(*args, **kwargs)

        if attribute == '_Observable__observers' and result is None:
            result = weakref.WeakValueDictionary()
            setattr(instance, '_Observable__observers', result)
        return result

    return wrapper


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

        classdict['notify'] = notify
        classdict['_Observable__observers'] = None
        
        klass = super(Observable, meta).__new__(meta, name, bases, classdict)
        klass.__setattr__ = observable__setattr__(klass.__setattr__)
        klass.__getattribute__ = observable__getattribute__(klass.__getattribute__)
        return klass
