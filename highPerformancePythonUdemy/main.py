
# exception
try:
    print("unreachable")
except:
    print("Runs when there is issue")
else:
    print("Runs when there is no issue")
finally:
    print("Runs always")


class TestContext:

    def __init__(self):
        self.data=[]

    def __enter__(self):
        # must return the object, it will be assigned to with variable
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.data.clear()
        del self.data

    def inc_int(self, val: int):
        self.data.append(val)


if __name__ == '__main__':

    with TestContext() as a:
        a.inc_int(1)
        a.inc_int(4)
        print(a.data)

