from fair_dices.dice import Dice


class MultiDice(Dice):
    def __init__(self, dices: list[Dice]) -> None:
        if not dices:
            raise ValueError("At least one dice must be provided")
        self.sides = 1
        for dice in dices:
            self.sides *= dice.sides
        self.dices = dices

    def roll(self) -> int:
        result = 0
        multiplier = 1
        for dice in self.dices:
            roll = dice.roll() - 1
            result += roll * multiplier
            multiplier *= dice.sides
        return result + 1

    def __str__(self) -> str:
        dices_str = ", ".join(f"d{dice.sides}" for dice in self.dices)
        return f"MultiDice({dices_str}) = d{self.sides}"

    def explain(self) -> str:
        dices_explain = ", ".join(dice.explain() for dice in self.dices)
        return f"MultiDice({dices_explain})"


class DuoDice(Dice):  # it's a multi dice with two dices. here for legacy reasons
    def __init__(self, dice_a: Dice, dice_b: Dice) -> None:
        self.sides = dice_a.sides * dice_b.sides
        self.dice_a = dice_a
        self.dice_b = dice_b

    def roll(self) -> int:
        roll_a = self.dice_a.roll() - 1
        b_sides = self.dice_b.sides
        roll_b = self.dice_b.roll()
        return roll_a * b_sides + roll_b

    def __str__(self) -> str:
        return f"DuoDice(d{self.dice_a.sides}, d{self.dice_b.sides}) = d{self.sides}"

    def explain(self) -> str:
        return f"DuoDice({self.dice_a.explain()}, {self.dice_b.explain()})"
