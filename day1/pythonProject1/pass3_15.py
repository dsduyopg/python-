for attempt in range(3):
    name = input("请输入用户名: ")
    passwd = input("请输入密码: ")

    if (name == 'admin' or name == 'administrator') and passwd == '012345':
        print("登录成功")
        break
else:
    print("登录失败")