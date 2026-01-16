from fair_dices.dice import Dice


class MeanDice(Dice):
    def __init__(self, dice_list: list[Dice]) -> None:
        self.dice_list = dice_list
        self.sides = sum(die.sides for die in dice_list) // len(dice_list)

    def roll(self) -> int:
        rolls = [die.roll() for die in self.dice_list]
        return sum(rolls) // len(rolls)

    def __str__(self) -> str:
        dice_str = ", ".join(str(die) for die in self.dice_list)
        return f"MeanDice([{dice_str}])"

    def explain(self) -> str:
        dice_explain = ", ".join(die.explain() for die in self.dice_list)
        return f"MeanDice([{dice_explain}])"


class MedianDice(Dice):
    def __init__(self, dice_list: list[Dice]) -> None:
        self.dice_list = dice_list
        self.sides = sorted(die.sides for die in dice_list)[len(dice_list) // 2]

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

    def explain(self) -> str:
        dice_explain = ", ".join(die.explain() for die in self.dice_list)
        return f"MedianDice([{dice_explain}])"


class ModeDice(Dice):
    def __init__(self, dice_list: list[Dice]) -> None:
        self.dice_list = dice_list
        self.sides = max(die.sides for die in dice_list)

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

    def explain(self) -> str:
        dice_explain = ", ".join(die.explain() for die in self.dice_list)
        return f"ModeDice([{dice_explain}])"

class VarianceDice(Dice):
    def __init__(self, dice_list: list[Dice]) -> None:
        self.dice_list = dice_list
        self.sides = max(die.sides for die in dice_list)

    def roll(self) -> int:
        rolls = [die.roll() for die in self.dice_list]
        mean = sum(rolls) / len(rolls)
        variance = sum((x - mean) ** 2 for x in rolls) / len(rolls)
        return int(variance)

    def __str__(self) -> str:
        dice_str = ", ".join(str(die) for die in self.dice_list)
        return f"VarianceDice([{dice_str}])"

    def explain(self) -> str:
        dice_explain = ", ".join(die.explain() for die in self.dice_list)
        return f"VarianceDice([{dice_explain}])"

class StdDevDice(Dice):
    def __init__(self, dice_list: list[Dice]) -> None:
        self.dice_list = dice_list
        self.sides = max(die.sides for die in dice_list)
        self.variance_dice = VarianceDice(dice_list)

    def roll(self) -> int:
        from math import sqrt
        variance = self.variance_dice.roll()
        stddev = sqrt(variance)
        return int(stddev)

    def __str__(self) -> str:
        dice_str = ", ".join(str(die) for die in self.dice_list)
        return f"StdDevDice([{dice_str}])"

    def explain(self) -> str:
        dice_explain = ", ".join(die.explain() for die in self.dice_list)
        return f"StdDevDice([{dice_explain}])"

class RangeDice(Dice):
    def __init__(self, dice_list: list[Dice]) -> None:
        self.dice_list = dice_list
        self.sides = max(die.sides for die in dice_list)

    def roll(self) -> int:
        rolls = [die.roll() for die in self.dice_list]
        return max(rolls) - min(rolls)

    def __str__(self) -> str:
        dice_str = ", ".join(str(die) for die in self.dice_list)
        return f"RangeDice([{dice_str}])"

    def explain(self) -> str:
        dice_explain = ", ".join(die.explain() for die in self.dice_list)
        return f"RangeDice([{dice_explain}])"

class WeightedMeanDice(Dice):
    def __init__(self, dice_list: list[Dice], dice_weights: list[Dice]) -> None:
        if len(dice_list) != len(dice_weights):
            raise ValueError("dice_list and dice_weights must have the same length")
        self.dice_list = dice_list
        self.dice_weights = dice_weights
        self.sides = max(die.sides * weight.sides for die, weight in zip(dice_list, dice_weights))

    def roll(self) -> int:
        weighted_rolls = [die.roll() * weight.roll() for die, weight in zip(self.dice_list, self.dice_weights)]
        total_weight = sum(weight.roll() for weight in self.dice_weights)
        return sum(weighted_rolls) // total_weight if total_weight != 0 else 0
    
    def __str__(self) -> str:
        dice_str = ", ".join(str(die) for die in self.dice_list)
        weights_str = ", ".join(str(weight) for weight in self.dice_weights)
        return f"WeightedMeanDice([{dice_str}], [{weights_str}])"
    
    def explain(self) -> str:
        dice_explain = ", ".join(die.explain() for die in self.dice_list)
        weights_explain = ", ".join(weight.explain() for weight in self.dice_weights)
        return f"WeightedMeanDice([{dice_explain}], [{weights_explain}])"