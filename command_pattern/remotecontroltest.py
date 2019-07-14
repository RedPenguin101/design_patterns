# remotecontroltest.py

from simpleremote import SimpleRemoteControl
from light import Light
from command import LightOnCommand

def main():
    remote = SimpleRemoteControl()
    light = Light()
    light_on = LightOnCommand(light)

    remote.set_command(light_on)
    remote.button_was_pressed()


if __name__ == '__main__':
    main()
