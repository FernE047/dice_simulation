from dices.dice import Dice
from dices.math_operations_dices import ModDice


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
        dices_explain = ", ".join(str(dice) for dice in self.dices)
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
        return f"DuoDice({self.dice_a}, {self.dice_b})"


class ComposedDice(Dice):
    def __init__(self, decision_dice: Dice, dices: list[Dice]) -> None:
        if not dices:
            raise ValueError("At least one dice must be provided")
        if len(dices) != decision_dice.sides:
            raise ValueError(
                "Number of dices must match the sides of the decision dice"
            )
        self.sides = sum(dice.sides for dice in dices)
        self.decision_dice = decision_dice
        self.dices = dices
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
        selected_dice = self.dices[decision - 1]
        dice_result = selected_dice.roll()
        result = (
            dice_result
            + sum(dice.sides for dice in self.dices[: decision - 1])
            - self._rounds
        ) % self.sides
        self.rounds += 1
        if result == 0:
            return self.sides
        return result

    def __str__(self) -> str:
        dices_explain = ", ".join(str(dice) for dice in self.dices)
        return f"ComposedDice({self.decision_dice}, [{dices_explain}])"


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
        return f"OneExtraSideDice({self.decision_dice}, {self.dice})"
