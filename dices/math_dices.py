from dices.dice import BaseDice, BiDice, DiceOfDices

"""This module contains dice that apply various mathematical operations to the results of other dice."""


class SumDice(DiceOfDices):
    def __init__(self, dice_list: list[BaseDice]) -> None:
        super().__init__(dice_list)
        self.max_side = sum(die.max_side for die in self.dices)

    def apply_logic(self, rolls: list[int]) -> int:
        return sum(rolls)

    def __str__(self) -> str:
        dice_str = ", ".join(str(die) for die in self.dices)
        return f"SumDice([{dice_str}])"


class MultiplicationDice(DiceOfDices):
    def __init__(self, dice_list: list[BaseDice]) -> None:
        super().__init__(dice_list)
        self.max_side = 1
        for die in self.dices:
            self.max_side *= die.max_side

    def apply_logic(self, rolls: list[int]) -> int:
        result = 1
        for roll in rolls:
            result *= roll
        return result

    def __str__(self) -> str:
        dice_str = ", ".join(str(die) for die in self.dices)
        return f"MultiplicationDice([{dice_str}])"


class ExponentiationDice(BiDice):
    """A dice representing the exponentiation of one dice by another. limited to 2 dice for simplicity."""

    def __init__(self, base_die: BaseDice, exponent_die: BaseDice) -> None:
        super().__init__(base_die, exponent_die)
        self.max_side = base_die.max_side**exponent_die.max_side

    def apply_logic(self, roll_a: int, roll_b: int) -> int:
        return roll_a**roll_b

    def __str__(self) -> str:
        return f"ExponentiationDice({self.dice_a}, {self.dice_b})"


class ModuloDice(BiDice):
    def __init__(self, dividend_die: BaseDice, divisor_die: BaseDice) -> None:
        super().__init__(dividend_die, divisor_die)
        self.max_side = dividend_die.max_side

    def apply_logic(self, roll_a: int, roll_b: int) -> int:
        return roll_a % roll_b

    def __str__(self) -> str:
        return f"ModuloDice({self.dice_a}, {self.dice_b})"


class FloorDivisionDice(BiDice):
    def __init__(self, dividend_die: BaseDice, divisor_die: BaseDice) -> None:
        super().__init__(dividend_die, divisor_die)
        self.max_side = dividend_die.max_side

    def apply_logic(self, roll_a: int, roll_b: int) -> int:
        return roll_a // roll_b

    def __str__(self) -> str:
        return f"FloorDivisionDice({self.dice_a}, {self.dice_b})"


class GCDDice(DiceOfDices):
    def __init__(self, dice_list: list[BaseDice]) -> None:
        super().__init__(dice_list)
        self.max_side = min(die.max_side for die in self.dices)

    def apply_logic(self, rolls: list[int]) -> int:
        from math import gcd

        return gcd(*rolls)

    def __str__(self) -> str:
        dice_str = ", ".join(str(die) for die in self.dices)
        return f"GCDDice([{dice_str}])"


class LCMDice(DiceOfDices):
    def __init__(self, dice_list: list[BaseDice]) -> None:
        super().__init__(dice_list)
        self.max_side = max(die.max_side for die in self.dices)

    def apply_logic(self, rolls: list[int]) -> int:
        from math import gcd

        total = 1
        for r in rolls:
            total *= r
        gcd_rolls = gcd(*rolls)
        return abs(total) // gcd_rolls

    def __str__(self) -> str:
        dice_str = ", ".join(str(die) for die in self.dices)
        return f"LCMDice([{dice_str}])"


class HipotenuseDice(BiDice):
    def __init__(self, side_a_die: BaseDice, side_b_die: BaseDice) -> None:
        super().__init__(side_a_die, side_b_die)
        self.max_side = int((side_a_die.max_side**2 + side_b_die.max_side**2) ** 0.5)

    def apply_logic(self, roll_a: int, roll_b: int) -> int:
        from math import sqrt

        return int(sqrt(roll_a**2 + roll_b**2))

    def __str__(self) -> str:
        return f"HipotenuseDice({self.dice_a}, {self.dice_b})"


class CatetusDice(BiDice):
    def __init__(self, hipotenuse_die: BaseDice, known_side_die: BaseDice) -> None:
        super().__init__(hipotenuse_die, known_side_die)
        self.max_side = hipotenuse_die.max_side

    def apply_logic(self, roll_a: int, roll_b: int) -> int:
        from math import sqrt

        hipotenuse = roll_a
        known_side = roll_b
        return int(sqrt(hipotenuse**2 - known_side**2))

    def __str__(self) -> str:
        return f"CatetusDice({self.dice_a}, {self.dice_b})"

class ConcatenationDice(DiceOfDices):
    def __init__(self, dice_list: list[BaseDice]) -> None:
        super().__init__(dice_list)
        self.max_side = int("".join(str(die.max_side) for die in dice_list))

    def apply_logic(self, rolls: list[int]) -> int:
        rolls_str = [str(r) for r in rolls]
        rolls_str.sort(reverse=True)
        return int("".join(rolls_str))

    def __str__(self) -> str:
        dice_str = ", ".join(str(die) for die in self.dices)
        return f"ConcatenationDice([{dice_str}])"
