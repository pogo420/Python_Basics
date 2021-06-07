# chaining responsibility , divide and conquer of large responsibility into multiple
# Beam uses
# Modification: each handler decides either to process the request or to pass it to the next handler in the chain.

from typing import List


class NumData:
    def __init__(self, num_data):
        self.num_data = num_data

    def __str__(self):
        return f"""NumData { {"num_data":self.num_data} }"""


class NumModifier:
    def __init__(self, num_data: NumData):
        self.num_data = num_data

    def handle(self): pass


class DoubleNumModifier(NumModifier):

    def handle(self):
        self.num_data.num_data *= 2
        return self.num_data


class Broker:
    def __init__(self, num_data: NumData):
        self.num_data = num_data
        self.process_list: List[NumModifier] = []

    def add_process(self, process: NumModifier):
        self.process_list.append(process)
        return self

    def process(self):
        temp = None
        for process in self.process_list:
            if not temp:
                temp = process(self.num_data).handle()
                continue
            temp = process(temp).handle()
        return temp


if __name__ == "__main__":
    num = NumData(9)
    result = Broker(num) \
        .add_process(DoubleNumModifier)\
        .add_process(DoubleNumModifier). \
        process()
    print(result)
