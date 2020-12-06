from abc import ABCMeta
import copy


class IPrototype(metaclass=ABCMeta):
    """Interface with clone method"""

    @staticmethod
    def clone():
        """The clone, deep or shallow, depends on how you want to implement the details in your concrete class """


class ConcreteClass1(IPrototype):
    """concrete class 1"""

    def __init__(self, i=0, s="", l=[], d={}):
        self.i = i
        self.s = s
        self.l = l
        self.d = d

    def clone(self):
        return type(self)(
            self.i,
            self.s,
            self.l.copy(),
            self.d.copy()
        )

    def __str__(self):
        return f"{id(self)}\ti={self.i}\ts={self.s}\tl={self.l}\td={self.d}"


class ConcreteClass2(IPrototype):
    """concrete class 2"""

    def __init__(self, i=0, s="", l={}, d=[]):
        self.i = i
        self.s = s
        self.l = l
        self.d = d

    def clone(self):
        return type(self)(
            self.i,
            self.s,
            copy.deepcopy(self.l),
            copy.deepcopy(self.d)
        )

    def __str__(self):
        return f"i={self.i}\t\ts={self.s}\tl={self.l}\td={self.d}\n{id(self.i)}" \
               f"\t{id(self.s)}\t{id(self.l)}\t{id(self.d)}\t"


if __name__ == "__main__":
    OBJECT1 = ConcreteClass1(
        1,
        "TWIN 1",
        {"height": 173, "weight": 60, "age": 20},
        [1, 2, 3]
    )
    print(f"OBJECT1 {OBJECT1}")

    OBJECT2 = OBJECT1.clone()
    OBJECT2.s = "TWIN 2"
    OBJECT2.i = 2
    print(f"OBJECT1 {OBJECT1}")
    print(f"OBJECT2 {OBJECT2}")
