# -*- coding:utf-8 -*-
#in如果在指定的序列中找到值返回 True，否则返回 False。
#not in如果在指定的序列中没有找到值返回 True，否则返回 False。
def in_demo():
    alist = ['你好',2,3.4]
    print(2 in alist)
    print(2 not in alist)
    print('你好' in alist)
    print('你好' not in alist)

in_demo()

#is 是判断两个标识符是不是引用自一个对象
#is not 是判断两个标识符是不是引用自不同对象
#id()查看变量的内存地址
def is_demo():
    a = '测试'
    b = '测试,工程师'
    a2 = b.split(',')[1]#通过切片掉“,”将b切成list["测试","工程师"]通过索引取值
    print(id(a))
    print(id(a2))
    print(a is not a2)
    print(a == a2)
    print(a)
    print(a2)
    print(id(a))
is_demo()