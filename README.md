# Notes on design patterns

## The problems with inheritance
* the expectation of reuse is broken if you have to override behavior a lot
* runtime behaviour changes are difficult
* changes to the superclass may impact children classes in unexpected ways

## the benefits of loose coupling
* it means that a class need only know a very limited amount about other classes: what interfaces they implement
* it means you are more flexible at runtime.
* you can reuse more code

## OO basics
* Abstraction
* Encapsulation
* polymorphism
* inheritance

## Object Oriented Design Principles
* pull out and encapsulate parts of your code that will change over time so it won't affect the rest of your code, and so that you can extend the parts that change without affecting those that don't
* Program to an interface, not an implementation
* favor composition over inheritence. Composition is when you put two classes together to get the overall behavior you want. Instead of _inheriting_ behaviour, your objects are _composed_ with the right behaviour classes. This provides you with flexibility at runtime.
* strive for loosely couple designs between objects that interact
* open-closed principle: classes should be open for extension but open for modification. We want to incorporate new behaviour without modifying old code.
* dependency inversion principle: import abstractions, don't import concrete classes. High level components shouldn't depend on low level components. Both should depend on abstractions.
* Principle of least knowledge (aka law of Demeter): talk only to your immediate friends. A class should only interact with a few other classes. No calling methods of objects you get by calling other ojects. You should only invoke methods that belong to
	* the object itself
	* objects passed in as a parameter to the method
	* any object the method creates
	* any components of the object

### guidelines for not violating the DIP
1. no variable should hold a reference to a concrete class (i.e. use a factory)
2. no class should derive from a concrete class (inheritence is a dependency)
3. no method should override an implemented method of it's base class (that would imply it's not a proper abstraction)a

## Patterns
1. Strategy Pattern: defines a family of algorithms, encapsulates each one, and makes them interchangeable.
2. Observer Pattern: defines a one to many dependency between objects so that when one object (the _subject_) changes state, the dependents (_observers_) are notified and updated
3. Dectorator pattern: attaches additional responsibilities to an object fynamically. a flecible alternative to subclassing for extending functionality
3. Factory Method Pattern: defines an interface for creating an object, but lets subclasses decide which class to instantiate. Factory Method lets a class defer instantiation to subclasses
4. Abstract Factory Pattern: provides an interface for creating families of realted or dependent objects without specifying their concrete classes
5. Singleton
6. Command Pattern
7. Adapter Pattern: converts the interface of a class into another interface the client accepts. Adapters let classes wok together that couldn't otherwise because of icompatible interfaces.
8. Facade Pattern: provides a unified interface to a set of interfaces in a subsystem. Facade defines a higher level interface that makes the subsystems easier to use.

### observer pattern
1. subject interface, implemented by concrete subjects. has methods for registeringObserver, removing observer, notifying observer
2. observer interface, just one method: update()
3. concrete subjects implement the 3 methods from the interface, and probably has some kind of get and set state methods.
4. concrete observers implement update(), and has methods for whatever it is the concrete observer does with the data
5. the goal is that the objects and subjects are loosely coupled.

### decorator pattern
. take a darkroast coffee object, decorate it with a cream object, then a sugar object, then call the cost() method and rely on delegation to tell you what the cost of a darkroast coffee with cream and sugar costs.
2. decorating, or wrapping, relies on polymorphism: the wrapper and wrapped objects are both subclasses of the same superclass, so you can treat them similarly
3. the decorator will add it's own behaviour before or after delegating to the object it decorates
4. the implementation in: you have a compontent class, a contretecomponent class which extends it
5. note you're using inheritence, and inheritence can be bad, but here we're using it achieve type matching and polymorphism, we're not trying to inherit behaviour. you could totally use an interface though.

### factory pattern 
1. when you instantiate, you are by definition coding to a concrete class. When your requirements change you will need to open your code (i.e. violate the open-closed principle)
2. a simple factory is just an encapsulation of object creation. More an idiom than a patter
3. all factory patterns encapsulate object creation

#### Factory Method Pattern
1. encapsulates object creation by letting subclasses decide what objects to create
2. There is an _abstract creator_ class, which has an _abstract factory method_ which subclasses implement. The subclasses are called _concrete creators_.
3. the abstract creator can have behavior code which isn't overidden by the concretes, but which is agnostic to the concrete type.
4. The _abstract product_ class is inherited by the _concrete product classes_.
5. the class types are parallel: the abstract creator references the abstract product, the concrete creators the concrete products

#### Abstract factory pattern
1. reducing dependecies to concrete classes is a good thing. It's called the Dependency Inversion Principle
2. an _abstract factory_ gives an interface for creating a family of products using _concrete factories._
3. as before you have _abstract products_ and _concrete products_, with your concrete factories instantiating your concrete products
4. Your concrete families produce the same products (since they implement the same abstract) but with different behaviour.
5. Our _client_ code gets composed with different factories depending on the desired behavior, but the client code itself is unchanged
6. usually there is still an abstract factory method, or several of them, in the abstract factory class.

#### differences between the two types
1. both AF and FM create objects, but FM does it through inheritence and AF does it through composition.
2. with FM, you extend a class which has an abstract factory method and implement the method, which creates the objects
3. with AF you have an abstract factory with subclasses which define how products are produced. then you instatiate one of the subclasses and pass it to code which is written against the abstract type. 
4. An AF can group together a set of related products, whereas FM is only good for a single product. But if you want to add another product to an AF, you need to change your interface, and probably all your subclasses

### What is the point of a Singleton
1. there are lots of things you need one and only one of, and if you have more than one it could cause problems. Registry settings, connections etc.
2. why not just have a global variable? it will generally be created when the app first starts, which can be undesirable.
3. One implementation: allow no direct instantiation, you get the only allowable instance with a `get_instance()` method (you need to be able to enforce a private constructor)
4. 

## Object Adapter pattern
1. a sqaure peg in a round hole - wrapping an interface in another interface which tranlastes between the client code and the original interface
2. have the adapter implement the target interface, implent all abstract methods, have a constructor which gets passed an instance of the adaptee, then have your client code initialise the adapter class, which can then be used as a instance of the target
3. if necessary you can have a 2 way adapter, which implements both interfaces
4. client creates a new instance of the adapter (`TurkeyAdapter`), but types it as a target(`Duck`), with the adapter being composed with the adaptee (`Turkey`)
5. Class adapter: slightly different, the adapter subclasses the target and adapter.
6. facade: makes an interface simpler, and in addition decouples the client from the complex and potentially changing lower level components
