from fair_dices.dice import Dice
from fair_dices.mod_dice import ModDice

# this die is unfair for a single round, but evens out over multiple rounds


class OneExtraSideDice(Dice):
    def __init__(self, dice: Dice) -> None:
        self.sides = dice.sides + 1
        self.decision_dice = ModDice(Dice(4), 2)
        self.dice = dice
        self._rounds = 0

    @property
    def rounds(self) -> int:
        return self._rounds

    @rounds.setter
    def rounds(self, value: int) -> None:
        self._rounds = value
        if self._rounds >= self.sides:
            self._rounds = 0

    def roll(self) -> int:
        decision = self.decision_dice.roll()
        if decision == 1:
            result = (1 - self._rounds) % self.sides
        else:
            dice_result = self.dice.roll()
            result = (dice_result + 1 - self._rounds) % self.sides
        self.rounds += 1
        if result == 0:
            return self.sides
        return result

    def __str__(self) -> str:
        return f"OneExtraSideDice(d2, d{self.dice.sides}) = d{self.sides}"

    def explain(self) -> str:
        return f"OneExtraSideDice({self.decision_dice.explain()}, {self.dice.explain()})"