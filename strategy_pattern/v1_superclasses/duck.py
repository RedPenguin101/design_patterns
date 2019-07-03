# duck.py
from abc import ABC, abstractmethod


class Duck(ABC):
    def quack(self):
        print('quack quack')

    def swim(self):
        print('splash splash')

    def fly(self):
        print('flap flap')

    @abstractmethod
    def display(self):
        pass


class MallardDuck(Duck):
    def display(self):
        print('looks like a mallard')


class RedheadDuck(Duck):
    def display(self):
        print('looks like a redhead')

