import math
def calculate_min_pizzas(m, n):
    big_diameter = int(m * 2.54)
    small_diameter = int(n * 2.54)
    big_radius = big_diameter / 2
    small_radius = small_diameter / 2
    big_area = math.pi * big_radius ** 2
    small_area = math.pi * small_radius ** 2
    num_small_pizzas = math.ceil(big_area / small_area)
    return num_small_pizzas

m = int(input())
n = int(input())
result = calculate_min_pizzas(m, n)
print(result)