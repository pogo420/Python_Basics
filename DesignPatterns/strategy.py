# algorithm is decided on the fly.
# logic implements same interface/ interfaces.
# We just plug the class, remaining code does not change.
# implementing without if else

import abc
from abc import ABC


class Strategy(ABC):
    @abc.abstractmethod
    def logic(self): pass


class Strategy1(Strategy):
    def logic(self):
        return "strategy 1"


class Strategy2(Strategy):
    def logic(self):
        return "strategy 2"

if __name__ == '__main__':

    strategy = "strategy2"
    print(
        eval(strategy.capitalize())().logic()
    )