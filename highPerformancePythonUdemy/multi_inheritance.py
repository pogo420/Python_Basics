from abc import ABC, abstractmethod

# https://www.linkedin.com/feed/update/urn:li:groupPost:25827-6831568259796619264/

class TypeBase(ABC):
    # interface
    @abstractmethod
    def get_type(self, obj): pass


class IntegerBase(TypeBase):
    def get_type(self, obj):
        if isinstance(obj, int):
            return "Integer"
        return super().get_type(obj)


class StringBase(TypeBase):
    def get_type(self, obj):
        if isinstance(obj, str):
            return "String"
        return super().get_type(obj)


class DataType(IntegerBase, StringBase):
    def get_type(self, obj):
        return super().get_type(obj)


if __name__ == '__main__':
    print(DataType().get_type("23"))
    print("-----------------------------")
    print(DataType().get_type(23))
    print(DataType.__mro__)
