from dices.dice import BaseDice


class MeanDice(BaseDice):
    def __init__(self, dice_list: list[BaseDice]) -> None:
        self.dice_list = dice_list
        self.max_side = sum(die.max_side for die in dice_list) // len(dice_list)

    def roll(self) -> int:
        rolls = [die.roll() for die in self.dice_list]
        return sum(rolls) // len(rolls)

    def __str__(self) -> str:
        dice_str = ", ".join(str(die) for die in self.dice_list)
        return f"MeanDice([{dice_str}])"


class MedianDice(BaseDice):
    def __init__(self, dice_list: list[BaseDice]) -> None:
        self.dice_list = dice_list
        self.max_side = sorted(die.max_side for die in dice_list)[len(dice_list) // 2]

    def roll(self) -> int:
        rolls = sorted(die.roll() for die in self.dice_list)
        n = len(rolls)
        mid = n // 2
        if n % 2 == 0:
            return (rolls[mid - 1] + rolls[mid]) // 2
        else:
            return rolls[mid]

    def __str__(self) -> str:
        dice_str = ", ".join(str(die) for die in self.dice_list)
        return f"MedianDice([{dice_str}])"


class ModeDice(BaseDice):
    def __init__(self, dice_list: list[BaseDice]) -> None:
        self.dice_list = dice_list
        self.max_side = max(die.max_side for die in dice_list)

    def roll(self) -> int:
        rolls = [die.roll() for die in self.dice_list]
        frequency: dict[int, int] = {}
        for roll in rolls:
            frequency[roll] = frequency.get(roll, 0) + 1
        mode = max(frequency, key=lambda x: frequency[x])
        return mode

    def __str__(self) -> str:
        dice_str = ", ".join(str(die) for die in self.dice_list)
        return f"ModeDice([{dice_str}])"


class VarianceDice(BaseDice):
    def __init__(self, dice_list: list[BaseDice]) -> None:
        self.dice_list = dice_list
        self.max_side = max(die.max_side for die in dice_list)

    def roll(self) -> int:
        rolls = [die.roll() for die in self.dice_list]
        mean = sum(rolls) / len(rolls)
        variance = sum((x - mean) ** 2 for x in rolls) / len(rolls)
        return int(variance)

    def __str__(self) -> str:
        dice_str = ", ".join(str(die) for die in self.dice_list)
        return f"VarianceDice([{dice_str}])"


class StdDevDice(BaseDice):
    def __init__(self, dice_list: list[BaseDice]) -> None:
        self.dice_list = dice_list
        self.max_side = max(die.max_side for die in dice_list)
        self.variance_dice = VarianceDice(dice_list)

    def roll(self) -> int:
        from math import sqrt

        variance = self.variance_dice.roll()
        stddev = sqrt(variance)
        return int(stddev)

    def __str__(self) -> str:
        dice_str = ", ".join(str(die) for die in self.dice_list)
        return f"StdDevDice([{dice_str}])"


class RangeDice(BaseDice):
    def __init__(self, dice_list: list[BaseDice]) -> None:
        self.dice_list = dice_list
        self.max_side = max(die.max_side for die in dice_list)

    def roll(self) -> int:
        rolls = [die.roll() for die in self.dice_list]
        return max(rolls) - min(rolls)

    def __str__(self) -> str:
        dice_str = ", ".join(str(die) for die in self.dice_list)
        return f"RangeDice([{dice_str}])"


class WeightedMeanDice(BaseDice):
    def __init__(self, dice_list: list[BaseDice], dice_weights: list[BaseDice]) -> None:
        if len(dice_list) != len(dice_weights):
            raise ValueError("dice_list and dice_weights must have the same length")
        self.dice_list = dice_list
        self.dice_weights = dice_weights
        self.max_side = max(
            die.max_side * weight.max_side
            for die, weight in zip(dice_list, dice_weights)
        )

    def roll(self) -> int:
        weighted_rolls = [
            die.roll() * weight.roll()
            for die, weight in zip(self.dice_list, self.dice_weights)
        ]
        total_weight = sum(weight.roll() for weight in self.dice_weights)
        return sum(weighted_rolls) // total_weight if total_weight != 0 else 0

    def __str__(self) -> str:
        dice_str = ", ".join(str(die) for die in self.dice_list)
        weights_str = ", ".join(str(weight) for weight in self.dice_weights)
        return f"WeightedMeanDice([{dice_str}], [{weights_str}])"
