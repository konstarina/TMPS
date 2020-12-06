from structural.abstractions.composite import CompositeInterface
from abc import ABC


class WorkingSpace(CompositeInterface, ABC):
    def get_business(self, type):
        types = {"home": "small", "store": "mediocre", "plant": "big", "gigafactory": "huge"}
        return types[type]


class Store(WorkingSpace):
    def __init__(self,  address, meters):
        self.address = address
        self.meters = meters
        self.cashiers = True
        self.cleaners = True
        self.accountants = True

    def get_area(self):
        return self.meters ** 2

