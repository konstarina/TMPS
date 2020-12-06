from abc import ABCMeta
from creational.chocolate_factory import ChocolateFactory
from creational.wonka_factory import WonkaFactory


class ISweetsFactory(metaclass=ABCMeta):
    """Sweets Factory Interface"""

    @staticmethod
    def get_sweets(sweets_type):
        """The static factory interface method"""


class SweetsFactory(ISweetsFactory):

    @staticmethod
    def get_sweets(sweets_type):
        try:
            if sweets_type in ["DarkChocolate", "MilkChocolate", "WhiteChocolate"]:
                return ChocolateFactory.get_chocolate(sweets_type)
            if sweets_type in ["HotIceCream", "WonkaBar", "ThreeCourseDinnerGum"]:
                return WonkaFactory.get_chocolate(sweets_type)
            raise AssertionError("Cannot find sweets type")
        except AssertionError as _e:
            print(_e)
        return None


if __name__ == "__main__":
    CHOCOLATE = ChocolateFactory.get_chocolate("MilkChocolate")
    print(f"{CHOCOLATE.__class__} : {CHOCOLATE.get_information()}")
