from abc import ABC, abstractmethod


class QuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        pass


class Quack(QuackBehavior):
    def quack(self):
        print('quack quack')


class Squeak(QuackBehavior):
    def quack(self):
        print('squeak squeak')


class MuteQuack(QuackBehavior):
    def quack(self):
        print('*silence*')

