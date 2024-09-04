# 请补充你的代码
year=int(input())
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("True")
        return
    print("False")
is_leap_year(year)
