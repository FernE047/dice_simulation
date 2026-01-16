from math import sqrt
from dices.dice import BaseDice, DiceOfDices


class MeanDice(DiceOfDices):
    def __init__(self, dice_list: list[BaseDice]) -> None:
        super().__init__(dice_list)
        self.max_side = sum(die.max_side for die in dice_list) // len(dice_list)

    def apply_logic(self, rolls: list[int]) -> int:
        return sum(rolls) // len(rolls)

    def __str__(self) -> str:
        dice_str = ", ".join(str(die) for die in self.dices)
        return f"MeanDice([{dice_str}])"


class MedianDice(DiceOfDices):
    def __init__(self, dice_list: list[BaseDice]) -> None:
        super().__init__(dice_list)
        self.max_side = sorted(die.max_side for die in dice_list)[len(dice_list) // 2]

    def apply_logic(self, rolls: list[int]) -> int:
        rolls = sorted(rolls)
        n = len(rolls)
        mid = n // 2
        if n % 2 == 0:
            return (rolls[mid - 1] + rolls[mid]) // 2
        else:
            return rolls[mid]

    def __str__(self) -> str:
        dice_str = ", ".join(str(die) for die in self.dices)
        return f"MedianDice([{dice_str}])"


class ModeDice(DiceOfDices):
    def __init__(self, dice_list: list[BaseDice]) -> None:
        super().__init__(dice_list)
        self.max_side = max(die.max_side for die in dice_list)

    def apply_logic(self, rolls: list[int]) -> int:
        frequency: dict[int, int] = {}
        for roll in rolls:
            frequency[roll] = frequency.get(roll, 0) + 1
        mode = max(frequency, key=lambda x: frequency[x])
        return mode

    def __str__(self) -> str:
        dice_str = ", ".join(str(die) for die in self.dices)
        return f"ModeDice([{dice_str}])"


class VarianceDice(DiceOfDices):
    def __init__(self, dice_list: list[BaseDice]) -> None:
        super().__init__(dice_list)
        self.max_side = max(die.max_side for die in dice_list)

    def apply_logic(self, rolls: list[int]) -> int:
        mean = sum(rolls) / len(rolls)
        variance = sum((x - mean) ** 2 for x in rolls) / len(rolls)
        return int(variance)

    def __str__(self) -> str:
        dice_str = ", ".join(str(die) for die in self.dices)
        return f"VarianceDice([{dice_str}])"


class StdDevDice(DiceOfDices):
    def __init__(self, dice_list: list[BaseDice]) -> None:
        super().__init__(dice_list)
        self.max_side = max(die.max_side for die in dice_list)

    def apply_logic(self, rolls: list[int]) -> int:
        mean = sum(rolls) / len(rolls)
        variance = sum((x - mean) ** 2 for x in rolls) / len(rolls)
        stddev = sqrt(variance)
        return int(stddev)

    def __str__(self) -> str:
        dice_str = ", ".join(str(die) for die in self.dices)
        return f"StdDevDice([{dice_str}])"


class RangeDice(DiceOfDices):
    def __init__(self, dice_list: list[BaseDice]) -> None:
        super().__init__(dice_list)

    def apply_logic(self, rolls: list[int]) -> int:
        return max(rolls) - min(rolls)

    def __str__(self) -> str:
        dice_str = ", ".join(str(die) for die in self.dices)
        return f"RangeDice([{dice_str}])"


class WeightedMeanDice(DiceOfDices):
    def __init__(self, dice_list: list[BaseDice], dice_weights: list[BaseDice]) -> None:
        if len(dice_list) != len(dice_weights):
            raise ValueError("dice_list and dice_weights must have the same length")
        super().__init__(dice_list + dice_weights)
        self.dice_amount = len(dice_list)
        self.max_side = max(
            die.max_side * weight.max_side
            for die, weight in zip(dice_list, dice_weights)
        )

    def apply_logic(self, rolls: list[int]) -> int:
        dice_rolls = rolls[: self.dice_amount]
        weight_rolls = rolls[self.dice_amount :]
        weighted_rolls = [
            die_roll * weight_roll
            for die_roll, weight_roll in zip(dice_rolls, weight_rolls)
        ]
        total_weight = sum(weight_rolls)
        return sum(weighted_rolls) // total_weight if total_weight != 0 else 0

    def __str__(self) -> str:
        dice_str = ", ".join(str(die) for die in self.dices[: self.dice_amount])
        weights_str = ", ".join(
            str(weight) for weight in self.dices[self.dice_amount :]
        )
        return f"WeightedMeanDice([{dice_str}], [{weights_str}])"
