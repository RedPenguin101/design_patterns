import abc


class Turkey(abc.ABC):
    @abc.abstractmethod
    def gobble(self):
        pass

    @abc.abstractmethod
    def fly(self):
        pass


class WildTurkey(Turkey):
    def gobble(self):
        print('gobble gobble')

    def fly(self):
        print("i'm flying a short distance")
