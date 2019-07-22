import abc


class Duck(abc.ABC):
    @abc.abstractmethod
    def quack(self):
        pass


    @abc.abstractmethod
    def fly(self):
        pass


class MallardDuck(Duck):
    def quack(self):
        print("quack")

    def fly(self):
        print("I'm flying")
