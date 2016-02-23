# miniluv
a viewmodel library for PySide


## status

Just released. It may contains a few bugs. Anyway the code is well covered by unit tests:

```bash
$ coverage run --source miniluv -m unittest miniluv.tests.tests

.................
----------------------------------------------------------------------
Ran 17 tests in 0.006s

OK
$ coverage report -m 
Name                                   Stmts   Miss  Cover   Missing
--------------------------------------------------------------------
miniluv/__init__.py                        2      0   100%   
miniluv/binder.py                         38      2    95%   55-56
miniluv/connectors.py                    154     15    90%   26, 33-34, 65-66, 69-70, 129-130, 159-160, 186-187, 218-219
miniluv/observer.py                       27      2    93%   9, 15
miniluv/tests/__init__.py                  0      0   100%   
miniluv/tests/allwidgets_template.py     106      0   100%   
miniluv/tests/allwidgets_view.py          18      5    72%   22-26
miniluv/tests/model.py                    23      0   100%   
miniluv/tests/tests.py                   122      1    99%   151
miniluv/viewmodel.py                      35      4    89%   19-20, 27, 38
--------------------------------------------------------------------
TOTAL                                    525     29    94%   
```


## what you need

* PySide 1.2.4
* Python 2.7

but in the future I'll support Python3 and PySide2


## how to use it

Use any python object as a MVVM model. It must use Observable as metaclass and must define observed_fields = (...) as a tuple of fields to be observed.

```python
class MyModel(object):
    __metaclass__ = Observable

	field1 = None
    field2 = None
    field3 = None
       
    observed_fields = ('field1', 'field2', 'field3')
```

then add a view instance and a model instance to the ViewModel

```python
    model = Model()
    view = AView()
    vm = ViewModel(model)
    vm.add_view(view)
```

ViewModel will manage 2-way databinding. Just be sure that the object's name for the field inside the view matches the name of a field inside the model.

a gist is [here](https://gist.github.com/fsantovito/24c2b46a11d9075d3fae).


## what's missing

* documentation (readthedocs.org in a near future)
* documentation (inside the code... sorry for that...)


## TODO

connectors.py needs to be refactored a little... but it'll be easy.

