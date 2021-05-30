# single object in a lifecycle


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


if __name__ == "__main__":
    d1 = Database(1)
    d2 = Database(2)

    print(d1 == d2)
