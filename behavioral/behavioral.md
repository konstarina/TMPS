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

## How it works for my system
Previously, I have implemented Chocolate Factory and Stores where all the products are created, stored, and sold in Creational DP. Later, there was also implemented Bussiness Model for the owners of the factory and stores in Structural DP. Now I added to CDP a notifiying system, where the accountants of the business are created, notified when the revenue service comes and when it is needed to pay the bills in the file factory_check.py : 
```python
def notify(self, event):
        print("Subject: Notifying accountants...\n")
        for publisher in self._publishers:
            publisher.update(event)

    def new_taxer(self, taxer):
        print("A new taxer has arrived to your factory")
        self.taxers.append(taxer)
        event = taxer.factory + " have come with new revenue checks\n" #a taxer
        self.notify(event)

    def new_manager(self, accountant):
        print("A new accountant for your factory")
        self.accountants.append(accountant)
        event = accountant.factory + " is a new accountant\n" #created an accountant
        self.notify(event)
```
Here is the process how a factory director is notified of current events in owner.py:
```python
from behavioral.abstractions.publisher import Publisher
from creational.builder import MilkaDirector


class Owner(Publisher):
    factory: object

    def __init__(self) -> object:
        self.factory = MilkaDirector

    def update(self, subscriber):
        print("The " + self.factory + " was notified. " + subscriber)
```
The result:
![](main.png)
