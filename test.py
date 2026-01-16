from dices.dice import BaseDice, SequentialDice, Dice
from dices.composed_dice import MultiDice, DuoDice, ComposedDice, OneExtraSideDice
from dices.gaming_dices import AdvantageDices, ComboDice, DisadvantageDices
from dices.math_operations_dices import (
    ModDice,
    PrimeDice,
    OffsetDice,
    FloorDice,
    CeilDice,
    ClampDice,
    FactorDice,
    FactorialDice,
    PowerDice,
    SqrtDice,
    LogDice,
    ExpDice,
    AbsDice,
    NegDice,
    DivisionDice,
)
from dices.math_dices import (
    SumDice,
    MultiplicationDice,
    ExponentiationDice,
    ModuloDice,
    FloorDivisionDice,
    GCDDice,
    LCMDice,
    HipotenuseDice,
    CatetusDice,
    ConcatenationDice,
)
from dices.programming_dices import (
    RoutingDice,
    ForLoopDice,
    WhileLoopDice,
    AndDice,
    OrDice,
    NotDice,
    XorDice,
)
from dices.statistical_dices import (
    MeanDice,
    MedianDice,
    ModeDice,
    VarianceDice,
    StdDevDice,
    RangeDice,
    WeightedMeanDice,
)


def probs(dices: list[BaseDice]) -> None:
    for dice in dices:
        print(f"Probabilities for {dice}:")
        dice.print_probabilities()
        print()


dice_3 = SequentialDice(3)
dice_4 = SequentialDice(4)
dice_5 = SequentialDice(5)
dice_6 = SequentialDice(6)
dice_8 = SequentialDice(8)
dice_10 = SequentialDice(10)
dice_12 = SequentialDice(12)
dice_20 = SequentialDice(20)

probs([dice_4, dice_6, dice_8, dice_10, dice_12, dice_20])


dice_weird_1 = Dice([1, 2, 2, 3, 3, 3])
dice_weird_2 = Dice([0, 0, 5, 5, 10])
dice_weird_3 = Dice([1, 3, 4, 61, 8, 4, 120])
dice_weird_4 = Dice([1, 2, 4, 8, 16, 32, 64, 128])

probs([dice_weird_1, dice_weird_2, dice_weird_3, dice_weird_4])


math_dices: list[BaseDice] = [
    ModDice(dice_6, 2),
    PrimeDice(dice_20),
    OffsetDice(dice_8, 3),
    FloorDice(dice_10, 3),
    CeilDice(dice_10, 5),
    ClampDice(dice_12, 3, 9),
    FactorDice(dice_6, 12),
    FactorialDice(dice_4),
    PowerDice(dice_4, 2),
    SqrtDice(dice_20),
    LogDice(dice_20, 10),
    ExpDice(dice_6),
    AbsDice(Dice([-3, -2, -1, 0, 1, 2, 3])),
    NegDice(dice_6),
    DivisionDice(dice_10, 2),
]
probs(math_dices)


composed_dices: list[BaseDice] = [
    MultiDice([dice_6, dice_8]),
    DuoDice(dice_10, dice_4),
    ComposedDice(dice_3, [dice_6, dice_8, dice_4]),  # gives error
    OneExtraSideDice(dice_12),
]

probs(composed_dices)


gaming_dices: list[BaseDice] = [
    AdvantageDices([dice_20, dice_20, dice_20]),
    DisadvantageDices([dice_20, dice_20, dice_20]),
    ComboDice(dice_4, [4]),
]
probs(gaming_dices)


math_dices_2: list[BaseDice] = [
    SumDice([dice_6, dice_8]),
    MultiplicationDice([dice_4, dice_10]),
    ExponentiationDice(dice_4, dice_3),
    ModuloDice(dice_20, dice_5),
    FloorDivisionDice(dice_12, dice_5),
    GCDDice([dice_6, dice_10]),
    LCMDice([dice_4, dice_8]),
    HipotenuseDice(dice_6, dice_8),
    CatetusDice(dice_10, dice_6),
    ConcatenationDice([dice_4, dice_6]),
]
probs(math_dices_2)


programming_dices: list[BaseDice] = [
    AndDice([dice_6, dice_4]),
    OrDice([dice_6, dice_4]),
    NotDice(dice_6),
    XorDice(dice_6, dice_4),
    RoutingDice(dice_6, [dice_4, dice_8, dice_10, dice_3, dice_20, dice_4]),
    ForLoopDice(dice_4, dice_6),
    WhileLoopDice(dice_4, dice_4, 3),
]
probs(programming_dices)


statistical_dices: list[BaseDice] = [
    MeanDice([dice_6, dice_8, dice_10]),
    MedianDice([dice_6, dice_8, dice_10]),
    ModeDice([dice_6, dice_8, dice_10]),
    VarianceDice([dice_6, dice_8, dice_10]),
    StdDevDice([dice_6, dice_8, dice_10]),
    RangeDice([dice_6, dice_8, dice_10]),
    WeightedMeanDice(
        [dice_6, dice_8, dice_10], [dice_20, dice_20, dice_20]
    ),
]
probs(statistical_dices)

disadv_6 = DisadvantageDices([dice_6, dice_6])
adv_disadv_6 = AdvantageDices([dice_6, disadv_6])
adv_disadvs_6 = AdvantageDices([disadv_6, disadv_6])
probs([adv_disadv_6, adv_disadvs_6])

dices_6: list[BaseDice] = [dice_6]
for a in range(5):
    dices_6.append(MultiplicationDice([dice_6] * (a + 2)))
exploding_6 = RoutingDice(dice_6, dices_6)

exploding_6.print_simulated_probs(10000000)
