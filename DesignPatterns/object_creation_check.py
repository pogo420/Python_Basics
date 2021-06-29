class ClassDummy:
    def __new__(cls, *args, **kwargs):
        print("__new__")
        return super().__new__(cls,*args, **kwargs)
        # return None
        # return 90

    def __init__(self):
        print("__init__")


if __name__ == '__main__':
    ClassDummy()
