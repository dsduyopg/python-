# 获取用户输入的正整数 n
n = int(input("请输入一个正整数: "))

# 初始化前n项和为0
total_sum =0

# 循环计算前 n 项的和
for i in range(1, n + 1):
    # 根据题目给出的公式，进行求和
    total_sum += (-1) ** (i + 1) * (i / (i + (i - 1)))

# 使用 str.format() 方法保留小数点后6位输出结果
print("{:.6f}".format(total_sum))
