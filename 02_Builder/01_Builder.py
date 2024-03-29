# simple scenario
TEXT = 'hello'
PARTS = ['<p>', TEXT, '</p>']
print(''.join(PARTS))

# more complicated
WORDS = ['hello', 'world']
PARTS = ['<ul>']
for w in WORDS:
    PARTS.append(f'\t<li>{w}</li>')
PARTS.append('</ul>')
print('\n'.join(PARTS))


class HtmlElement:
    indent_size = 2

    def __init__(self, name="", text=""):
        self.name = name
        self.text = text
        self.elements = []

    def __str(self, indent):
        lines = []
        i = ' ' * (indent * self.indent_size)
        lines.append(f'{i}<{self.name}>')

        if self.text:
            i1 = ' ' * ((indent + 1) * self.indent_size)
            lines.append(f'{i1}{self.text}')

        for e in self.elements:
            lines.append(e.__str(indent + 1))

        lines.append(f'{i}</{self.name}>')
        return '\n'.join(lines)

    def __str__(self):
        return self.__str(0)

    @staticmethod
    def create(name):
        return HtmlBuilder(name)


class HtmlBuilder:
    __root = HtmlElement()

    def __init__(self, root_name):
        self.root_name = root_name
        self.__root.name = root_name

    # not fluent
    def add_child(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )

    # fluent
    def add_child_fluent(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )
        return self

    def clear(self):
        self.__root = HtmlElement(name=self.root_name)

    def __str__(self):
        return str(self.__root)


BUILDER = HtmlBuilder('ul')
BUILDER.add_child('li', 'hello')
BUILDER.add_child('li', 'world')
print('Ordinary builder:')
print(BUILDER)

# chaining methods
FLUENT = HtmlBuilder('ul')
FLUENT.add_child_fluent('li', 'hello').add_child_fluent('li', 'world')
print('Fluent builder:')
print(FLUENT)

# create
CREATED = HtmlElement.create('ul')
CREATED.add_child_fluent('li', 'python')
print('Created builder:')
print(CREATED)