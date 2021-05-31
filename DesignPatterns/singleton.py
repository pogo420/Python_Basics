# Single object in a lifecycle
# Careful with testing: Make sure we have 1 singleton for test and 1 for prod.

def decorator(class_):  # class object
    instance = {}  # dictionary for {class -> object}

    def inner(*args, **kwargs):  # class constructor arguments
        if not instance.get(class_):  # is instance is not created
            instance[class_] = class_(*args, **kwargs)  # create an instance
        return instance[class_]

    return inner


@decorator
class Database:

    def __init__(self, i):
        print("Connecting to DB")


# Mono State, Variation of singleton where state of
class MonoState:
    __shared_state = {}

    def __new__(cls, *args, **kwargs):
        # static method is called when object is created
        obj = super().__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__shared_state
        return obj


class CFO(MonoState):

    def __init__(self):
        self.name = ""
        self.money=0

    def __str__(self):
        return f"""CFO { {
            "name": self.name,
            "money": self.money} } """


class ObjectTest:

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)


if __name__ == "__main__":
    d1 = Database(1)
    d2 = Database(2)
    print(d1 == d2)

    # Mono state example
    cfo1 = CFO()
    cfo2 = CFO()
    print(cfo1, cfo2)
    cfo1.money = 100000
    print(cfo1, cfo2)

    print(ObjectTest())
