# -*- coding:utf-8 -*-
from development.data_type import dict#从datatype里面导入dict到当前模块中
global1="全局变量"
dict.dict1()#调用datatype中的dict文件中的dict1函数


def l1():
    global global1#这里引用全局变量
    global1="全局变量修改"#重新赋值全局变量
    l1=["詹姆斯","库里","浓眉哥"]
    l2="-".join(l1)#join连接list中的元素
    print(l2)
    print(global1)


l1()