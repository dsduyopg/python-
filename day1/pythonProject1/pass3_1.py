# 请补充你的代码
a=int(input())
b=int(input())
c=int(input())
def is_triangle(a,b,c):
    if a+b>c and b+c>a and a+c>b:
        if a ** 2 + b ** 2 == c ** 2 or a**2 + c ** 2 == b**2 or b**2 + c ** 2 == a**2:
            return True
    return False
if(is_triangle(a,b,c)):
    print("YES")
else:
    print("NO")