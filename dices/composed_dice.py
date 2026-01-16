from dices.dice import BaseDice, SequentialDice
from dices.math_operations_dices import ModDice


class MultiDice(BaseDice):
    def __init__(self, dices: list[BaseDice]) -> None:
        if not dices:
            raise ValueError("At least one dice must be provided")
        self.max_side = 1
        for dice in dices:
            self.max_side *= dice.max_side
        self.dices = dices

    def roll(self) -> int:
        result = 0
        multiplier = 1
        for dice in self.dices:
            roll = dice.roll() - 1
            result += roll * multiplier
            multiplier *= int(dice.max_side)
        return result + 1

    def __str__(self) -> str:
        dices_explain = ", ".join(str(dice) for dice in self.dices)
        return f"MultiDice({dices_explain})"


class DuoDice(BaseDice):  # it's a multi dice with two dices. here for legacy reasons
    def __init__(self, dice_a: BaseDice, dice_b: BaseDice) -> None:
        self.max_side = dice_a.max_side * dice_b.max_side
        self.dice_a = dice_a
        self.dice_b = dice_b

    def roll(self) -> int:
        roll_a = self.dice_a.roll() - 1
        b_sides = int(self.dice_b.max_side)
        roll_b = self.dice_b.roll()
        return roll_a * b_sides + roll_b

    def __str__(self) -> str:
        return f"DuoDice({self.dice_a}, {self.dice_b})"


class ComposedDice(BaseDice):
    def __init__(self, decision_dice: BaseDice, dices: list[BaseDice]) -> None:
        if not dices:
            raise ValueError("At least one dice must be provided")
        if len(dices) != decision_dice.max_side:
            raise ValueError(
                "Number of dices must match the sides of the decision dice"
            )
        self.max_side = sum(dice.max_side for dice in dices)
        self.decision_dice = decision_dice
        self.dices = dices
        self._rounds = 0

    @property
    def rounds(self) -> int:
        return self._rounds

    @rounds.setter
    def rounds(self, value: int) -> None:
        self._rounds = value
        if self._rounds >= self.max_side:
            self._rounds = 0

    def roll(self) -> int:
        decision = self.decision_dice.roll()
        selected_dice = self.dices[decision - 1]
        dice_result = selected_dice.roll()
        result = (
            dice_result
            + sum(int(dice.max_side) for dice in self.dices[: decision - 1])
            - self._rounds
        ) % int(self.max_side)
        self.rounds += 1
        if result == 0:
            return int(self.max_side)
        return result

    def __str__(self) -> str:
        dices_explain = ", ".join(str(dice) for dice in self.dices)
        return f"ComposedDice({self.decision_dice}, [{dices_explain}])"


class OneExtraSideDice(BaseDice):
    def __init__(self, dice: BaseDice) -> None:
        self.max_side = dice.max_side + 1
        self.decision_dice = ModDice(SequentialDice(4), 2)
        self.dice = dice
        self._rounds = 0

    @property
    def rounds(self) -> int:
        return self._rounds

    @rounds.setter
    def rounds(self, value: int) -> None:
        self._rounds = value
        if self._rounds >= int(self.max_side):
            self._rounds = 0

    def roll(self) -> int:
        decision = self.decision_dice.roll()
        if decision == 1:
            result = (1 - self._rounds) % int(self.max_side)
        else:
            dice_result = self.dice.roll()
            result = (dice_result + 1 - self._rounds) % int(self.max_side)
        self.rounds += 1
        if result == 0:
            return int(self.max_side)
        return result

    def __str__(self) -> str:
        return f"OneExtraSideDice({self.decision_dice}, {self.dice})"
