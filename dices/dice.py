from abc import ABC, abstractmethod
import random
from typing import Union, cast

OutcomesData = list[
    tuple[list[int], int]
]  # é uma lista de tuplas, cada tupla tem uma lista de inteiros (os dices rolls que levaram até o resultado) e um inteiro (o resultado final)
OutcomesMatriz = list[Union[int, "OutcomesMatriz"]]


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

    def simulate_probabilities(self, num_rolls: int) -> dict[int, float]:
        rolls = self.simulate_rolls(num_rolls)
        counts: dict[int, int] = {}
        for roll in rolls:
            counts[roll] = counts.get(roll, 0) + 1
        return {side: count / num_rolls for side, count in counts.items()}

    def print_simulated_probs(self, num_rolls: int) -> None:
        probabilities = self.simulate_probabilities(num_rolls)
        for side in sorted(probabilities.keys()):
            print(f"Side {side}: {probabilities[side]:.2%}")

    @abstractmethod
    def get_outcomes(self) -> OutcomesData:
        pass

    def print_outcomes(self) -> None:
        outcomes = self.get_outcomes()
        for rolls, result in outcomes:
            rolls_str = ", ".join(str(roll) for roll in rolls)
            print(f"Rolls: [{rolls_str}] => Result: {result}")

    def outcomes_matriz(self) -> OutcomesMatriz:
        outcomes = self.get_outcomes()
        matriz: OutcomesMatriz = []
        unique_values: list[list[int]] = []
        for rolls, _ in outcomes:
            if not unique_values:
                for roll in rolls:
                    unique_values.append([roll])
            else:
                for i, roll in enumerate(rolls):
                    if roll not in unique_values[i]:
                        unique_values[i].append(roll)

        def build_matriz(level: int, current_rolls: list[int]) -> OutcomesMatriz | int:
            if level == len(unique_values):
                for rolls, result in outcomes:
                    if rolls == current_rolls:
                        return result
                return 0  # should not happen
            matriz_level: OutcomesMatriz = []
            for value in unique_values[level]:
                next_rolls = current_rolls + [value]
                matriz_level.append(build_matriz(level + 1, next_rolls))
            return matriz_level

        matriz = cast(OutcomesMatriz, build_matriz(0, []))
        return matriz

    def get_probabilities(self) -> dict[int, float]:
        outcomes = self.get_outcomes()
        counts: dict[int, int] = {}
        for _, result in outcomes:
            counts[result] = counts.get(result, 0) + 1
        total_outcomes = len(outcomes)
        return {side: count / total_outcomes for side, count in counts.items()}

    def print_probabilities(self) -> None:
        probabilities = self.get_probabilities()
        for side in sorted(probabilities.keys()):
            print(f"Side {side}: {probabilities[side]:.2%}")


class Dice(BaseDice):
    """Dice with arbitrary side values."""

    def __init__(self, sides: list[int]) -> None:
        self.sides = sides
        self.max_side = max(sides) if sides else 0

    def roll(self) -> int:
        return random.choice(self.sides)

    def get_outcomes(self) -> OutcomesData:
        outcomes: OutcomesData = []
        for side in self.sides:
            outcomes.append(([side], side))
        return outcomes

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

    def get_outcomes(self) -> OutcomesData:
        outcomes: OutcomesData = []
        for side in range(1, self.num_sides + 1):
            outcomes.append(([side], side))
        return outcomes

    def __str__(self) -> str:
        return f"SequentialDice({self.num_sides})"


class DiceOfDices(BaseDice):
    def __init__(self, dices: list[BaseDice]) -> None:
        self.dices = dices

    @abstractmethod
    def apply_logic(self, rolls: list[int]) -> int:
        pass

    def roll(self) -> int:
        rolls = [dice.roll() for dice in self.dices]
        return self.apply_logic(rolls)

    def __str__(self) -> str:
        dices_str = ", ".join(str(dice) for dice in self.dices)
        return f"DiceOfDices([{dices_str}])"

    def get_outcomes(self) -> list[tuple[list[int], int]]:
        outcomes_calculator: list[tuple[list[int], list[int]]] = []
        for dice in self.dices:
            new_outcomes_calculator: list[tuple[list[int], list[int]]] = []
            dice_outcomes = dice.get_outcomes()  # list of (rolls, result)
            if not outcomes_calculator:
                for dice_rolls, dice_result in dice_outcomes:
                    new_outcomes_calculator.append((dice_rolls, [dice_result]))
            else:
                for existing_rolls, existing_results in outcomes_calculator:
                    for dice_rolls, dice_result in dice_outcomes:
                        combined_rolls = existing_rolls + dice_rolls
                        combined_results = existing_results + [dice_result]
                        new_outcomes_calculator.append(
                            (combined_rolls, combined_results)
                        )
            outcomes_calculator = new_outcomes_calculator
        final_outcomes: OutcomesData = []
        for rolls, results in outcomes_calculator:
            final_result = self.apply_logic(results)
            final_outcomes.append((rolls, final_result))
        return final_outcomes


class BiDice(BaseDice):
    def __init__(self, dice_a: BaseDice, dice_b: BaseDice) -> None:
        self.dice_a = dice_a
        self.dice_b = dice_b

    @abstractmethod
    def apply_logic(self, roll_a: int, roll_b: int) -> int:
        pass

    def roll(self) -> int:
        roll_a = self.dice_a.roll()
        roll_b = self.dice_b.roll()
        return self.apply_logic(roll_a, roll_b)

    def get_outcomes(self) -> OutcomesData:
        outcomes: OutcomesData = []
        dice_a_outcomes = self.dice_a.get_outcomes()
        dice_b_outcomes = self.dice_b.get_outcomes()
        for rolls_a, result_a in dice_a_outcomes:
            for rolls_b, result_b in dice_b_outcomes:
                total_result = self.apply_logic(result_a, result_b)
                outcomes.append((rolls_a + rolls_b, total_result))
        return outcomes


class AlterDice(BaseDice):
    def __init__(self, die: BaseDice, opperand: list[int]) -> None:
        self.die = die
        self.opperand = opperand

    @abstractmethod
    def apply_logic(self, roll: int) -> int:
        pass

    def roll(self) -> int:
        roll = self.die.roll()
        return self.apply_logic(roll)

    def get_outcomes(self) -> OutcomesData:
        outcomes: OutcomesData = []
        dice_outcomes = self.die.get_outcomes()
        for rolls, result in dice_outcomes:
            total_result = self.apply_logic(result)
            outcomes.append((rolls, total_result))
        return outcomes


class FunctionDice(BaseDice):
    # it only have one die as input, and applies a function to its roll using apply_logic
    def __init__(self, die: BaseDice) -> None:
        self.die = die

    @abstractmethod
    def apply_logic(self, roll: int) -> int:
        pass

    def roll(self) -> int:
        roll = self.die.roll()
        return self.apply_logic(roll)

    def get_outcomes(self) -> OutcomesData:
        outcomes: OutcomesData = []
        dice_outcomes = self.die.get_outcomes()
        for rolls, result in dice_outcomes:
            total_result = self.apply_logic(result)
            outcomes.append((rolls, total_result))
        return outcomes
