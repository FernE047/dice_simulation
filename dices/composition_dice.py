from dices.dice import Dice


class CompositeDice(Dice):
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
        return f"CompositeDice(d{self.dice_a.sides}, d{self.dice_b.sides}) = d{self.sides}"

    def explain(self) -> str:
        return f"CompositeDice({self.dice_a.explain()}, {self.dice_b.explain()})"