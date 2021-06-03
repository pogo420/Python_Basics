# bridge patter: Reduces cartesian product of class combination
# Keyboard Driver and Mouse Driver
# Unix Adapter and Windows Adapter
# We might end up with 4 classes, but we will reduce this by sending objects as parameters(as bridge)
import abc
from abc import ABC


class Driver(ABC):
    def __init__(self, dvr_type: str):
        self.dvr_type = dvr_type

    @abc.abstractmethod
    def implement(self): pass


class KeyboardDriver(Driver):
    def __init__(self, dvr_type: str = "KEYBOARD"):
        super().__init__(dvr_type)

    def implement(self):
        return "i am keyboard driver"


class MouseDriver(Driver):
    def __init__(self, dvr_type: str = "MOUSE"):
        super().__init__(dvr_type)

    def implement(self):
        return "i am mouse driver"


class OsAdapters(ABC):
    def __init__(self, os: str):
        self.os = os

    @abc.abstractmethod
    def adapter(self, driver: Driver): pass


class UnixAdapter(OsAdapters):
    def __init__(self, os: str = "UNIX"):
        super().__init__(os)

    def adapter(self, driver: Driver):
        print(f"{driver.implement()} in {self.os}")


class WinAdapter(OsAdapters):
    def __init__(self, os: str = "WIN"):
        super().__init__(os)

    def adapter(self, driver: Driver):
        print(f"{driver.implement()} in {self.os}")


if __name__ == "__main__":
    kd = KeyboardDriver()
    md = MouseDriver()

    WinAdapter().adapter(kd)
    UnixAdapter().adapter(md)
