from dice import Dice
from mod_dice import ModDice

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