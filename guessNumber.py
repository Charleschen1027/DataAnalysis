# 在教程最开始的几课里，有一个猜数字的游戏：程序随机一个结果，用户通过命令行输入去猜。程序会告诉你猜大了还是小了，直到猜中为止。

# 现在，请你独立实现这个小游戏，并且加上一些功能，比如：

# 游戏可以反复进行，猜中了之后可以重新开始
# 统计用户猜了几轮，平均几次猜中

import random
round = 0 #统计用户猜了几轮
count = 0 #统计用户猜了几次
num = random.randint(1,20)
#程序判断用户是否输入正确
bingo = False
while bingo == False:
    inputNum = int(input("猜猜看正确数字是多少？\n"))
    count += 1
    if inputNum < num:
        print("太小啦！")
    elif inputNum > num:
        print("太大啦！")
    else:
        print("BINGO!")
        round += 1
        if int(input("是否继续游戏？1继续，0退出\n")) == 0:
            bingo = True

#统计
print(f"你一共猜了{round}轮,平均{count//round}次猜中~")
       