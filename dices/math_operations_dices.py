from typing import cast
from dices.dice import Dice

"""This module contains dice that have their behavior modified by mathematical operations."""


class ModDice(Dice):
    def __init__(self, base_die: Dice, modulo: int = 0) -> None:
        self.sides = modulo
        self.base_die = base_die
        self.modulo = modulo

    def roll(self) -> int:
        return self.base_die.roll() % self.modulo + 1

    def __str__(self) -> str:
        return f"ModDice({self.base_die}, {self.modulo})"


class PrimeDice(Dice):
    def __init__(self, base_die: Dice) -> None:
        self.base_die = base_die

    def roll(self) -> int:
        from sympy import prime  # type: ignore

        n = self.base_die.roll()
        return cast(int, prime(n))

    def __str__(self) -> str:
        return f"PrimeDice({self.base_die})"
