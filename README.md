# Design-Patterns-in-Python

- [SOLID](https://github.com/Yanivv77/Design-Patterns-in-Python/tree/main/01_Solid)
  - Five design principles intended to make object-oriented designs more understandable, flexible, and maintainable 
- Creational Design Patterns:
  - [Builder](/builder)
    - A builder is a separate component for building an object
    - Can either give builder an initializer or return it via a static function
    - To make builder fluent, return self
    - Different facets of an object can be built with different builders working in tandem via a base class
  - [Factories (Factory Method and Abstract Factory)](/factories)
    - A factory method is a static method that creates object
    - A factory is an entity that can take care of object creation
    - A factory can be external or reside inside the object as an inner class
    - Hierarchies of factories can be used to create related objects