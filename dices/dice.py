import random


class Dice(object):
    def __init__(self, sides: int = 6) -> None:
        self.sides = sides

    def roll(self) -> int:
        return random.randint(1, self.sides)

    def __str__(self) -> str:
        return f"Dice({self.sides})"
    
    def explain(self) -> str:
        return str(self)