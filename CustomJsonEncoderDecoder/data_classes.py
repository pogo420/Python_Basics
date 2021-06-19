class Address:
    def __init__(self, pin_code: int, city: str):
        self.city = city
        self.pin_code = pin_code

    def __str__(self):
        return f"""Address { {"city": self.city, "pincode": self.pin_code} }"""


class Company:
    def __init__(self, company: str, rating: str):
        self.company = company
        self.rating = rating

    def __str__(self):
        return f"""Company { {"company": self.company, "rating": self.rating} }"""


class Person:
    def __init__(self, name: str, address: Address, company: Company):
        self.company = company
        self.address = address
        self.name = name

    def __str__(self):
        return f"""Person { {"name": self.name, "company": str(self.company), "address": str(self.address)} }"""


if __name__ == '__main__':
    address_ = Address(560089, "BLR")
    company_ = Company("Zebra", "5")
    person_ = Person("arnab", address_, company_)
    print(person_)

