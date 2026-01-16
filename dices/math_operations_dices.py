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

class OffsetDice(Dice):
    def __init__(self, base_die: Dice, offset: int) -> None:
        self.base_die = base_die
        self.offset = offset
        self.sides = base_die.sides + offset

    def roll(self) -> int:
        return self.base_die.roll() + self.offset

    def __str__(self) -> str:
        return f"OffsetDice({self.base_die}, {self.offset})"
    
class FloorDice(Dice):
    def __init__(self, base_die: Dice, floor: int) -> None:
        self.base_die = base_die
        self.floor = floor
        self.sides = base_die.sides

    def roll(self) -> int:
        result = self.base_die.roll()
        return max(result, self.floor)

    def __str__(self) -> str:
        return f"FloorDice({self.base_die}, {self.floor})"
    
class CeilDice(Dice):
    def __init__(self, base_die: Dice, ceil: int) -> None:
        self.base_die = base_die
        self.ceil = ceil
        self.sides = base_die.sides

    def roll(self) -> int:
        result = self.base_die.roll()
        return min(result, self.ceil)

    def __str__(self) -> str:
        return f"CeilDice({self.base_die}, {self.ceil})"
    
class ClampDice(Dice):
    def __init__(self, base_die: Dice, floor: int, ceil: int) -> None:
        self.base_die = base_die
        self.floor = floor
        self.ceil = ceil
        self.sides = base_die.sides

    def roll(self) -> int:
        result = self.base_die.roll()
        return max(self.floor, min(result, self.ceil))

    def __str__(self) -> str:
        return f"ClampDice({self.base_die}, {self.floor}, {self.ceil})"
    
class FactorDice(Dice):
    def __init__(self, base_die: Dice, factor: int) -> None:
        self.base_die = base_die
        self.factor = factor
        self.sides = base_die.sides * factor

    def roll(self) -> int:
        return self.base_die.roll() * self.factor

    def __str__(self) -> str:
        return f"FactorDice({self.base_die}, {self.factor})"
    
class FactorialDice(Dice):
    def __init__(self, base_die: Dice) -> None:
        self.base_die = base_die
        self.sides = base_die.sides

    def roll(self) -> int:
        from math import factorial

        n = self.base_die.roll()
        return factorial(n)

    def __str__(self) -> str:
        return f"FactorialDice({self.base_die})"

class PowerDice(Dice):
    def __init__(self, base_die: Dice, power: int) -> None:
        self.base_die = base_die
        self.power = power
        self.sides = base_die.sides ** power

    def roll(self) -> int:
        return self.base_die.roll() ** self.power

    def __str__(self) -> str:
        return f"PowerDice({self.base_die}, {self.power})"
    
class SqrtDice(Dice):
    def __init__(self, base_die: Dice) -> None:
        self.base_die = base_die
        self.sides = base_die.sides

    def roll(self) -> int:
        from math import isqrt

        n = self.base_die.roll()
        return isqrt(n)

    def __str__(self) -> str:
        return f"SqrtDice({self.base_die})"
    
class LogDice(Dice):
    def __init__(self, base_die: Dice, base: float = 10) -> None:
        self.base_die = base_die
        self.base = base
        self.sides = base_die.sides

    def roll(self) -> int:
        from math import log, floor

        n = self.base_die.roll()
        return floor(log(n, self.base))

    def __str__(self) -> str:
        return f"LogDice({self.base_die}, {self.base})"
    
class ExpDice(Dice):
    def __init__(self, base_die: Dice, exponent: float = 2) -> None:
        self.base_die = base_die
        self.exponent = exponent
        self.sides = base_die.sides

    def roll(self) -> int:
        from math import exp, floor

        n = self.base_die.roll()
        return floor(exp(n * self.exponent))

    def __str__(self) -> str:
        return f"ExpDice({self.base_die}, {self.exponent})"
    
class AbsDice(Dice):
    def __init__(self, base_die: Dice) -> None:
        self.base_die = base_die
        self.sides = base_die.sides

    def roll(self) -> int:
        n = self.base_die.roll()
        return abs(n)

    def __str__(self) -> str:
        return f"AbsDice({self.base_die})"
    
class NegDice(Dice):
    def __init__(self, base_die: Dice) -> None:
        self.base_die = base_die
        self.sides = base_die.sides

    def roll(self) -> int:
        n = self.base_die.roll()
        return -n

    def __str__(self) -> str:
        return f"NegDice({self.base_die})"
    
class DivisionDice(Dice):
    def __init__(self, base_die: Dice, divisor: int) -> None:
        if divisor == 0:
            raise ValueError("Divisor cannot be zero.")
        self.base_die = base_die
        self.divisor = divisor
        self.sides = base_die.sides // divisor

    def roll(self) -> int:
        n = self.base_die.roll()
        return n // self.divisor

    def __str__(self) -> str:
        return f"DivisionDice({self.base_die}, {self.divisor})"