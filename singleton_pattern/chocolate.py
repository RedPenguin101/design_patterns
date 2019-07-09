# chocolate.py


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args,
                    **kwargs)
        return cls._instances[cls]


class ChocolateBoiler(metaclass=Singleton):
    def __init__(self):
        self.empty = True
        self.boiled = False

    def fill(self):
        if self.empty:
            self.empty = False
            self.boiled = False

    def drain(self):
        if not self.empty and self.boiled:
            self.empty = True

    def boil(self):
        if not self.empty and not self.boiled:
            self.boiled = True
