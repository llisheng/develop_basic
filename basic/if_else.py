# # 单个if
# print("hello")
# if 2 < 1:  # if只执行if里面的代码块，同级的相当于重新起的
#     print("false")
#
# print("world")


"""
#if else判断
age=input("请输入你的年龄：")
if int(age) >= 18:#这里用int把age的类型转成int
    print("成年人")

else:
    print("未成年人")

"""

# # if elif else判断。。。依次判断并执行
# num = int(input("根据球号码猜球星："))
# if (num) == 23:
#     print("詹姆斯")
# elif num == 30:
#     print("curry")
# elif num == 77:
#     print("Donqiqi")
# else:  # 当以上条件都不满足时执行else
#     print("I,d konw!")




# # 嵌套的if
# username = input("请输入你的用户名：")
# password = input("请输入你的密码：")
# code="ls"
# your_captcha=input("请输入验证码：")
#
# if your_captcha == code:
#    if username == "lisheng" and password == "1110":
#        print("登录成功！")
#    else:
#        print("用户名或者密码错误，请重新输入。")
#
# else:
#    print("验证码错误")


us=input("请输入用户名：")
pw=input("请输入密码：")
code=str(23)#这里要把23转成str，因为下面input只支持str类型输入
y_caputur=input("请输入验证码:")
if y_caputur==code:
    if us == "ls" and  pw=="ls":
        print("登录成功")
    else:
        print("账户或密码错误")

else:
    print("验证码错误")







