class Bird:
    def swim(self):
        print(f"The {self.__class__.__name__.lower()} is swimming")

    def fly(self):
        print(f"The {self.__class__.__name__.lower()} is flying")

    def eat(self):
        print(f"The {self.__class__.__name__.lower()} is eating")

    def sleep(self):
        print(f"The {self.__class__.__name__.lower()} is sleeping")

    def make_sound(self):
        print(f"The {self.__class__.__name__.lower()} is making a sound")

    def flap_wing(self):
        print(f"The {self.__class__.__name__.lower()} is flapping it's wings")


class Duck(Bird):
    pass


class Crow(Bird):
    pass


class Mallard(Duck):
    pass


# Testing the classes
duck = Duck()
crow = Crow()
mallard = Mallard()

duck.swim()  # Output: The duck is swimming
duck.fly()  # Output: The duck is flying

crow.swim()  # Output: The crow is swimming
crow.fly()  # Output: The crow is flying

mallard.swim()  # Output: The mallard is swimming
mallard.fly()  # Output: The mallard is flying

# add a new behavior from the class

mallard.flap_wing()
