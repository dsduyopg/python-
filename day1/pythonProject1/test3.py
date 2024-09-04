import math

a = float(input())
b = float(input())
c= float(input())
x=(-b+math.sqrt(b**2-4*a*c))/(2*a)
print("{:.2f}".format(x))