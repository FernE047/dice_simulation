from dices.dice import Dice

"""This module contains dice that apply various mathematical operations to the results of other dice."""


class SumDice(Dice):
    def __init__(self, dice_list: list[Dice]) -> None:
        self.dice_list = dice_list
        self.sides = sum(die.sides for die in dice_list)

    def roll(self) -> int:
        return sum(die.roll() for die in self.dice_list)

    def __str__(self) -> str:
        dice_str = ", ".join(str(die) for die in self.dice_list)
        return f"SumDice([{dice_str}])"


class MultiplicationDice(Dice):
    def __init__(self, dice_list: list[Dice]) -> None:
        self.dice_list = dice_list
        self.sides = 1
        for die in dice_list:
            self.sides *= die.sides

    def roll(self) -> int:
        result = 1
        for die in self.dice_list:
            result *= die.roll()
        return result

    def __str__(self) -> str:
        dice_str = ", ".join(str(die) for die in self.dice_list)
        return f"MultiplicationDice([{dice_str}])"


class ExponentiationDice(Dice):
    """A dice representing the exponentiation of one dice by another. limited to 2 dice for simplicity."""

    def __init__(self, base_die: Dice, exponent_die: Dice) -> None:
        self.base_die = base_die
        self.exponent_die = exponent_die
        self.sides = base_die.sides**exponent_die.sides

    def roll(self) -> int:
        return self.base_die.roll() ** self.exponent_die.roll()

    def __str__(self) -> str:
        return f"ExponentiationDice({self.base_die}, {self.exponent_die})"


class ModuloDice(Dice):
    def __init__(self, dividend_die: Dice, divisor_die: Dice) -> None:
        self.dividend_die = dividend_die
        self.divisor_die = divisor_die
        self.sides = dividend_die.sides

    def roll(self) -> int:
        dividend = self.dividend_die.roll()
        divisor = self.divisor_die.roll()
        return dividend % divisor

    def __str__(self) -> str:
        return f"ModuloDice({self.dividend_die}, {self.divisor_die})"


class FloorDivisionDice(Dice):
    def __init__(self, dividend_die: Dice, divisor_die: Dice) -> None:
        self.dividend_die = dividend_die
        self.divisor_die = divisor_die
        self.sides = dividend_die.sides

    def roll(self) -> int:
        dividend = self.dividend_die.roll()
        divisor = self.divisor_die.roll()
        return dividend // divisor

    def __str__(self) -> str:
        return f"FloorDivisionDice({self.dividend_die}, {self.divisor_die})"


class GCDDice(Dice):
    def __init__(self, dice_list: list[Dice]) -> None:
        self.dice_list = dice_list
        self.sides = min(die.sides for die in dice_list)

    def roll(self) -> int:
        from math import gcd

        rolls = [die.roll() for die in self.dice_list]
        return gcd(*rolls)

    def __str__(self) -> str:
        dice_str = ", ".join(str(die) for die in self.dice_list)
        return f"GCDDice([{dice_str}])"


class LCMDice(Dice):
    def __init__(self, dice_list: list[Dice]) -> None:
        self.dice_list = dice_list
        self.sides = max(die.sides for die in dice_list)

    def roll(self) -> int:
        from math import gcd

        rolls = [die.roll() for die in self.dice_list]
        total = 1
        for r in rolls:
            total *= r
        gcd_rolls = gcd(*rolls)
        return abs(total) // gcd_rolls

    def __str__(self) -> str:
        dice_str = ", ".join(str(die) for die in self.dice_list)
        return f"LCMDice([{dice_str}])"


class HipotenuseDice(Dice):
    def __init__(self, side_a_die: Dice, side_b_die: Dice) -> None:
        self.side_a_die = side_a_die
        self.side_b_die = side_b_die
        self.sides = int((side_a_die.sides**2 + side_b_die.sides**2) ** 0.5)

    def roll(self) -> int:
        from math import sqrt

        side_a = self.side_a_die.roll()
        side_b = self.side_b_die.roll()
        return int(sqrt(side_a**2 + side_b**2))

    def __str__(self) -> str:
        return f"HipotenuseDice({self.side_a_die}, {self.side_b_die})"


class CatetusDice(Dice):
    def __init__(self, hipotenuse_die: Dice, known_side_die: Dice) -> None:
        self.hipotenuse_die = hipotenuse_die
        self.known_side_die = known_side_die
        self.sides = hipotenuse_die.sides

    def roll(self) -> int:
        from math import sqrt

        hipotenuse = self.hipotenuse_die.roll()
        known_side = self.known_side_die.roll()
        return int(sqrt(hipotenuse**2 - known_side**2))

    def __str__(self) -> str:
        return f"CatetusDice({self.hipotenuse_die}, {self.known_side_die})"


class ConcatenationDice(Dice):
    def __init__(self, dice_list: list[Dice]) -> None:
        self.dice_list = dice_list
        self.sides = int("".join(str(die.sides) for die in dice_list))

    def roll(self) -> int:
        rolls = [str(die.roll()) for die in self.dice_list]
        rolls.sort(reverse=True)
        return int("".join(rolls))

    def __str__(self) -> str:
        dice_str = ", ".join(str(die) for die in self.dice_list)
        return f"ConcatenationDice([{dice_str}])"