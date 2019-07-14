# simpleremote.py

from command import Command

class SimpleRemoteControl:

    def set_command(self, command: Command):
        self.slot = command

    def button_was_pressed(self):
        self.slot.execute()
