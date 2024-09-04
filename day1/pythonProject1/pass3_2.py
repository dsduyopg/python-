# 读取三个边长
a = int(input())
b = int(input())
c = int(input())


def is_right_angle_triangle(a, b, c):
    # 确定最长边作为假定的斜边
    sides = sorted([a, b, c])
    a, b, c = sides[0], sides[1], sides[2]

    # 使用勾股定理判断是否为直角三角形
    if a ** 2 + b ** 2 == c ** 2:
        return True
    return False


# 判断并输出结果
if is_right_angle_triangle(a, b, c):
    print("YES")
else:
    print("NO")