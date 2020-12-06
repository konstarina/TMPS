# ***TMPS Labaratory Work #2***
# ***Structural Design Patterns***

### Author: Constantinova Carina
----

## Objectives:

* Get familiar with the Structural Design Patterns;
* As a continuation of the previous laboratory work;
* Implement at least 3 CDPs for the specific domain;

## Creational Design Pattern:
 - [x] Adapter
 - [ ] Bridge
 - [ ] Composite
 - [x] Decorator
 - [x] Flyweight
 - [ ] Proxy

## Implementation:
#### Adapter
Adapter is a structural design pattern that allows objects with incompatible interfaces to collaborate.
The adapter design pattern solves these problems:
* How can a class be reused that does not have an interface that a client requires?
* How can classes that have incompatible interfaces work together?
* How can an alternative interface be provided for a class?
```python 
class ClassBAdapter(IA):
    def __init__(self):
        self.class_b = ClassB()

    def method_a(self):
        """calls the class b method_b instead"""
        self.class_b.method_b()

```
[Screenshot](adapter.png)

#### Decorator
The decorator pattern is a structural pattern, that allows you to attach additional responsibilities to an object at run time.
The decorator pattern is used in both the Object Oriented and Functional paradigms.
The decorator pattern is different than the Python language feature of Python Decorators in it’s syntax, but the application of it is the same, in the way that it is essentially a wrapper.
The Decorator pattern adds extensibility, without modifying the original function.
```python
class HavingAccountant:
    def __init__(self, business):
        self.business = business
        business.business_plan = False

    def get_money(self, profit):
        return "good" if profit == "stable" else self.business.get_money(profit)


class BusinessPlan:
    def __init__(self, business):
        self.business = business
        business.business_plan = True

    def get(self):
        return self.business.get().replace("Without business plan", "With business plan")

    def get_money(self, profit):
        return "great" if profit == "huge" else self.business.get_money(profit)
```
[Screenshot](decorator.png)

#### Flyweight
Flyweight is a structural design pattern that lets you fit more objects into the available amount of RAM by sharing common parts of state between multiple objects instead of keeping all of the data in each object.
For more convenient access to various flyweights, you can create a factory method that manages a pool of existing flyweight objects. The method accepts the intrinsic state of the desired flyweight from a client, looks for an existing flyweight object matching this state, and returns it if it was found. If not, it creates a new flyweight and adds it to the pool.

There are several options where this method could be placed. The most obvious place is a flyweight container. Alternatively, you could create a new factory class. Or you could make the factory method static and put it inside an actual flyweight class.

```python
class FlyweightFactory:
    _flyweights: Dict[str, Flyweight] = {}

    def __init__(self, initial_flyweights: Dict) -> None:
        for state in initial_flyweights:
            self._flyweights[get_key(state)] = Flyweight(state)

```
Added to class ChocolateFactory from CDPs
```python
    def get_flyweight(self, param):
        pass
```
[Screenshot](flyweight.png)
----------------
Thank you!
