from behavioral.abstractions.publisher import Publisher
from creational.builder import MilkaDirector


class FactoryAccountant(Publisher):
    def __init__(self):
        self.factory = MilkaDirector

    def update(self, subscriber):
        print("Factory Accountant " + self.factory + " was notified about coming of the Revenue Service. " + subscriber)
