import math

# 用户输入 a 和 b 的值
a = float(input())
b = float(input())

# 计算公式中的 x 值
x = (-b + math.sqrt(2 * a * math.sin(math.radians(60)) * math.cos(math.radians(60)))) / (2 * a)

# 输出 x 的值，保留两位小数
print("{:.2f}".format(x))
