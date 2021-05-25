# Builder implementation details

class Person:

    def __init__(self):
        self.name = ""
        self.age = 0
        self.address = ""
        self.company = ""
        self.salary = 0.0

    def __str__(self):
        return f"""Person{
        {"name": self.name,
        "age": self.age,
        "address": self.address,
        "company": self.company,
        "salary": self.salary}
        }"""

    @staticmethod
    def builder() -> 'PersonBuilder':
        return PersonBuilder()


class PersonBuilder:

    def __init__(self, person_=Person()):
        self.person = person_

    def name(self, name):
        self.person.name = name
        return self

    def address(self, address):
        self.person.address = address
        return self

    def build(self):
        return self.person


person = Person.builder().name("Ola").address("2389").build()
print(person)
