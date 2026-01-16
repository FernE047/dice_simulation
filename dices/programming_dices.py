from dices.dice import BaseDice


class RoutingDice(BaseDice):
    def __init__(self, decision_dice: BaseDice, dices: list[BaseDice]) -> None:
        if not dices:
            raise ValueError("At least one dice must be provided")
        if len(dices) != decision_dice.max_side:
            raise ValueError(
                "Number of dices must match the sides of the decision dice"
            )
        self.max_side = sum(dice.max_side for dice in dices)
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


class ForLoopDice(BaseDice):
    def __init__(self, base_die: BaseDice, iterations_die: BaseDice) -> None:
        self.base_die = base_die
        self.iterations_die = iterations_die
        self.max_side = base_die.max_side * iterations_die.max_side

    def roll(self) -> int:
        total = 0
        iterations = self.iterations_die.roll()
        for _ in range(iterations):
            total += self.base_die.roll()
        return total

    def __str__(self) -> str:
        return f"ForLoopDice({self.base_die}, {self.iterations_die})"


class WhileLoopDice(BaseDice):
    def __init__(
        self, base_die: BaseDice, condition_die: BaseDice, target: int
    ) -> None:
        self.base_die = base_die
        self.condition_die = condition_die
        self.target = target
        self.max_side = float("inf")  # Theoretically unbounded, it can break some other dice logic

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
