import math
def calculate_min_pizzas(m, n):
    # 计算大披萨和小披萨的有效直径
    big_diameter = int(m * 2.54)
    small_diameter = int(n * 2.54)

    # 计算大披萨和小披萨的半径
    big_radius = big_diameter / 2
    small_radius = small_diameter / 2

    # 计算大披萨和小披萨的面积
    big_area = math.pi * big_radius ** 2
    small_area = math.pi * small_radius ** 2

    # 计算至少需要多少个小披萨
    num_small_pizzas = math.ceil(big_area / small_area)

    return num_small_pizzas


# 输入部分
m = int(input())
n = int(input())

# 计算并输出结果
result = calculate_min_pizzas(m, n)
print(result)