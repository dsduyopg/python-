import sys

# 获取输入并转换为整数
a, b = map(int, input().split())

# 检查输入是否合法
if a < 0 and b < 0:
    print("Data Error!")
    sys.exit()
found = False

for x in range(0, a):
    y = a - x
    if 2 * x + 4 * y == b and x + y == a:
        print("有{}只鸡，{}只兔".format(x, y))
        found = True
        break
if not found:
    print("Data Error!")