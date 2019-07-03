from abc import ABC, abstractmethod

class FlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        pass

class FlyWithWings(FlyBehavior):
    def fly(self):
        print('flap flap')

class FlyNoWay(FlyBehavior):
    def fly(self):
        print('*nothing happens*')


class FlyRocketPowered(FlyBehavior):
    def fly(self):
        print('boom boom')


