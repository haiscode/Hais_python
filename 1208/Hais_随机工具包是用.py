import random
player = int(input("请输入（1）石头（2）剪刀（3）布 :"))

computer = random.randint(1,3)

print("玩家选择拳：%d  - 电脑选择拳：%d" %(player ,computer))


if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):
    print("玩家获胜")
else:
    print("电脑获胜")