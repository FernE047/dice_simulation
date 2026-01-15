from dice import Dice

# uses the modulo operator to create a die


class ModDice(Dice):
    def __init__(self, base_die: Dice, modulo: int = 0) -> None:
        self.base_die = base_die
        self.modulo = modulo

    def roll(self) -> int:
        return self.base_die.roll() % self.modulo + 1
