from dices.dice import Dice


class RoutingDice(Dice):
    def __init__(self, decision_dice: Dice, dices: list[Dice]) -> None:
        if not dices:
            raise ValueError("At least one dice must be provided")
        if len(dices) != decision_dice.sides:
            raise ValueError(
                "Number of dices must match the sides of the decision dice"
            )
        self.sides = sum(dice.sides for dice in dices)
        self.decision_dice = decision_dice
        self.dices = dices

    def roll(self) -> int:
        decision = self.decision_dice.roll()
        selected_dice = self.dices[decision - 1]
        result = selected_dice.roll()
        return result

    def __str__(self) -> str:
        dices_explain = ", ".join(str(dice) for dice in self.dices)
        return f"RoutingDice({self.decision_dice}, [{dices_explain}])"
