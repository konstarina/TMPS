from abc import ABCMeta


class IWonka(metaclass=ABCMeta):
    @staticmethod
    def get_information():
        """"The Chocolate Interface"""


class HotIceCream(IWonka):

    def __init__(self):
        self.cacao = 70
        self.carbs = 45
        self.fat = 38
        self.protein = 8

    def get_information(self):
        return {"cacao": self.cacao, "carbohydrates": self.carbs, "fats": self.fat, "proteins": self.protein}


class WonkaBar(IWonka):

    def __init__(self):
        self.cacao = 30
        self.carbs = 59
        self.fat = 29
        self.protein = 6.3

    def get_information(self):
        return {"cacao": self.cacao, "carbohydrates": self.carbs, "fats": self.fat, "proteins": self.protein}


class ThreeCourseDinnerGum(IWonka):

    def __init__(self):
        self.flavour = "unknown"
        self.first = "tomato soup"
        self.second = "roast beef"
        self.stage = "experimental"

    def get_information(self):
        return {"Number of flavour": self.flavour, "first dish": self.first, "second dish": self.second, "stage": self.stage}


class WonkaFactory:

    @staticmethod
    def get_chocolate(chocotype):
        try:
            if chocotype == "HotIceCream":
                return HotIceCream()
            if chocotype == "WonkaBar":
                return WonkaBar()
            if chocotype == "ThreeCourseDinnerGum":
                return ThreeCourseDinnerGum()
            raise AssertionError("Chocolate is not found")
        except AssertionError as _e:
            print(_e)


if __name__ == "__main__":
    CHOCO = WonkaFactory.get_chocolate("HotIceCream")
    print("Hot Ice-cream contains", CHOCO.get_information())
    CHOCO = WonkaFactory.get_chocolate("WonkaBar")
    print("Wonka Chocolate  bar contains", CHOCO.get_information())
    CHOCO = WonkaFactory.get_chocolate("ThreeCourseDinnerGum")
    print("Three Course Dinner Gum contains", CHOCO.get_information())
