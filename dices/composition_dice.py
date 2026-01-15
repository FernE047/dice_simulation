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
