from typing import cast
from dices.dice import AlterDice, BaseDice, Dice, FunctionDice


class RemoveItemDice(Dice):
    def __init__(self, sides: list[int]) -> None:
        super().__init__(sides)
        self.original_sides = sides.copy()

    def remove_item(self, item: int) -> None:
        if item in self.sides:
            self.sides.remove(item)

    def roll(self) -> int:
        if not self.sides:
            return 0
        value = super().roll()
        self.remove_item(value)
        return value

    def reset(self) -> None:
        self.sides = self.original_sides.copy()

    def __str__(self) -> str:
        return f"RemoveItemDice({self.sides})"


class AddItemDice(Dice):
    def __init__(self, sides: list[int]) -> None:
        super().__init__(sides)
        self.original_sides = sides.copy()

    def roll(self) -> int:
        value = super().roll()
        self.sides.append(value)
        return value

    def reset(self) -> None:
        self.sides = self.original_sides.copy()

    def __str__(self) -> str:
        return f"AddItemDice({self.sides})"


class AccumulatorSumDice(FunctionDice):
    def __init__(self, die: BaseDice) -> None:
        super().__init__(die)
        self._accumulated_sum = 0

    def apply_logic(self, roll: int) -> int:
        self._accumulated_sum += roll
        return self._accumulated_sum

    def reset(self) -> None:
        self._accumulated_sum = 0

    def __str__(self) -> str:
        return f"AccumulatorSumDice({self.die}, {self._accumulated_sum})"


class AccumulatorProductDice(FunctionDice):
    def __init__(self, die: BaseDice) -> None:
        super().__init__(die)
        self._accumulated_product = 1

    def apply_logic(self, roll: int) -> int:
        self._accumulated_product *= roll
        return self._accumulated_product

    def reset(self) -> None:
        self._accumulated_product = 1

    def __str__(self) -> str:
        return f"AccumulatorProductDice({self.die}, {self._accumulated_product})"


class MaxStateDice(FunctionDice):
    def __init__(self, die: BaseDice) -> None:
        super().__init__(die)
        self.max_roll = float("-inf")

    def apply_logic(self, roll: int) -> int:
        if roll > self.max_roll:
            self.max_roll = roll
        return cast(int, self.max_roll)

    def reset(self) -> None:
        self.max_roll = float("-inf")

    def __str__(self) -> str:
        return f"MaxStateDice({self.die}, {self.max_roll})"


class MinStateDice(FunctionDice):
    def __init__(self, die: BaseDice) -> None:
        super().__init__(die)
        self.min_roll = float("inf")

    def apply_logic(self, roll: int) -> int:
        if roll < self.min_roll:
            self.min_roll = roll
        return cast(int, self.min_roll)

    def reset(self) -> None:
        self.min_roll = float("inf")

    def __str__(self) -> str:
        return f"MinStateDice({self.die}, {self.min_roll})"


class CountOccurrencesDice(FunctionDice):
    def __init__(self, die: BaseDice) -> None:
        super().__init__(die)
        self.occurrences: dict[int, int] = {}

    def apply_logic(self, roll: int) -> int:
        if roll in self.occurrences:
            self.occurrences[roll] += 1
        else:
            self.occurrences[roll] = 1
        return self.occurrences[roll]

    def reset(self) -> None:
        self.occurrences = {}

    def __str__(self) -> str:
        return f"CountOccurrencesDice({self.die})"


class AverageStateDice(FunctionDice):
    def __init__(self, die: BaseDice) -> None:
        super().__init__(die)
        self.total = 0
        self.count = 0

    def apply_logic(self, roll: int) -> int:
        self.total += roll
        self.count += 1
        return self.total // self.count if self.count > 0 else 0

    def reset(self) -> None:
        self.total = 0
        self.count = 0

    def __str__(self) -> str:
        return f"AverageStateDice({self.die}, {self.total}, {self.count})"


class ThePastDice(AlterDice):
    def __init__(self, die: BaseDice, n: int) -> None:
        super().__init__(die, [n])
        self.past_rolls: list[int] = []

    def apply_logic(self, roll: int) -> int:
        if len(self.past_rolls) < self.opperand[0]:
            self.past_rolls.append(roll)
            return 0
        else:
            past_roll = self.past_rolls.pop(0)
            self.past_rolls.append(roll)
            return past_roll

    def reset(self) -> None:
        self.past_rolls = []

    def __str__(self) -> str:
        return f"ThePastDice({self.die}, {self.opperand[0]})"


class WaitDice(AlterDice):
    # test if a fixed time has passed to get used
    def __init__(self, die: BaseDice, wait_time: int) -> None:
        super().__init__(die, [wait_time])
        from datetime import datetime

        self.current_time = datetime.now()

    def apply_logic(self, roll: int) -> int:
        from datetime import datetime, timedelta

        if datetime.now() - self.current_time >= timedelta(seconds=self.opperand[0]):
            self.current_time = datetime.now()
            return roll
        else:
            return 0

    def reset(self) -> None:
        from datetime import datetime

        self.current_time = datetime.now()

    def __str__(self) -> str:
        return f"WaitDice({self.die}, {self.opperand[0]})"


class LimitUsesDice(AlterDice):
    def __init__(self, die: BaseDice, max_uses: int) -> None:
        super().__init__(die, [max_uses])
        self.uses_left = max_uses

    def apply_logic(self, roll: int) -> int:
        if self.uses_left > 0:
            self.uses_left -= 1
            return roll
        else:
            return 0

    def reset(self) -> None:
        self.uses_left = self.opperand[0]

    def __str__(self) -> str:
        return f"LimitUsesDice({self.die}, {self.opperand[0]}, {self.uses_left})"
