
number = int(input("请输入一个正整数: "))
i = 1
sum = 0
while i <= number:
    sum += i**2
    i += 1
print("前{}项平方和为: {}".format(number, sum))
