# classes and representations of cats
from cats import cats

class Cat:
    def __init__(self, name: str, breed: str, color: str, age: int, personality: str ):
        self.name = name
        self.breed = breed
        self.color = color
        self.age = age
        self.personality = personality

    def __repr__(self) -> str:
        pass