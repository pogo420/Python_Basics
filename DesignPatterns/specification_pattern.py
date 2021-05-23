# Perfect example for OCP
# Specification pattern: Multiple permutation & combination of business rules.
# Filtering data based on multiple logics.
# Specification: Object properties and is satisfied
# Filter filtering objects based on spec
# Perfect in cases for data objects and we are doing filtering

from enum import Enum
from typing import List


class Color(Enum):
    RED = 0
    YELLOW = 1
    GREEN = 2


class Size(Enum):
    SMALL = 0
    MEDIUM = 1
    LARGE = 2


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

    def __str__(self) -> str:
        return f"""Product{ {"name": self.name,
                             "colour": self.color,
                             "size": self.size}
        }"""


class Specification:

    def is_satisfied(self, spec) -> bool:
        raise NotImplementedError()

    def __and__(self, other: 'Specification'):
        return AndSpecification(self, other)


class AndSpecification(Specification):

    def __init__(self, spec1: Specification, spec2: Specification):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied(self, item: Product) -> bool:
        return self.spec1.is_satisfied(item) and self.spec2.is_satisfied(item)


class Filter:
    def filter(self, item: List[Product], spec: Specification):
        raise NotImplementedError()


class ProductFilter(Filter):
    def filter(self, item: List[Product], spec: Specification):
        for it in item:
            if spec.is_satisfied(it):
                yield it


class ColorSpecification(Specification):
    def __init__(self, color: Color):
        self.color = color

    def is_satisfied(self, item: Product) -> bool:
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size: Size):
        self.size = size

    def is_satisfied(self, item: Product) -> bool:
        return item.size == self.size


class NameSpecification(Specification):
    def __init__(self, name: str):
        self.name = name

    def is_satisfied(self, item: Product) -> bool:
        return item.name == self.name


green_spec = ColorSpecification(Color.GREEN)
medium_spec = SizeSpecification(Size.MEDIUM)
name_spec = NameSpecification('Tree')

medium_green = (green_spec & medium_spec & name_spec)

apple = Product('Apple', Color.GREEN, Size.SMALL)
tree = Product('Tree', Color.GREEN, Size.LARGE)
tree2 = Product('Tree', Color.GREEN, Size.MEDIUM)
house = Product('House', Color.RED, Size.LARGE)

products = [apple, tree, tree2, house]

pf = ProductFilter()
for p in pf.filter(products, medium_green):
    print(p)
