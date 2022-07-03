from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.size = size
        self.color = color
        self.name = name


class ProductFilter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color:
                yield p

    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size:
                yield p

    def filter_by_size_and_color(self, products, size, color):
        for p in products:
            if p.color == color and p.size == size:
                yield p


# Enterprise Patterns: Specification
class Specification:
    def is_satisfied(self, item):
        pass

    # syntatic sugar
    def __and__(self, other):
        return AndSpecification(self, other)


class Filter:
    def filter(self, items, spec):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class AndSpecification(Specification):
    def __init__(self, spec1, spec2):
        self.spec2 = spec2
        self.spec1 = spec1

    def is_satisfied(self, item):
        return self.spec1.is_satisfied(item) and \
               self.spec2.is_satisfied(item)


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item

APPLE = Product('Apple', Color.GREEN, Size.SMALL)
TREE = Product('Tree', Color.GREEN, Size.LARGE)
HOUSE = Product('House', Color.BLUE, Size.LARGE)

PRODUCTS = [APPLE, TREE, HOUSE]
PF = ProductFilter()
print("Green products (old):")
for p in PF.filter_by_color(PRODUCTS, Color.GREEN):
    print(f' - {p.name} is green')

BF = BetterFilter()
print("Green products (new):")
GREEN = ColorSpecification(Color.GREEN)
for p in BF.filter(PRODUCTS, GREEN):
    print(f' - {p.name} is green')

print("Large products:")
LARGE = SizeSpecification(Size.LARGE)
for p in BF.filter(PRODUCTS, LARGE):
    print(f' - {p.name} is large')

print("Large blue items:")
# large_blue = AndSpecification(large, ColorSpecification(Color.BLUE))
# using python's and
large_blue = LARGE and ColorSpecification(Color.BLUE)
for p in BF.filter(PRODUCTS, large_blue):
    print(f' - {p.name} is large and blue')