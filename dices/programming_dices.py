from dices.dice import BaseDice, DiceOfDices


class RoutingDice(DiceOfDices):
    def __init__(self, decision_dice: BaseDice, dices: list[BaseDice]) -> None:
        if not dices:
            raise ValueError("At least one dice must be provided")
        if len(dices) != decision_dice.max_side:
            raise ValueError(
                "Number of dices must match the sides of the decision dice"
            )
        super().__init__([decision_dice] + dices)
        self.max_side = sum(dice.max_side for dice in dices[1:])

    def apply_logic(self, rolls: list[int]) -> int:
        decision = rolls[0]
        selected_dice_roll = rolls[decision]
        return selected_dice_roll

    def __str__(self) -> str:
        dices_explain = ", ".join(str(dice) for dice in self.dices[1:])
        return f"RoutingDice({self.dices[0]}, [{dices_explain}])"


class ForLoopDice(DiceOfDices):
    def __init__(self, base_die: BaseDice, iterations_die: BaseDice) -> None:
        super().__init__([iterations_die] + [base_die] * int(iterations_die.max_side))
        self.max_side = base_die.max_side * iterations_die.max_side

    def apply_logic(self, rolls: list[int]) -> int:
        iterations = rolls[0]
        total = sum(rolls[1 : iterations + 1])
        return total

    def __str__(self) -> str:
        return f"ForLoopDice({self.dices[1]}, {self.dices[0]})"


class WhileLoopDice(DiceOfDices):
    def __init__(
        self, base_die: BaseDice, condition_die: BaseDice, target: int
    ) -> None:
        super().__init__([condition_die] * 100 + [base_die] * 100) # Arbitrary large number to allow multiple rolls
        self.target = target
        self.max_side = 100 * base_die.max_side

    def apply_logic(self, rolls: list[int]) -> int:
        total = 0
        condition_rolls = rolls[:100]
        base_rolls = rolls[100:]
        for cond_roll, base_roll in zip(condition_rolls, base_rolls):
            if cond_roll != self.target:
                break
            total += base_roll
        return total

    def __str__(self) -> str:
        return f"WhileLoopDice({self.dices[100]}, {self.dices[0]}, {self.target})"
