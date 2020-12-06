from behavioral.abstractions.publisher import Publisher
from creational.builder import MilkaDirector


class Owner(Publisher):
    factory: object

    def __init__(self) -> object:
        self.factory = MilkaDirector

    def update(self, subscriber):
        print("The " + self.factory + " was notified. " + subscriber)
