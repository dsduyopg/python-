# 输入部分
father_length = int(input())
mother_length = int(input())
gender = input().strip()


def is_gender(gender):
    # 判断性别是否为 '男' 或 '女'
    if gender == '男':
        return True
    elif gender == '女':
        return False
    else:
        print("无对应公式")
        return None


def fact_length():
    # 根据性别计算身高
    is_male = is_gender(gender)

    if is_male is None:
        return

    if is_male:
        fact_length = ((father_length + mother_length) * 1.08) / 2
    else:
        fact_length = (father_length * 0.923 + mother_length) / 2

    # 输出计算结果，并取整
    print(int(round(fact_length)))
fact_length()