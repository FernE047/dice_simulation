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

    def simulate_rolls(self, num_rolls: int) -> list[int]:
        """Simulate multiple rolls of the dice."""
        return [self.roll() for _ in range(num_rolls)]

    def get_probabilities(self, num_rolls: int) -> dict[int, float]:
        rolls = self.simulate_rolls(num_rolls)
        counts: dict[int, int] = {}
        for roll in rolls:
            counts[roll] = counts.get(roll, 0) + 1
        return {side: count / num_rolls for side, count in counts.items()}

    def print_probabilities(self, num_rolls: int) -> None:
        probabilities = self.get_probabilities(num_rolls)
        for side in sorted(probabilities.keys()):
            print(f"Side {side}: {probabilities[side]:.2%}")

class Dice(BaseDice):
    """Dice with arbitrary side values."""

    def __init__(self, sides: list[int]) -> None:
        self.sides = sides
        self.max_side = max(sides) if sides else 0

    def roll(self) -> int:
        return random.choice(self.sides)

    def __str__(self) -> str:
        return f"Dice({self.sides})"


class SequentialDice(Dice):
    """Traditional dice with sequential sides (1 to N)."""

    def __init__(self, num_sides: int = 6) -> None:
        super().__init__(list(range(1, num_sides + 1)))
        self.num_sides = num_sides
        self.dice = Dice(list(range(1, num_sides + 1)))

    def roll(self) -> int:
        return self.dice.roll()

    def __str__(self) -> str:
        return f"SequentialDice({self.num_sides})"
