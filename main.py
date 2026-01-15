from dices.composition_dice import CompositeDice
from dices.dice import Dice
from dices.mod_dice import ModDice

# 1. dices we have available to use

dice_4 = Dice(4)
dice_6 = Dice(6)
dice_8 = Dice(8)
dice_10 = Dice(10)
dice_12 = Dice(12)
dice_20 = Dice(20)

# 2. dice we mod

dice_1 = ModDice(dice_4, 1)
dice_2 = ModDice(dice_4, 2)
dice_3 = ModDice(dice_6, 3)
dice_5 = ModDice(dice_10, 5)

# 3. dice we combine

dice_9 = CompositeDice(dice_3, dice_3)
dice_15 = CompositeDice(dice_3, dice_5)
dice_16 = CompositeDice(dice_4, dice_4)
dice_18 = CompositeDice(dice_3, dice_6)
dice_24 = CompositeDice(dice_2, dice_6)
dice_25 = CompositeDice(dice_5, dice_5)
dice_27 = CompositeDice(dice_3, dice_9)
dice_30 = CompositeDice(dice_5, dice_6)
dice_32 = CompositeDice(dice_8, dice_4)
dice_36 = CompositeDice(dice_6, dice_6)
dice_40 = CompositeDice(dice_5, dice_8)
dice_45 = CompositeDice(dice_9, dice_5)
dice_48 = CompositeDice(dice_4, dice_12)
dice_50 = CompositeDice(dice_5, dice_10)
dice_54 = CompositeDice(dice_3, dice_18)
dice_60 = CompositeDice(dice_5, dice_12)
dice_64 = CompositeDice(dice_8, dice_8)
dice_72 = CompositeDice(dice_6, dice_12)
dice_75 = CompositeDice(dice_5, dice_15)
dice_80 = CompositeDice(dice_5, dice_16)
dice_81 = CompositeDice(dice_3, dice_27)
dice_90 = CompositeDice(dice_5, dice_18)
dice_96 = CompositeDice(dice_8, dice_12)
dice_100 = CompositeDice(dice_10, dice_10)
