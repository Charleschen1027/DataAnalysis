# 示例
# a = 1
# while a != 0:
#     print("please input")
#     a = int(input())
# print("over")
#升级版猜数字
num = 10
print('Guess what I think?')
bingo = False

while bingo == False:
    answer = int(input())

    if answer < num:
        print("Too small!")
    elif answer > num:
        print("Too big!")
    else:
        print("Bingo!")
        bingo = True