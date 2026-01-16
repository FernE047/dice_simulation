from typing import cast
from dices.dice import BaseDice

"""This module contains dice that have their behavior modified by mathematical operations."""


class ModDice(BaseDice):
    def __init__(self, base_die: BaseDice, modulo: int = 0) -> None:
        self.max_side = modulo
        self.base_die = base_die
        self.modulo = modulo

    def roll(self) -> int:
        return self.base_die.roll() % self.modulo + 1

    def __str__(self) -> str:
        return f"ModDice({self.base_die}, {self.modulo})"


class PrimeDice(BaseDice):
    def __init__(self, base_die: BaseDice) -> None:
        self.base_die = base_die

    def roll(self) -> int:
        from sympy import prime  # type: ignore

        n = self.base_die.roll()
        return cast(int, prime(n))

    def __str__(self) -> str:
        return f"PrimeDice({self.base_die})"


class OffsetDice(BaseDice):
    def __init__(self, base_die: BaseDice, offset: int) -> None:
        self.base_die = base_die
        self.offset = offset
        self.max_side = base_die.max_side + offset

    def roll(self) -> int:
        return self.base_die.roll() + self.offset

    def __str__(self) -> str:
        return f"OffsetDice({self.base_die}, {self.offset})"


class FloorDice(BaseDice):
    def __init__(self, base_die: BaseDice, floor: int) -> None:
        self.base_die = base_die
        self.floor = floor
        self.max_side = base_die.max_side

    def roll(self) -> int:
        result = self.base_die.roll()
        return max(result, self.floor)

    def __str__(self) -> str:
        return f"FloorDice({self.base_die}, {self.floor})"


class CeilDice(BaseDice):
    def __init__(self, base_die: BaseDice, ceil: int) -> None:
        self.base_die = base_die
        self.ceil = ceil
        self.max_side = base_die.max_side

    def roll(self) -> int:
        result = self.base_die.roll()
        return min(result, self.ceil)

    def __str__(self) -> str:
        return f"CeilDice({self.base_die}, {self.ceil})"


class ClampDice(BaseDice):
    def __init__(self, base_die: BaseDice, floor: int, ceil: int) -> None:
        self.base_die = base_die
        self.floor = floor
        self.ceil = ceil
        self.max_side = base_die.max_side

    def roll(self) -> int:
        result = self.base_die.roll()
        return max(self.floor, min(result, self.ceil))

    def __str__(self) -> str:
        return f"ClampDice({self.base_die}, {self.floor}, {self.ceil})"


class FactorDice(BaseDice):
    def __init__(self, base_die: BaseDice, factor: int) -> None:
        self.base_die = base_die
        self.factor = factor
        self.max_side = base_die.max_side * factor

    def roll(self) -> int:
        return self.base_die.roll() * self.factor

    def __str__(self) -> str:
        return f"FactorDice({self.base_die}, {self.factor})"


class FactorialDice(BaseDice):
    def __init__(self, base_die: BaseDice) -> None:
        self.base_die = base_die
        self.max_side = base_die.max_side

    def roll(self) -> int:
        from math import factorial

        n = self.base_die.roll()
        return factorial(n)

    def __str__(self) -> str:
        return f"FactorialDice({self.base_die})"


class PowerDice(BaseDice):
    def __init__(self, base_die: BaseDice, power: int) -> None:
        self.base_die = base_die
        self.power = power
        self.max_side = base_die.max_side**power

    def roll(self) -> int:
        return self.base_die.roll() ** self.power

    def __str__(self) -> str:
        return f"PowerDice({self.base_die}, {self.power})"


class SqrtDice(BaseDice):
    def __init__(self, base_die: BaseDice) -> None:
        self.base_die = base_die
        self.max_side = base_die.max_side

    def roll(self) -> int:
        from math import isqrt

        n = self.base_die.roll()
        return isqrt(n)

    def __str__(self) -> str:
        return f"SqrtDice({self.base_die})"


class LogDice(BaseDice):
    def __init__(self, base_die: BaseDice, base: float = 10) -> None:
        self.base_die = base_die
        self.base = base
        self.max_side = base_die.max_side

    def roll(self) -> int:
        from math import log, floor

        n = self.base_die.roll()
        return floor(log(n, self.base))

    def __str__(self) -> str:
        return f"LogDice({self.base_die}, {self.base})"


class ExpDice(BaseDice):
    def __init__(self, base_die: BaseDice, exponent: float = 2) -> None:
        self.base_die = base_die
        self.exponent = exponent
        self.max_side = base_die.max_side

    def roll(self) -> int:
        from math import exp, floor

        n = self.base_die.roll()
        return floor(exp(n * self.exponent))

    def __str__(self) -> str:
        return f"ExpDice({self.base_die}, {self.exponent})"


class AbsDice(BaseDice):
    def __init__(self, base_die: BaseDice) -> None:
        self.base_die = base_die
        self.max_side = base_die.max_side

    def roll(self) -> int:
        n = self.base_die.roll()
        return abs(n)

    def __str__(self) -> str:
        return f"AbsDice({self.base_die})"


class NegDice(BaseDice):
    def __init__(self, base_die: BaseDice) -> None:
        self.base_die = base_die
        self.max_side = base_die.max_side

    def roll(self) -> int:
        n = self.base_die.roll()
        return -n

    def __str__(self) -> str:
        return f"NegDice({self.base_die})"


class DivisionDice(BaseDice):
    def __init__(self, base_die: BaseDice, divisor: int) -> None:
        if divisor == 0:
            raise ValueError("Divisor cannot be zero.")
        self.base_die = base_die
        self.divisor = divisor
        self.max_side = base_die.max_side // divisor

    def roll(self) -> int:
        n = self.base_die.roll()
        return n // self.divisor

    def __str__(self) -> str:
        return f"DivisionDice({self.base_die}, {self.divisor})"
