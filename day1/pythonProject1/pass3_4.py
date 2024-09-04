# 请补充你的代码
import math

a=eval(input())
b=eval(input())
c=eval(input())
def is_triangle(a,b,c):
    if a+b>c and b+c>a and a+c>b:
        return True
    return False
s=(a+b+c)/2
if(is_triangle(a,b,c)):
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("YES\n{:.2f}".format(area))
else:
    print("NO")