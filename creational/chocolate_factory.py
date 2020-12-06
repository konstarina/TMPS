from abc import ABCMeta


class IChocolate(metaclass=ABCMeta):
    @staticmethod
    def get_information():
        """"The Chocolate Interface"""


class DarkChocolate(IChocolate):

    def __init__(self):
        self.cacao = 70
        self.carbs = 45
        self.fat = 38
        self.protein = 8

    def get_information(self):
        return {"cacao": self.cacao, "carbohydrates": self.carbs, "fats": self.fat, "proteins": self.protein}


class MilkChocolate(IChocolate):

    def __init__(self):
        self.cacao = 30
        self.carbs = 59
        self.fat = 29
        self.protein = 6.3

    def get_information(self):
        return {"cacao": self.cacao, "carbohydrates": self.carbs, "fats": self.fat, "proteins": self.protein}


class WhiteChocolate(IChocolate):

    def __init__(self):
        self.cacao = 0
        self.carbs = 65
        self.fat = 28
        self.protein = 4.3

    def get_information(self):
        return {"cacao": self.cacao, "carbohydrates": self.carbs, "fats": self.fat, "proteins": self.protein}


class ChocolateFactory:

    @staticmethod
    def get_chocolate(chocotype):
        try:
            if chocotype == "HotIceCream":
                return DarkChocolate()
            if chocotype == "WonkaBar":
                return MilkChocolate()
            if chocotype == "ThreeCourseDinnerGum":
                return WhiteChocolate()
            raise AssertionError("Chocolate is not found")
        except AssertionError as _e:
            print(_e)

    def get_flyweight(self, param):
        pass


if __name__ == "__main__":
    CHOCO = ChocolateFactory.get_chocolate("HotIceCream")
    print("Dark Chocolate contains", CHOCO.get_information())
    CHOCO = ChocolateFactory.get_chocolate("WonkaBar")
    print("Milk Chocolate contains", CHOCO.get_information())
    CHOCO = ChocolateFactory.get_chocolate("ThreeCourseDinnerGum")
    print("White Chocolate contains", CHOCO.get_information())
