 singleton.py

class Singleton:
    class _InnerClass:
        def __init__(self, arg):
            self.value = arg

    instance = None

    def __init__(self, arg):
        if Singleton.instance is None:
            Singleton.instance = Singleton._InnerClass(arg)
        else:
            print('no no no, only one instance allowed')

### a decorator

def singleton_decorator(class_):
    instances = {}
    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return get_instance

@singleton_decorator
class MyClass:
    pass

### metaclass - maybe the best. Have a custom metaclass, which inherits from
### the base metaclass `type` has a class dictionary 'instances', and overide
### __call__ to return the value of the key cls in the instance dict.
### (as well as create the instance using the super __call__ to type. if it
### doesn't exist."

class SingletonMC(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMC, cls).__call__(*args,
                    **kwargs)
        return cls._instances[cls]

class MyClass2(metaclass=SingletonMC):
    pass
