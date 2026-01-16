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


class ForLoopDice(Dice):
    def __init__(self, base_die: Dice, iterations_die: Dice) -> None:
        self.base_die = base_die
        self.iterations_die = iterations_die
        self.sides = base_die.sides * iterations_die.sides

    def roll(self) -> int:
        total = 0
        iterations = self.iterations_die.roll()
        for _ in range(iterations):
            total += self.base_die.roll()
        return total

    def __str__(self) -> str:
        return f"ForLoopDice({self.base_die}, {self.iterations_die})"


class WhileLoopDice(Dice):
    """This one breaks everything because of infinite loops"""

    def __init__(self, base_die: Dice, condition_die: Dice, target: int) -> None:
        self.base_die = base_die
        self.condition_die = condition_die
        self.target = target

    def roll(self) -> int:
        total = 0
        while True:
            condition_roll = self.condition_die.roll()
            if condition_roll != self.target:
                break
            total += self.base_die.roll()
        return total

    def __str__(self) -> str:
        return f"WhileLoopDice({self.base_die}, {self.condition_die}, {self.target})"
