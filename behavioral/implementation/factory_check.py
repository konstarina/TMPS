from behavioral.abstractions.publisher import Subscriber, Publisher
from abc import ABCMeta, abstractmethod
from typing import List


class FactoryOwner(Subscriber, ABCMeta):
    taxers = []
    accountants = []
    _publishers: List[Publisher] = []

    def attach(self, publisher: Publisher):
        print("Subject: Attached a new taxer.")
        self._publishers.append(publisher)

    def detach(self, publisher: Publisher):
        self._publishers.remove(publisher)

    def notify(self, event):
        print("Subject: Notifying accountants...\n")
        for publisher in self._publishers:
            publisher.update(event)

    def new_taxer(self, taxer):
        print("A new taxer has arrived to your factory")
        self.taxers.append(taxer)
        event = taxer.factory + " have come with new revenue checks\n"
        self.notify(event)

    def new_manager(self, accountant):
        print("A new accountant for your block")
        self.accountants.append(accountant)
        event = accountant.factory + " is a new accountant\n"
        self.notify(event)
