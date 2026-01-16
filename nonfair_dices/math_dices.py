from fair_dices.dice import Dice


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
        self.sides = base_die.sides ** exponent_die.sides

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