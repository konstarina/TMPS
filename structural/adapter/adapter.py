"""
Adapter Design Pattern
"""

from abc import ABCMeta, abstractmethod


class IA(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def method_a():
        """An abstract method A"""


class ClassA(IA):
    def method_a(self):
        print("The chocolate store that still did not elaborate their goals in the business plan")


class IB(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def method_b():
        """An abstract method B"""


class ClassB(IB):
    def method_b(self):
        print("The chocolate store that has a business plan, helping out to enhance the business")


"""ClassB does not have a method_a, so we create an adapter"""


class ClassBAdapter(IA):
    def __init__(self):
        self.class_b = ClassB()

    def method_a(self):
        """calls the class b method_b instead"""
        self.class_b.method_b()


#client code

#ITEM = ClassA()
#ITEM = ClassB()  # has no method_a
ITEM = ClassBAdapter()

ITEM.method_a()
