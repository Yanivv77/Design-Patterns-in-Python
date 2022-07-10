import copy


class Address:
    def __init__(self, street_address, city, country):
        self.city = city
        self.street_address = street_address
        self.country = country

    def __str__(self):
        return f'{self.street_address}, {self.city}, {self.country}'


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} lives at {self.address}'


JOHN = Person('John', Address('123 London Road', 'London', 'UK'))
print(JOHN)

# does not work
# JANE = JOHN
# JANE.name = JOHN

# need to make deep copy
JANE = copy.deepcopy(JOHN)
JANE.name = 'Jane'
JANE.address.street_address = '124 London Road'
print(JANE)