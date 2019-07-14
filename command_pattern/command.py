# command.py

import abc

from light import Light


class Command(abc.ABC):
    @abc.abstractmethod
    def execute(self):
        pass


class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.on()
