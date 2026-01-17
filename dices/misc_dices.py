from dices.dice import (
    AlterDice,
    BaseDice,
    BiDice,
    Dice,
    DiceOfDices,
    FunctionDice,
    OutcomesData,
)
import random


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


class RecursionHellDice(DiceOfDices):  # joke dice
    def __init__(self, dices: list[BaseDice]) -> None:
        super().__init__(dices + [self])

    def apply_logic(self, rolls: list[int]) -> int:
        return sum(rolls)

    def __str__(self) -> str:
        return f"RecursionHellDice({self.dices})"


class TalkativeDice(FunctionDice):
    def __init__(self, die: BaseDice) -> None:
        super().__init__(die)

    def apply_logic(self, roll: int) -> int:
        self.talk()
        return roll

    def talk(self) -> str:
        dialogues = [
            "I'm just a dice, but I have a lot to say!",
            "Roll me and let's see what fate has in store!",
            "I'm here to add some fun to your game!",
            "What will you roll today? Let's find out!",
            "Every roll is a tiny leap of faith.",
            "I don't choose the number, destiny does.",
            "Shake me gently, I'm sensitive.",
            "Go on, roll me. I dare you.",
            "I live for the sound of clattering plastic.",
            "High hopes, low numbers — classic.",
            "Luck is just chaos with good PR.",
            "I promise nothing. Ever.",
            "Sometimes I roll high. Sometimes I ruin lives.",
            "Don't blame me, blame probability.",
            "I contain multitudes. Mostly ones through six.",
            "One roll closer to victory… or disaster.",
            "I was born to tumble.",
            "Statistics say this will end badly.",
            "Roll responsibly.",
            "I feel lucky today. Do you?",
            "Fate is in your hands. Literally.",
            "I hope you stretched your expectations.",
            "I've seen things. Mostly tables.",
            "Let the dice decide. I am the dice.",
            "This roll will be important. Probably.",
            "I thrive on uncertainty.",
            "You shake, I speak.",
            "A moment of suspense, coming right up.",
            "Roll me like you mean it.",
            "I do my best work mid-air.",
            "The universe loves randomness.",
            "I am small, but powerful.",
            "Another roll, another timeline.",
            "Numbers are just opinions.",
            "Trust the process. Or don't.",
            "Your odds are… interesting.",
            "I sense a critical something.",
            "Hope is a dangerous thing to roll with.",
            "I never lie. I just roll.",
            "Prepare yourself emotionally.",
            "This is where plans go to die.",
            "I bring balance. And chaos.",
            "Roll first. Regret later.",
            "Destiny needs a little push.",
            "I like dramatic pauses.",
            "Click clack, here comes fate.",
            "I am impartial. Brutally so.",
            "You asked for this.",
            "Another spin of the universe.",
            "I was calibrated by chaos.",
            "No takebacks.",
            "Math is watching you.",
            "I decide faster than you think.",
            "Roll me and accept your truth.",
            "Every number has consequences.",
            "I enjoy the suspense more than you.",
            "This roll has vibes.",
            "Probability is my love language.",
            "The table trembles in anticipation.",
            "I roll, therefore I am.",
            "Some numbers hit harder than others.",
            "You look nervous. Good.",
            "The odds are never personal. Mostly.",
            "I can feel a low roll coming.",
            "Or maybe a high one. Who knows?",
            "I exist between hope and despair.",
            "One tiny cube. Infinite outcomes.",
            "Roll me like it's the final boss.",
            "Chaos, but make it fair.",
            "I am the great equalizer.",
            "This roll will define the moment.",
            "I hope you like surprises.",
            "Your fate is clattering already.",
            "I don't judge. I just land.",
            "A number approaches.",
            "Suspense is my favorite sound.",
            "I was shaken, not stirred.",
            "Even I don't know what I'll say.",
            "This is a statistically significant moment.",
            "Roll now. Overthink later.",
            "I bring numbers, not comfort.",
            "Every roll tells a story.",
            "I can feel the tension.",
            "Sometimes I shine. Sometimes I disappoint.",
            "I answer only to gravity.",
            "Let's consult the cube of destiny.",
            "Your move activated me.",
            "I'm ready when you are.",
            "Roll me. Accept me.",
            "This outcome is between you and the universe.",
        ]
        return random.choice(dialogues)


class SleepDice(AlterDice):
    # sleeps when rolling
    def __init__(self, die: BaseDice, sleep_time: int) -> None:
        super().__init__(die, [sleep_time])
        self.sleep_time = sleep_time

    def apply_logic(self, roll: int) -> int:
        from time import sleep

        sleep(self.sleep_time)
        return roll

    def __str__(self) -> str:
        return f"SleepDice({self.die}, {self.sleep_time})"


class SelfComplexityDice(FunctionDice):
    """This dice adds to its roll the number of characters in its own string representation.
    It's a dice that is aware of its own complexity.
    Very good to use with dices that get complex as they roll."""

    def __init__(self, die: BaseDice) -> None:
        super().__init__(die)

    def apply_logic(self, roll: int) -> int:
        complexity = len(str(self.die))
        return roll + complexity

    def __str__(self) -> str:
        return f"SelfComplexityDice({self.die})"


class CountDicesDice(FunctionDice):
    """This dice adds to its roll the number of dices it contains.
    Useful for meta-gaming scenarios where the complexity of the dice setup affects outcomes."""

    def __init__(self, die: BaseDice) -> None:
        super().__init__(die)

    def apply_logic(self, roll: int) -> int:
        text = str(self.die)
        count = text.count("Dice")
        # every dice class name contains "Dice", some have it twice, but that's fine
        return roll + count

    def __str__(self) -> str:
        return f"CountDicesDice({self.die})"
