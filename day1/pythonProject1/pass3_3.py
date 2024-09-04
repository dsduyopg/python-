# 请补充你的代码
year=int(input())
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    return False
if(is_leap_year(year)):
    print(366)
else:
    print(365)