from enum import Enum
from json import JSONEncoder, JSONDecoder, dumps, loads
from typing import Any, Dict
from data_classes import Address, Company, Person, ObjectType


# customer json encoder: Objects to Bytes
class CustomJsonEncoder(JSONEncoder):

    def default(self, o: Any) -> Any:
        if isinstance(o, Enum):
            return o.name
        if isinstance(o, (Company, Address)):
            return o.__dict__  # editable objects as key(reference name)-value(object value).
        if isinstance(o, Person):
            return {"object_type": ObjectType.Person, "name": o.name, "company": o.company, "address": o.address}
            # it won't work as expected
            # return f"""{ {"object_type": ObjectType.Person, "name": o.name, "company": o.company,
            # "address": o.address} }"""
        return super().default(o)


# custom json decoder: Bytes to Objects
class CustomJsonDecoder(JSONDecoder):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, obj: Dict):  # work perfectly with dictionary type
        if "object_type" in obj:
            return Person(obj.get("name"), obj.get("address"), obj.get("company"))
        return obj


if __name__ == '__main__':
    address_ = Address(560089, "BLR")
    company_ = Company("Zebra", "5")
    person_ = Person("Arnab", address_, company_)

    serialize: str = dumps(person_, cls=CustomJsonEncoder)
    print(
        serialize, type(serialize)
    )

    print(
        loads(serialize, cls=CustomJsonDecoder)
    )
