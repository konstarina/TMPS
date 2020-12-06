from functools import reduce
from abc import ABC


class CompositeInterface:
    def get_area(self):
        pass


class Composite(CompositeInterface, ABC):
    def get_area(self):
        return reduce((lambda x, y: x + y.get_area()), self._children, 0)
