# Template
 * Allows us to define the 'skeleton' of the algorithm, with concrete
  implementations kept in subclass

## Why to use Template pattern
- Algorithms can be decomposed into common parts + specifics
- Strategy pattern does this through composition
  - High-level algorithm expects strategies to conform to an interface
  - Concrete implementations implement the interface
- Template Method does the same thing through inheritance
  - Overall algorithm defined in base class; makes use of abstract members
  - Inheritors ovveride the abstract methods
  - Template method invoked to get work done