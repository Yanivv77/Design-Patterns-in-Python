# Design-Patterns-in-Python

# [SOLID](https://github.com/Yanivv77/Design-Patterns-in-Python/tree/main/01_Solid)
  - Five design principles intended to make object-oriented designs more understandable, flexible, and maintainable 

# Creational Design Patterns:
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
  - [Singleton](/05_Singleton)
    - Different realizations of Singleton: custom allocator, decorator, metaclass
    - Laziness is easy, just init on first request
    - Monostate variation
    - Testability issues

# Structural Design Patterns: 
  - [Adapter](/06_Adapter)
    - Implementing an Adapter is easy
    - Determine the API you have and the API you need
    - Create a component which aggregates (has a reference to, ...)
    - Intermediate representations can pile up: use caching and other optimizations
  - [Bridge](/07_Bridge)
    - Decouple abstraction from implementation
    - Both can exist as hierarchies
    - A stronger form of encapsulation
  - [Composite](/08_Composite)
    - Objects can use other objects via inheritance/composition
    - Some composed and singular objects need similar/identical behaviors
    - Composite design pattern lets us treat both types of objects uniformly
    - Python supports iteration with \_\_iter\_\_ and Iterable ABC
    - A single object can itself iterable by yielding self from \_\_iter\_\_
  - [Decorator](/09_Decorator) 
    - A decorator keeps the reference to the decorated object(s)
    - Adds utility attributes and methods to augment the object's features
    - May or may not forward calls to the underlying object
    - Proxying of underlying calls can be done dynamically
    - Python's functional decorators wrap functions; no direct relation to the GoF Decorator Pattern
  - [Facade](/10_Facade)
    - Build a Facade to provide a simplified API over a set of classes
    - May wish to (optionally) expose internals through the facade
    - May allow users to 'escalate' to use more complex API
 - [Flyweight](/11_Flyweight)
    - Store common data externally
    - Specify an index or a reference into the external data store
    - Define the idea of 'ranges' on homogeneuous collections and store data related to those ranges
  - [Proxy](/12_Proxy)
    - A proxy has the same interface as underlying object
    - To create a proxy, simple replicate the existing interface of an object
    - Add relevant functionality to the redefined member functions
    - Different proxies (communications, logging, caching, etc.) have completely different behaviors

  # Behavioral Design Patterns
  - [Chain of Responsibility](/13_Chain_of_Responsibility)
    - Chain of responsibility can be implemented as a chain of references or
      a centralized construct
    - Enlist objects in the chain, possibly controlling their order
    - Object removal from chain (e.g., \_\_exit\_\_)
  - [Command](/14_Command)
    - Encapsulate all details of an operation in a separate object
    - Define instruction for applying the command (either in the command itself, or elsewhere)
    - Optionally define instructions for undoing the command
    - Can create composite commands (a.k.a. macros)
  - [Interpreter](/15_Interpreter)
    - Barring simple cases, an interpreter acts in two stages
    - Lexing turns text into a set of tokens
    - Parsing tokens into meaningful construct
  - [Iterator](/16_Iterator)
    - An iterator specified how you can traverse an object
    - Stateful iterators cannot be recursive
    - yield allows for much more succinct iteration
  - [Mediator](/17_Mediator)
    - Create the mediator and have each object in the system refer to it
      - E.g., in a property
    - Mediator engages in bidirectional communication with its connected components
    - Mediator has functions the components can call
    - Components have functions the mediator can call
    - Event processing (e.g., Rx) libraries make communication easier to implement
  - [Memento](/18_Memento)
    - Mementos are used to roll back states arbitrarily
    - A memento is simply a token/handle class with typically no function of its own
    - A memento is not required to expose directly the state(s) to which it reverts the system
    - Can be used to implement undo/redo
  - [Observer](/19_Observer)
    - Observer is an intrusive approach: an observable must provide an event to subscribe to
    - Subsciption and unsubscription with additional/removal of items in list
    - Property notifications are easy: dependent property notifications are tricky
  - [State](/20_State)
    - Given sufficient complexity, it pays to formally define possible states and events/triggers
    - Can define
      - State entry/exit behaviors
      - Action when a particular event causes a transition
      - Guard conditions enabling/disabling a transition
      - Default action when no transitions are found for an event
  - [Strategy](/21_Strategy)
    - Define an algorithm at a high level
    - Define the interface you expect each strategy to follow
    - Provide for dynamic composition of strategies in the resulting object
  - [Template](/22_Template_Method)
    - Define an algorithm at a high level in parent class
    - Define constituent parts as abstract methods/properties
    - Inherit the algorthm class, providing the necessary ovverides
  - [Visitor](/23_Visitor)
    - OOP double-dispatch approach is not necessary in Python
    - Make a visitor, decorating each 'overload' with @visitor
    - Call visit() and the entire structure gets traversed

    ## Awknowledgement

- Dmitri Nesteruk's course "Design Patterns in Python" on Udemy.com