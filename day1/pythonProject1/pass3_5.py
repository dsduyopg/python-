# 请补充你的代码
father_length=eval(input())
mother_length=eval(input())
gender=input()
def is_gender(gender):
    if gender == '男':
        return True
    else:
        return False
def fact_length():
    if(is_gender(gender)):
        fact_length=((father_length+mother_length)*1.08)/2
    else:
        fact_length=(father_length*0.923+mother_length)/2
print((fact_length()))