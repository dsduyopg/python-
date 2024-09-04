def calculate_tax_and_income():
    # 获取用户输入
    salary = eval(input())

    # 检查输入是否合法
    if salary < 0:
        print("error")
        return

    # 计算应纳税所得额
    money = salary - 5000

    # 根据应纳税所得额确定税率和速算扣除数
    if money <= 0:
        rate = 0
        quick_deduction = 0
    elif money < 3000:
        rate = 0.03
        quick_deduction = 0
    elif money < 12000:
        rate = 0.10
        quick_deduction = 210
    elif money < 25000:
        rate = 0.20
        quick_deduction = 1410
    elif money < 35000:
        rate = 0.25
        quick_deduction = 2660
    elif money < 55000:
        rate = 0.30
        quick_deduction = 4410
    elif money < 80000:
        rate = 0.35
        quick_deduction = 7160
    else:
        rate = 0.45
        quick_deduction = 15160

    # 计算应缴税款
    tax = money * rate - quick_deduction
    if tax < 0 or tax==-0:
        tax = 0

    # 计算实发工资
    net_income = salary - tax

    # 输出结果
    print("应缴税款{:.2f}元，实发工资{:.2f}元。".format(tax, net_income))


# 调用函数
calculate_tax_and_income()