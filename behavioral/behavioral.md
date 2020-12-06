# ***TMPS Laboratory Work #3***
# ***Behavioral Design Patterns***

### Author: Constantinova Carina
----

## Objectives:

* Get familiar with the Behavioral Design Patterns;
* As a continuation of the previous laboratory work, think about what communication between software entities might be involed in my system;
* Implement some additional functionalities using behavioral design patterns;

## Behavioral Design Pattern:
 - [ ] Command
 - [ ] Interpreter
 - [ ] Iterator
 - [ ] Mediator
 - [x] Publisher
 - [ ] Strategy

## Implementation:
#### Observer
The observer pattern is a software design pattern in which an object, called the subject or observable, manages a list of dependents, called observers, and notifies them automatically of any internal state changes, and calls one of their methods.
There are created two classes:
```python 
class Subscriber(ABCMeta):
    @abstractmethod
    def attach(self, publisher: Publisher):
        pass

    @abstractmethod
    def detach(self, publisher: Publisher):
        pass

    @abstractmethod
    def notify(self):
        pass


class Publisher(ABCMeta):
    @abstractmethod
    def update(self, subscriber: Subscriber):
        pass
```
The classical ones: Observable(Subscriber) and Observers(Publisher)
