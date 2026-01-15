from dices.dice import Dice


class ModDice(Dice):
    def __init__(self, base_die: Dice, modulo: int = 0) -> None:
        self.sides = modulo
        self.base_die = base_die
        self.modulo = modulo

    def roll(self) -> int:
        return self.base_die.roll() % self.modulo + 1
    
    def __str__(self) -> str:
        return f"ModDice(d{self.base_die.sides} % {self.modulo}) = d{self.sides}"
    
    def explain(self) -> str:
        return f"ModDice({self.base_die.explain()}, {self.modulo})"