import math

# 获取输入的整数 x
x = int(input())

# 根据条件判断并计算 y 的值
if -6 <= x < 0:
    y = abs(x) + 5
elif 0 <= x < 3:
    y = math.factorial(x)
elif 3 <= x <= 6:
    y = x ** (x - 2)
else:
    y = 0

# 输出 y 的值
print(y)
