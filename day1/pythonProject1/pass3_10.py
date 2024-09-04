def convert_score(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    elif 0 <= score < 60:
        return "E"
    else:
        return "data error!"
    # 读取输入分数，并转换为浮点数
score = float(input("请输入百分制成绩: "))
    # 调用函数并输出结果
result = convert_score(score)
print(result)