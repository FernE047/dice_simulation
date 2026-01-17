from dices.dice import BaseDice, BiDice, Dice, DiceOfDices, FunctionDice, OutcomesData


class TheFutureDice(BaseDice):  # joke dice
    def __init__(self, die: BaseDice) -> None:
        super().__init__()
        self.die = die

    def roll(self) -> int:
        return 1  # always predict 1

    def get_outcomes(self) -> OutcomesData:
        return [([1], 1)]

    def __str__(self) -> str:
        return f"TheFutureDice({self.die})"


class CarouselDice(DiceOfDices):
    def __init__(self, dices: list[BaseDice]) -> None:
        super().__init__(dices)
        self.index = 0

    def apply_logic(self, rolls: list[int]) -> int:
        result = rolls[self.index]
        self.index = (self.index + 1) % len(self.dices)
        return result

    def reset(self) -> None:
        self.index = 0

    def __str__(self) -> str:
        return f"CarouselDice({self.dices})"


class IgnoreDice(FunctionDice):  # joke dice
    def __init__(self, die: BaseDice) -> None:
        super().__init__(die)

    def apply_logic(self, roll: int) -> int:
        return 0  # always ignore the roll

    def __str__(self) -> str:
        return f"IgnoreDice({self.die})"


class BothAgreeDice(BiDice):
    def __init__(self, dice_a: BaseDice, dice_b: BaseDice) -> None:
        outcomes_a = dice_a.get_outcomes()
        outcomes_b = dice_b.get_outcomes()
        is_valid = False
        for _, result_a in outcomes_a:
            for _, result_b in outcomes_b:
                if result_a == result_b:
                    is_valid = True
                    break
        if not is_valid:
            raise ValueError(
                "BothAgreeDice requires at least one common outcome between the two dice."
            )
        super().__init__(dice_a, dice_b)

    def apply_logic(self, roll_a: int, roll_b: int) -> int:
        return int((roll_a != 0) and (roll_b != 0))

    def roll(self) -> int:
        while True:
            roll_a = self.dice_a.roll()
            roll_b = self.dice_b.roll()
            if roll_a == roll_b:
                return roll_a
            else:
                continue

    def __str__(self) -> str:
        return f"BothAgreeDice({self.dice_a}, {self.dice_b})"


class AlwaysMaxDice(FunctionDice):
    def __init__(self, die: BaseDice) -> None:
        super().__init__(die)

    def apply_logic(self, roll: int) -> int:
        return int(self.die.max_side)

    def __str__(self) -> str:
        return f"AlwaysMaxDice({self.die})"


class RandomErrorDice(FunctionDice):  # joke dice LMAO
    def __init__(self, die: BaseDice, error_rate: float) -> None:
        super().__init__(die)
        if not (0.0 <= error_rate <= 1.0):
            raise ValueError("error_rate must be between 0.0 and 1.0")
        self.error_rate = error_rate

    def apply_logic(self, roll: int) -> int:
        import random

        if random.random() < self.error_rate:
            raise ValueError("Random error occurred during dice roll.")
        else:
            return roll

    def __str__(self) -> str:
        return f"RandomErrorDice({self.die}, error_rate={self.error_rate})"


class SurpriseDice(Dice):
    def __init__(self, sides_amount: int, min_value: int, max_value: int) -> None:
        self.sides_amount = sides_amount
        self.min_value = min_value
        self.max_value = max_value
        self.change_sides()
        super().__init__(self.sides)

    def change_sides(self) -> None:
        import random

        sides = random.sample(
            range(self.min_value, self.max_value + 1), self.sides_amount
        )
        self.sides = sides

    def roll(self) -> int:
        result = super().roll()
        self.change_sides()
        return result

    def __str__(self) -> str:
        return f"SurpriseDice({self.sides})"
