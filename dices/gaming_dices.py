from dices.dice import BaseDice


class AdvantageDices(BaseDice):
    def __init__(self, dices: list[BaseDice]) -> None:
        self.dices = dices
        self.max_side = max(dice.max_side for dice in dices)

    def roll(self) -> int:
        return max(dice.roll() for dice in self.dices)

    def __str__(self) -> str:
        dices_str = ", ".join(str(dice) for dice in self.dices)
        return f"AdvantageDices([{dices_str}])"


class DisadvantageDices(BaseDice):
    def __init__(self, dices: list[BaseDice]) -> None:
        self.dices = dices
        self.max_side = min(
            dice.max_side for dice in dices
        )  # because if a dice has less sides, the min will never be higher than that

    def roll(self) -> int:
        return min(dice.roll() for dice in self.dices)

    def __str__(self) -> str:
        dices_str = ", ".join(str(dice) for dice in self.dices)
        return f"DisadvantageDices([{dices_str}])"


class ComboDice(BaseDice):
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
        self.dice = dice
        self.target = target
        self.non_target = non_target
        self.max_side = dice.max_side

    def _stop(self, roll: int) -> bool:
        if self.target:
            return roll not in self.target
        if self.non_target:
            return roll in self.non_target
        return False

    def roll(self) -> int:
        total = 0
        while True:
            roll = self.dice.roll()
            total += roll
            if self._stop(roll):
                break
        return total
