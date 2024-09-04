
num = int(input('请输入一个数:'))

c = 1
a = 1
b = 1
if num == 0:
    shuChu = 0
elif num == 1:
    shuChu = 1
elif num > 1:
    for i in range(1, num):
        x = i
        y = a + b
        a = b
        b = y
        c += x / y * pow(-1, i)

print('{:.6f}'.format(c))