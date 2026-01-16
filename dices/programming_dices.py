from dices.dice import BaseDice, BiDice, DiceOfDices, FunctionDice

class AndDice(DiceOfDices):
    def __init__(self, dice_list: list[BaseDice]) -> None:
        super().__init__(dice_list)
        self.max_side = 2  # True or False

    def apply_logic(self, rolls: list[int]) -> int:
        return int(all(rolls))

    def __str__(self) -> str:
        dice_str = ", ".join(str(die) for die in self.dices)
        return f"AndDice([{dice_str}])"

class OrDice(DiceOfDices):
    def __init__(self, dice_list: list[BaseDice]) -> None:
        super().__init__(dice_list)
        self.max_side = 2  # True or False

    def apply_logic(self, rolls: list[int]) -> int:
        return int(any(rolls))

    def __str__(self) -> str:
        dice_str = ", ".join(str(die) for die in self.dices)
        return f"OrDice([{dice_str}])"

class NotDice(FunctionDice):
    def __init__(self, dice: BaseDice) -> None:
        super().__init__(dice)
        self.max_side = 2  # True or False

    def apply_logic(self, roll: int) -> int:
        return 1 if roll == 0 else 0

    def __str__(self) -> str:
        return f"NotDice({self.die})"

class XorDice(BiDice):
    def __init__(self, dice_a: BaseDice, dice_b: BaseDice) -> None:
        super().__init__(dice_a, dice_b)
        self.max_side = 2  # True or False

    def apply_logic(self, roll_a: int, roll_b: int) -> int:
        return int((roll_a != 0) ^ (roll_b != 0))

    def __str__(self) -> str:
        return f"XorDice({self.dice_a}, {self.dice_b})"

class RoutingDice(DiceOfDices):
    def __init__(self, decision_dice: BaseDice, dices: list[BaseDice]) -> None:
        if not dices:
            raise ValueError("At least one dice must be provided")
        if len(dices) != decision_dice.max_side:
            raise ValueError(
                "Number of dices must match the sides of the decision dice"
            )
        super().__init__([decision_dice] + dices)
        self.max_side = sum(dice.max_side for dice in dices)

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
        self,
        base_die: BaseDice,
        condition_die: BaseDice,
        target: int,
        loop_limit: int = 5,
    ) -> None:
        super().__init__([condition_die] * loop_limit + [base_die] * loop_limit)
        self.target = target
        self.loop_limit = loop_limit
        self.max_side = loop_limit * base_die.max_side

    def apply_logic(self, rolls: list[int]) -> int:
        total = 0
        condition_rolls = rolls[: self.loop_limit]
        base_rolls = rolls[self.loop_limit :]
        for cond_roll, base_roll in zip(condition_rolls, base_rolls):
            if cond_roll == self.target:
                break
            total += base_roll
        return total

    def __str__(self) -> str:
        return f"WhileLoopDice({self.dices[self.loop_limit]}, {self.dices[0]}, {self.target})"
