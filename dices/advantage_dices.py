from fair_dices.dice import Dice


class AdvantageDices(Dice):
    def __init__(self, dices: list[Dice]) -> None:
        self.dices = dices
        self.sides = max(dice.sides for dice in dices)

    def roll(self) -> int:
        return max(dice.roll() for dice in self.dices)
    
    def __str__(self) -> str:
        dices_str = ", ".join(str(dice) for dice in self.dices)
        return f"AdvantageDices([{dices_str}])"

class DisadvantageDices(Dice):
    def __init__(self, dices: list[Dice]) -> None:
        self.dices = dices
        self.sides = min(dice.sides for dice in dices) #because if a dice has less sides, the min will never be higher than that

    def roll(self) -> int:
        return min(dice.roll() for dice in self.dices)
    
    def __str__(self) -> str:
        dices_str = ", ".join(str(dice) for dice in self.dices)
        return f"DisadvantageDices([{dices_str}])"