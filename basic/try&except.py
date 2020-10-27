# -*- coding:utf-8 -*-
'''练习课件中的代码
有代码如下:
try_demo1(a,b):
    try:
        num = a/b
    except:
        print('除数异常')
    else:
        print('未发生异常')
    finally:
        print('finally分支')
try_demo1(1,2): 控制台输出什么
try_demo1(1,0): 控制台输出什么
'''
# def try_demo1(a,b):
# #     try:#执行代码
# #         num = a/b
# #     except:#发生异常时执行的代码
# #         print('除数异常')
# #     else:#没有发生异常执行的代码
# #         print('未发生异常')
# #     finally:#不管有没有发生异常都执行的代码
# #         print('finally分支')
# # try_demo1(1,2)
# # try_demo1(1,0)

def try_demo():
    try:
        a=int(input("输入除数："))
        b=int(input("输入被除数："))
        c=(a/b)
        print("两个数的商是：",c)
    except ValueError:
        print("程序发生格式错误")
    except ArithmeticError:
        print("发生了算术错误")
    finally:
        print("不管有没有异常都执行的")
try_demo()



