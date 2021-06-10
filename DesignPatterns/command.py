# command design pattern: all command/instruction as object even these excutute and un execute logic.
# for new command will just extent no need for modification.

import abc
from abc import ABC


class CommandProcess(ABC):
    @abc.abstractmethod
    def process(self): pass


class Command(ABC):
    @abc.abstractmethod
    def execute(self, process_object: CommandProcess): pass

    @abc.abstractmethod
    def unexecute(self, process_object: CommandProcess): pass


##############################################################################
class Light(Command):

    def execute(self, process_object: CommandProcess):
        return process_object.process()

    def unexecute(self, process_object: CommandProcess):
        return process_object.process()


class LightOnCommand(CommandProcess):
    def process(self):
        return "Light On"


class LightOffCommand(CommandProcess):
    def process(self):
        return "Light Off"


if __name__ == '__main__':
    light_command = Light()
    print(light_command.execute(LightOnCommand()))
    print(light_command.execute(LightOffCommand()))
