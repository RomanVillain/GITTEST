import random as r
bones_1_1 = r.randint(1, 6)
bones_2_2 = r.randint(1, 6)
one = print("перший гравець отримав:", bones_1_1, bones_2_2)

bones_1_2 = r.randint(1, 6)
bones_2_3 = r.randint(1, 6)
two = print("перший гравець отримав", bones_1_2, bones_2_3)

one_1 = bones_1_1 + bones_2_2
print(one_1,  "перший гравець")
two_2 = bones_1_2 + bones_2_3
print(two_2, "другий гравець")
if one_1 > two_2:
    print("виграв перший гравець")
elif one_1 < two_2:
    print("виграв другий гравець")
else:
    print("однаково")