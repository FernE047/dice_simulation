from dices.dice import BaseDice, BiDice, DiceOfDices, SequentialDice
from dices.math_operations_dices import ModDice


class MultiDice(DiceOfDices):
    def __init__(self, dices: list[BaseDice]) -> None:
        if not dices:
            raise ValueError("At least one dice must be provided")
        self.max_side = 1
        for dice in dices:
            self.max_side *= dice.max_side
        super().__init__(dices)

    def apply_logic(self, rolls: list[int]) -> int:
        result = 0
        multiplier = 1
        for index, roll in enumerate(rolls):
            result += (roll - 1) * multiplier
            multiplier *= int(self.dices[index].max_side)
        return result + 1

    def __str__(self) -> str:
        dices_explain = ", ".join(str(dice) for dice in self.dices)
        return f"MultiDice({dices_explain})"


class DuoDice(BiDice):  # it's a multi dice with two dices. here for legacy reasons
    def __init__(self, dice_a: BaseDice, dice_b: BaseDice) -> None:
        self.max_side = dice_a.max_side * dice_b.max_side
        super().__init__(dice_a, dice_b)

    def apply_logic(self, roll_a: int, roll_b: int) -> int:
        b_sides = int(self.dice_b.max_side)
        return (roll_a - 1) * b_sides + roll_b

    def __str__(self) -> str:
        return f"DuoDice({self.dice_a}, {self.dice_b})"


class ComposedDice(DiceOfDices):
    def __init__(self, decision_dice: BaseDice, dices: list[BaseDice]) -> None:
        if not dices:
            raise ValueError("At least one dice must be provided")
        if len(dices) != decision_dice.max_side:
            raise ValueError(
                "Number of dices must match the sides of the decision dice"
            )
        self.max_side = sum(dice.max_side for dice in dices)
        super().__init__([decision_dice] + dices)
        self._rounds = 0

    @property
    def rounds(self) -> int:
        return self._rounds

    @rounds.setter
    def rounds(self, value: int) -> None:
        self._rounds = value
        if self._rounds >= self.max_side:
            self._rounds = 0

    def apply_logic(self, rolls: list[int]) -> int:
        decision = rolls[0]
        dice_result = rolls[decision]
        total = sum(int(dice.max_side) for dice in self.dices[1 : decision + 1])
        result = (dice_result + total - self._rounds) % int(self.max_side)
        self.rounds += 1
        if result == 0:
            return int(self.max_side)
        return result

    def __str__(self) -> str:
        dices_explain = ", ".join(str(dice) for dice in self.dices[1:])
        return f"ComposedDice({self.dices[0]}, [{dices_explain}])"


class OneExtraSideDice(BiDice):
    def __init__(self, dice: BaseDice) -> None:
        self.max_side = dice.max_side + 1
        super().__init__(ModDice(SequentialDice(4), 2), dice)
        self._rounds = 0

    @property
    def rounds(self) -> int:
        return self._rounds

    @rounds.setter
    def rounds(self, value: int) -> None:
        self._rounds = value
        if self._rounds >= int(self.max_side):
            self._rounds = 0

    def apply_logic(self, roll_a: int, roll_b: int) -> int:
        decision = roll_a
        if decision == 1:
            result = (1 - self._rounds) % int(self.max_side)
        else:
            dice_result = roll_b
            result = (dice_result + 1 - self._rounds) % int(self.max_side)
        self.rounds += 1
        if result == 0:
            return int(self.max_side)
        return result

    def __str__(self) -> str:
        return f"OneExtraSideDice({self.dice_a}, {self.dice_b})"
