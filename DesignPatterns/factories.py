# component for creating wholesale objects
# Any method creating an object -> Factory method
# Class containing all factory methods -> Factory

import abc
from abc import ABC
from enum import Enum, auto


class Drinks(Enum):
    Tea = auto()


class HotDrink(ABC):
    @abc.abstractmethod
    def consume(self):
        pass


class HotDrinkFactory(ABC):
    @abc.abstractmethod
    def prepare(self, water):
        pass


class Tea(HotDrink):
    def consume(self):
        print("tea is delicious")


class TeaFactory(HotDrinkFactory):
    def prepare(self, water):
        f"Add tea with water: {water} ml"
        return Tea()


def make_drink(idx):
    factory_instance = []
    for drink in Drinks:
        factory_instance.append(
            (drink.name+"Factory", eval(drink.name+"Factory")())
        )
    return factory_instance[idx][1].prepare(10).consume()


if __name__ == "__main__":
    make_drink(0)
