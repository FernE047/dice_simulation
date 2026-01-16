from abc import ABC, abstractmethod
import random


class BaseDice(ABC):
    """Base class for all dice types."""

    def __init__(self) -> None:
        self.max_side: float = 0.0

    @abstractmethod
    def roll(self) -> int:
        """Roll the dice and return a value."""
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


class Dice(BaseDice):
    """Dice with arbitrary side values."""

    def __init__(self, sides: list[int]) -> None:
        self.sides = sides

    def roll(self) -> int:
        return random.choice(self.sides)

    def __str__(self) -> str:
        return f"Dice({self.sides})"


class SequentialDice(Dice):
    """Traditional dice with sequential sides (1 to N)."""

    def __init__(self, num_sides: int = 6) -> None:
        self.num_sides = num_sides
        self.dice = Dice(list(range(1, num_sides + 1)))

    def roll(self) -> int:
        return self.dice.roll()

    def __str__(self) -> str:
        return f"SequentialDice({self.num_sides})"
