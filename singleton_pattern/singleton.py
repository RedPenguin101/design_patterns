# singleton.py

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

class Singleton2:
    instance = None

    def __init__(self, arg):
        if Singleton2.instance = None:
            
