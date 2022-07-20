# Design-Patterns-in-Python

- [SOLID](https://github.com/Yanivv77/Design-Patterns-in-Python/tree/main/01_Solid)
  - Five design principles intended to make object-oriented designs more understandable, flexible, and maintainable 

- Creational Design Patterns:
  - [Builder](/02_Builder)
    - A builder is a separate component for building an object
    - Can either give builder an initializer or return it via a static function
    - To make builder fluent, return self
    - Different facets of an object can be built with different builders working in tandem via a base class
  - [Factories (Factory Method and Abstract Factory)](/03_Factories)
    - A factory method is a static method that creates object
    - A factory is an entity that can take care of object creation
    - A factory can be external or reside inside the object as an inner class
    - Hierarchies of factories can be used to create related objects
  - [Prototype](/04_Prototype)
    - To implement a prototype, partially construct an object and store it somewhere
    - Deep copy the prototype
    - Customize the resulting instance
    - A factory provides a convenient API for using prototypes
  - Creational Design Patterns:
  - [Singleton](/05_Singleton)
    - Different realizations of Singleton: custom allocator, decorator, metaclass
    - Laziness is easy, just init on first request
    - Monostate variation
    - Testability issues

- Structural Design Patterns: 
  - [Adapter](/06_Adapter)
    - Implementing an Adapter is easy
    - Determine the API you have and the API you need
    - Create a component which aggregates (has a reference to, ...) the adaptee
    - Intermediate representations can pile up: use caching and other optimizations
  - [Bridge](/07_Bridge)
    - Decouple abstraction from implementation
    - Both can exist as hierarchies
    - A stronger form of encapsulation