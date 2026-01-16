from dices.dice import BaseDice, DiceOfDices


class AdvantageDices(DiceOfDices):
    def __init__(self, dices: list[BaseDice]) -> None:
        super().__init__(dices)
        self.max_side = max(dice.max_side for dice in dices)

    def apply_logic(self, rolls: list[int]) -> int:
        return max(rolls)

    def __str__(self) -> str:
        dices_str = ", ".join(str(dice) for dice in self.dices)
        return f"AdvantageDices([{dices_str}])"


class DisadvantageDices(DiceOfDices):
    def __init__(self, dices: list[BaseDice]) -> None:
        super().__init__(dices)
        self.max_side = min(
            dice.max_side for dice in dices
        )  # because if a dice has less sides, the min will never be higher than that

    def apply_logic(self, rolls: list[int]) -> int:
        return min(rolls)

    def __str__(self) -> str:
        dices_str = ", ".join(str(dice) for dice in self.dices)
        return f"DisadvantageDices([{dices_str}])"


class ComboDice(DiceOfDices):
    """Warning: this dice can take a long time to roll, because it simulates 100 rolls always"""
    def __init__(
        self,
        dice: BaseDice,
        target: list[int] | None = None,
        non_target: list[int] | None = None,
    ) -> None:
        if target is None and non_target is None:
            raise ValueError("Either target or non_target must be provided.")
        if target is None:
            target = []
        if non_target is None:
            non_target = []
        super().__init__([dice] * 100) # Arbitrary large number to allow multiple rolls
        self.target = target
        self.non_target = non_target
        self.max_side = dice.max_side

    def _stop(self, roll: int) -> bool:
        if self.target:
            return roll not in self.target
        if self.non_target:
            return roll in self.non_target
        return False

    def apply_logic(self, rolls: list[int]) -> int:
        total = 0
        for roll in rolls:
            total += roll
            if self._stop(roll):
                break
        return total

    def __str__(self) -> str:
        return f"ComboDice({self.dices[0]}, {self.target}, {self.non_target})"
