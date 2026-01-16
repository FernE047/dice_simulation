from math import exp, factorial, floor, isqrt, log
from sympy import prime  # type: ignore
from typing import cast
from dices.dice import AlterDice, BaseDice, FunctionDice

"""This module contains dice that have their behavior modified by mathematical operations."""


class ModDice(AlterDice):
    def __init__(self, base_die: BaseDice, modulo: int = 0) -> None:
        super().__init__(base_die, [modulo])
        self.max_side = modulo - 1

    def apply_logic(self, roll: int) -> int:
        return roll % self.opperand[0] + 1

    def __str__(self) -> str:
        return f"ModDice({self.die}, {self.opperand})"


class PrimeDice(FunctionDice):
    def __init__(self, base_die: BaseDice) -> None:
        super().__init__(base_die)
        self.max_side = cast(int, prime(base_die.max_side))

    def apply_logic(self, roll: int) -> int:
        return cast(int, prime(roll))

    def __str__(self) -> str:
        return f"PrimeDice({self.die})"


class OffsetDice(AlterDice):
    def __init__(self, base_die: BaseDice, offset: int) -> None:
        super().__init__(base_die, [offset])
        self.max_side = base_die.max_side + offset

    def apply_logic(self, roll: int) -> int:
        return roll + self.opperand[0]

    def __str__(self) -> str:
        return f"OffsetDice({self.die}, {self.opperand[0]})"


class FloorDice(AlterDice):
    def __init__(self, base_die: BaseDice, floor: int) -> None:
        super().__init__(base_die, [floor])
        self.max_side = base_die.max_side

    def apply_logic(self, roll: int) -> int:
        return max(roll, self.opperand[0])

    def __str__(self) -> str:
        return f"FloorDice({self.die}, {self.opperand[0]})"


class CeilDice(AlterDice):
    def __init__(self, base_die: BaseDice, ceil: int) -> None:
        super().__init__(base_die, [ceil])
        self.max_side = base_die.max_side

    def apply_logic(self, roll: int) -> int:
        return min(roll, self.opperand[0])

    def __str__(self) -> str:
        return f"CeilDice({self.die}, {self.opperand[0]})"


class ClampDice(AlterDice):
    def __init__(self, base_die: BaseDice, floor: int, ceil: int) -> None:
        super().__init__(base_die, [floor, ceil])
        self.max_side = base_die.max_side

    def apply_logic(self, roll: int) -> int:
        return max(self.opperand[0], min(roll, self.opperand[1]))

    def __str__(self) -> str:
        return f"ClampDice({self.die}, {self.opperand[0]}, {self.opperand[1]})"


class FactorDice(AlterDice):
    def __init__(self, base_die: BaseDice, factor: int) -> None:
        super().__init__(base_die, [factor])
        self.max_side = base_die.max_side * factor

    def apply_logic(self, roll: int) -> int:
        return roll * self.opperand[0]

    def __str__(self) -> str:
        return f"FactorDice({self.die}, {self.opperand[0]})"


class FactorialDice(FunctionDice):
    def __init__(self, base_die: BaseDice) -> None:
        super().__init__(base_die)
        self.max_side = factorial(int(base_die.max_side))

    def apply_logic(self, roll: int) -> int:
        return factorial(roll)

    def __str__(self) -> str:
        return f"FactorialDice({self.die})"


class PowerDice(AlterDice):
    def __init__(self, base_die: BaseDice, power: int) -> None:
        super().__init__(base_die, [power])
        self.max_side = base_die.max_side**power

    def apply_logic(self, roll: int) -> int:
        return roll ** self.opperand[0]

    def __str__(self) -> str:
        return f"PowerDice({self.die}, {self.opperand[0]})"


class SqrtDice(FunctionDice):
    def __init__(self, base_die: BaseDice) -> None:
        super().__init__(base_die)
        self.max_side = base_die.max_side

    def apply_logic(self, roll: int) -> int:
        return isqrt(roll)

    def __str__(self) -> str:
        return f"SqrtDice({self.die})"


class LogDice(AlterDice):
    def __init__(self, base_die: BaseDice, base: int = 10) -> None:
        super().__init__(base_die, [base])
        self.max_side = base_die.max_side

    def apply_logic(self, roll: int) -> int:
        return floor(log(roll, self.opperand[0]))

    def __str__(self) -> str:
        return f"LogDice({self.die}, {self.opperand[0]})"


class ExpDice(AlterDice):
    def __init__(self, base_die: BaseDice, exponent: int = 2) -> None:
        super().__init__(base_die, [exponent])
        self.max_side = base_die.max_side

    def apply_logic(self, roll: int) -> int:
        return floor(exp(roll * self.opperand[0]))

    def __str__(self) -> str:
        return f"ExpDice({self.die}, {self.opperand[0]})"


class AbsDice(FunctionDice):
    def __init__(self, base_die: BaseDice) -> None:
        super().__init__(base_die)
        self.max_side = base_die.max_side

    def apply_logic(self, roll: int) -> int:
        return abs(roll)

    def __str__(self) -> str:
        return f"AbsDice({self.die})"


class NegDice(FunctionDice):
    def __init__(self, base_die: BaseDice) -> None:
        super().__init__(base_die)
        self.max_side = base_die.max_side

    def apply_logic(self, roll: int) -> int:
        return -roll

    def __str__(self) -> str:
        return f"NegDice({self.die})"


class DivisionDice(AlterDice):
    def __init__(self, base_die: BaseDice, divisor: int) -> None:
        if divisor == 0:
            raise ValueError("Divisor cannot be zero.")
        super().__init__(base_die, [divisor])
        self.max_side = base_die.max_side // divisor

    def apply_logic(self, roll: int) -> int:
        return roll // self.opperand[0]

    def __str__(self) -> str:
        return f"DivisionDice({self.die}, {self.opperand[0]})"
