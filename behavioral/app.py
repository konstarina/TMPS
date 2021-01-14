from behavioral.implementation.owner import Owner
from behavioral.implementation.revenue_service import FactoryAccountant
from behavioral.implementation.factory_check import FactoryOwner


def if_subscribe(factory_accountant, person):
    val = input("Do you want to subscribe to block's updates? ").lower()
    if val == "yes" or val == "y":
        factory_accountant.attach(person)


if __name__ == "__main__":
    factory_check = FactoryOwner()
    while True:
        print("Print yes if a revenue service came this quarter")
        print("Print no to assign an accountant for this deal")

        val = int(input())
        factory = input("Your factory name: ")

        if val == 1:
            owner = Owner()
            factory_check.new_manager(owner)
            if_subscribe(factory_check, owner)
        elif val == 2:
            manager = FactoryAccountant()
            factory_check.new_manager(manager)
            factory_check.attach(manager)
