from dices.dice import Dice
from dices.mod_dice import ModDice
from dices.composition_dice import CompositeDice
from dices.contraption_dice import ContraptionDice

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

# 4. unfair, but fair dices

dice_7 = ContraptionDice(dice_6)
dice_11 = ContraptionDice(dice_10)
dice_13 = ContraptionDice(dice_12)
dice_17 = ContraptionDice(dice_16)
dice_19 = ContraptionDice(dice_18)
dice_31 = ContraptionDice(dice_30)
dice_37 = ContraptionDice(dice_36)
dice_41 = ContraptionDice(dice_40)
dice_61 = ContraptionDice(dice_60)
dice_73 = ContraptionDice(dice_72)
dice_97 = ContraptionDice(dice_96)

# we combine a few more and then make more contraption dice
dice_14 = CompositeDice(dice_7, dice_2)
dice_21 = CompositeDice(dice_7, dice_3)
dice_28 = CompositeDice(dice_7, dice_4)
dice_35 = CompositeDice(dice_7, dice_5)
dice_42 = CompositeDice(dice_7, dice_6)
dice_49 = CompositeDice(dice_7, dice_7)
dice_56 = CompositeDice(dice_7, dice_8)
dice_63 = CompositeDice(dice_7, dice_9)
dice_70 = CompositeDice(dice_7, dice_10)
dice_84 = CompositeDice(dice_7, dice_12)
dice_98 = CompositeDice(dice_7, dice_14)
dice_22 = CompositeDice(dice_11, dice_2)
dice_33 = CompositeDice(dice_11, dice_3)
dice_44 = CompositeDice(dice_11, dice_4)
dice_55 = CompositeDice(dice_11, dice_5)
dice_66 = CompositeDice(dice_11, dice_6)
dice_77 = CompositeDice(dice_11, dice_7)
dice_88 = CompositeDice(dice_11, dice_8)
dice_99 = CompositeDice(dice_11, dice_9)
dice_26 = CompositeDice(dice_13, dice_2)
dice_39 = CompositeDice(dice_13, dice_3)
dice_52 = CompositeDice(dice_13, dice_4)
dice_65 = CompositeDice(dice_13, dice_5)
dice_78 = CompositeDice(dice_13, dice_6)
dice_91 = CompositeDice(dice_13, dice_7)
dice_34 = CompositeDice(dice_17, dice_2)
dice_51 = CompositeDice(dice_17, dice_3)
dice_68 = CompositeDice(dice_17, dice_4)
dice_85 = CompositeDice(dice_17, dice_5)
dice_38 = CompositeDice(dice_19, dice_2)
dice_57 = CompositeDice(dice_19, dice_3)
dice_76 = CompositeDice(dice_19, dice_4)
dice_95 = CompositeDice(dice_19, dice_5)
dice_62 = CompositeDice(dice_31, dice_2)
dice_93 = CompositeDice(dice_31, dice_3)
dice_74 = CompositeDice(dice_37, dice_2)
dice_82 = CompositeDice(dice_41, dice_2)

# rinse and repeat
dice_23 = ContraptionDice(dice_22)
dice_29 = ContraptionDice(dice_28)
dice_43 = ContraptionDice(dice_42)
dice_53 = ContraptionDice(dice_52)
dice_67 = ContraptionDice(dice_66)
dice_71 = ContraptionDice(dice_70)
dice_79 = ContraptionDice(dice_78)
dice_83 = ContraptionDice(dice_82)
dice_89 = ContraptionDice(dice_88)

dice_46 = CompositeDice(dice_23, dice_2)
dice_69 = CompositeDice(dice_23, dice_3)
dice_92 = CompositeDice(dice_23, dice_4)
dice_58 = CompositeDice(dice_29, dice_2)
dice_87 = CompositeDice(dice_29, dice_3)
dice_86 = CompositeDice(dice_43, dice_2)

dice_47 = ContraptionDice(dice_46)
dice_59 = ContraptionDice(dice_58)

dice_94 = CompositeDice(dice_47, dice_2)

all_dices: list[Dice] = [
    Dice(0), # placeholder for index 0
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
