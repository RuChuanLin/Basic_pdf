
#  coding:utf-8
rows = int(input('输入列数： '))
i = j = k = 1
#  声明变量,i用于控制外层循环（图形行数），j用于控制空格的个数，k用于控制*的个数
#  打印菱形
print("打印空心等菱形，这里去掉if-else条件判断就是实心的")
for i in range(rows):
    for j in range(rows - i):
        print(" ", end=" ")
        j += 1
    for k in range(2 * i - 1):
        if k == 0 or k == 2 * i - 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
        k += 1
    print ("\n")
    i += 1
    #  菱形的下半部分
for i in range(rows):
    for j in range(i):
        #  (1,rows-i)
        print(" ", end=" ")
        j += 1
    for k in range(2 * (rows - i) - 1):
        if k == 0 or k == 2 * (rows - i) - 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
        k += 1
    print("\n")
    i += 1

    # ==================================================================

    for i in range(-4, 5, 2):
        print(('*' * (5 - abs(i))).center(5))

    for i in range(5):
        if i < 3:
            print('{}{}'.format(' ' * abs(2 - i), '*' * (1 + 2 * i)))
        else:
            print('{}{}'.format(' ' * abs(2 - i), '*' * (9 - 2 * i)))

    for i in range(-4, 5, 2):
        print(' ' * abs(i // 2) + ('*' * (5 - abs(i))))


    def drawDiamond(x):
        for i in range(-x + 1, x, 2):
            print(('*' * (x - abs(i))).center(x))