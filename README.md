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

## Patterns
1. Strategy Pattern: defines a family of algorithms, encapsulates each one, and makes them interchangeable.
2. Observer Pattern: defines a one to many dependency between objects so that when one object (the _subject_) changes state, the dependents (_observers_) are notified and updated
3. Dectorator pattern: attaches additional responsibilities to an object fynamically. a flecible alternative to subclassing for extending functionality

### observer pattern
1. subject interface, implemented by concrete subjects. has methods for registeringObserver, removing observer, notifying observer
2. observer interface, just one method: update()
3. concrete subjects implement the 3 methods from the interface, and probably has some kind of get and set state methods.
4. concrete observers implement update(), and has methods for whatever it is the concrete observer does with the data
5. the goal is that the objects and subjects are loosely coupled.

### decorator pattern
1. take a darkroast coffee object, decorate it with a cream object, then a sugar object, then call the cost() method and rely on delegation to tell you what the cost of a darkroast coffee with cream and sugar costs.
2. decorating, or wrapping, relies on polymorphism: the wrapper and wrapped objects are both subclasses of the same superclass, so you can treat them similarly
3. the decorator will add it's own behaviour before or after delegating to the object it decorates
4. the implementation in: you have a compontent class, a contretecomponent class which extends it
5. note you're using inheritence, and inheritence can be bad, but here we're using it achieve type matching and polymorphism, we're not trying to inherit behaviour. you could totally use an interface though.
