from fair_dices.dice import Dice
from fair_dices.mod_dice import ModDice
from fair_dices.product_dice import DuoDice
from nonlocal_fair_dices.composed_dice import OneExtraSideDice

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

dice_9 = DuoDice(dice_3, dice_3)
dice_15 = DuoDice(dice_3, dice_5)
dice_16 = DuoDice(dice_4, dice_4)
dice_18 = DuoDice(dice_3, dice_6)
dice_24 = DuoDice(dice_2, dice_6)
dice_25 = DuoDice(dice_5, dice_5)
dice_27 = DuoDice(dice_3, dice_9)
dice_30 = DuoDice(dice_5, dice_6)
dice_32 = DuoDice(dice_8, dice_4)
dice_36 = DuoDice(dice_6, dice_6)
dice_40 = DuoDice(dice_5, dice_8)
dice_45 = DuoDice(dice_9, dice_5)
dice_48 = DuoDice(dice_4, dice_12)
dice_50 = DuoDice(dice_5, dice_10)
dice_54 = DuoDice(dice_3, dice_18)
dice_60 = DuoDice(dice_5, dice_12)
dice_64 = DuoDice(dice_8, dice_8)
dice_72 = DuoDice(dice_6, dice_12)
dice_75 = DuoDice(dice_5, dice_15)
dice_80 = DuoDice(dice_5, dice_16)
dice_81 = DuoDice(dice_3, dice_27)
dice_90 = DuoDice(dice_5, dice_18)
dice_96 = DuoDice(dice_8, dice_12)
dice_100 = DuoDice(dice_10, dice_10)

# 4. unfair, but fair dices

dice_7 = OneExtraSideDice(dice_6)
dice_11 = OneExtraSideDice(dice_10)
dice_13 = OneExtraSideDice(dice_12)
dice_17 = OneExtraSideDice(dice_16)
dice_19 = OneExtraSideDice(dice_18)
dice_31 = OneExtraSideDice(dice_30)
dice_37 = OneExtraSideDice(dice_36)
dice_41 = OneExtraSideDice(dice_40)
dice_61 = OneExtraSideDice(dice_60)
dice_73 = OneExtraSideDice(dice_72)
dice_97 = OneExtraSideDice(dice_96)

# we combine a few more and then make more contraption dice
dice_14 = DuoDice(dice_7, dice_2)
dice_21 = DuoDice(dice_7, dice_3)
dice_28 = DuoDice(dice_7, dice_4)
dice_35 = DuoDice(dice_7, dice_5)
dice_42 = DuoDice(dice_7, dice_6)
dice_49 = DuoDice(dice_7, dice_7)
dice_56 = DuoDice(dice_7, dice_8)
dice_63 = DuoDice(dice_7, dice_9)
dice_70 = DuoDice(dice_7, dice_10)
dice_84 = DuoDice(dice_7, dice_12)
dice_98 = DuoDice(dice_7, dice_14)
dice_22 = DuoDice(dice_11, dice_2)
dice_33 = DuoDice(dice_11, dice_3)
dice_44 = DuoDice(dice_11, dice_4)
dice_55 = DuoDice(dice_11, dice_5)
dice_66 = DuoDice(dice_11, dice_6)
dice_77 = DuoDice(dice_11, dice_7)
dice_88 = DuoDice(dice_11, dice_8)
dice_99 = DuoDice(dice_11, dice_9)
dice_26 = DuoDice(dice_13, dice_2)
dice_39 = DuoDice(dice_13, dice_3)
dice_52 = DuoDice(dice_13, dice_4)
dice_65 = DuoDice(dice_13, dice_5)
dice_78 = DuoDice(dice_13, dice_6)
dice_91 = DuoDice(dice_13, dice_7)
dice_34 = DuoDice(dice_17, dice_2)
dice_51 = DuoDice(dice_17, dice_3)
dice_68 = DuoDice(dice_17, dice_4)
dice_85 = DuoDice(dice_17, dice_5)
dice_38 = DuoDice(dice_19, dice_2)
dice_57 = DuoDice(dice_19, dice_3)
dice_76 = DuoDice(dice_19, dice_4)
dice_95 = DuoDice(dice_19, dice_5)
dice_62 = DuoDice(dice_31, dice_2)
dice_93 = DuoDice(dice_31, dice_3)
dice_74 = DuoDice(dice_37, dice_2)
dice_82 = DuoDice(dice_41, dice_2)

# rinse and repeat
dice_23 = OneExtraSideDice(dice_22)
dice_29 = OneExtraSideDice(dice_28)
dice_43 = OneExtraSideDice(dice_42)
dice_53 = OneExtraSideDice(dice_52)
dice_67 = OneExtraSideDice(dice_66)
dice_71 = OneExtraSideDice(dice_70)
dice_79 = OneExtraSideDice(dice_78)
dice_83 = OneExtraSideDice(dice_82)
dice_89 = OneExtraSideDice(dice_88)

dice_46 = DuoDice(dice_23, dice_2)
dice_69 = DuoDice(dice_23, dice_3)
dice_92 = DuoDice(dice_23, dice_4)
dice_58 = DuoDice(dice_29, dice_2)
dice_87 = DuoDice(dice_29, dice_3)
dice_86 = DuoDice(dice_43, dice_2)

dice_47 = OneExtraSideDice(dice_46)
dice_59 = OneExtraSideDice(dice_58)

dice_94 = DuoDice(dice_47, dice_2)

all_dices: list[Dice] = [
    Dice(0),  # placeholder for index 0
    dice_1,
    dice_2,
    dice_3,
    dice_4,
    dice_5,
    dice_6,
    dice_7,
    dice_8,
    dice_9,
    dice_10,
    dice_11,
    dice_12,
    dice_13,
    dice_14,
    dice_15,
    dice_16,
    dice_17,
    dice_18,
    dice_19,
    dice_20,
    dice_21,
    dice_22,
    dice_23,
    dice_24,
    dice_25,
    dice_26,
    dice_27,
    dice_28,
    dice_29,
    dice_30,
    dice_31,
    dice_32,
    dice_33,
    dice_34,
    dice_35,
    dice_36,
    dice_37,
    dice_38,
    dice_39,
    dice_40,
    dice_41,
    dice_42,
    dice_43,
    dice_44,
    dice_45,
    dice_46,
    dice_47,
    dice_48,
    dice_49,
    dice_50,
    dice_51,
    dice_52,
    dice_53,
    dice_54,
    dice_55,
    dice_56,
    dice_57,
    dice_58,
    dice_59,
    dice_60,
    dice_61,
    dice_62,
    dice_63,
    dice_64,
    dice_65,
    dice_66,
    dice_67,
    dice_68,
    dice_69,
    dice_70,
    dice_71,
    dice_72,
    dice_73,
    dice_74,
    dice_75,
    dice_76,
    dice_77,
    dice_78,
    dice_79,
    dice_80,
    dice_81,
    dice_82,
    dice_83,
    dice_84,
    dice_85,
    dice_86,
    dice_87,
    dice_88,
    dice_89,
    dice_90,
    dice_91,
    dice_92,
    dice_93,
    dice_94,
    dice_95,
    dice_96,
    dice_97,
    dice_98,
    dice_99,
    dice_100,
]
