import math
a=float(input())
b=float(input())
c=float(input())
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("周长={:.2f}".format(a+b+c))
print("面积为= {:.2f}".format(area))