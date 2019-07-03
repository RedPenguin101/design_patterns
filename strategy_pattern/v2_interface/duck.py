# duck.py
from abc import ABC, abstractmethod

import quackbehavior as qb
import flybehavior as fb

class Duck(ABC):
    def setQuackBehavior(self, quackbeh: qb.QuackBehavior):
        self.quackBehavior = quackbeh

    def perform_quack(self):
        self.quackBehavior.quack()

    def swim(self):
        pass

    def setFlyBehavior(self, flybeh: fb.FlyBehavior):
        self.flyBehavior = flybeh

    def perform_fly(self):
        self.flyBehavior.fly()

    @abstractmethod
    def display(self):
        pass


class MallardDuck(Duck):
    def __init__(self):
        self.quackBehavior = qb.Quack()
        self.flyBehavior = fb.FlyWithWings()

    def display(self):
        print('looks like a mallard')


class RedheadDuck(Duck):
    def __init__(self):
        self.quackBehavior = qb.Quack()
        self.flyBehavior = fb.FlyWithWings()

    def display(self):
        print('looks like a redhead')


class RubberDuck(Duck):
    def __init__(self):
        self.quackBehavior = qb.Squeak()
        self.flyBehavior = fb.FlyNoWay()

    def display(self):
        print('looks like a rubber duck')


class ModelDuck(Duck):
    def __init__(self):
        self.quackBehavior = qb.Quack()
        self.flyBehavior = fb.FlyNoWay()

    def display(self):
        print('looks like a model duck')
