# -*- coding:utf-8 -*-
from functools import partial
#偏函数,要求为f1写一个偏函数，固定传入参数c为10
def f1(a,b,c):
    return a+b-c


if __name__ == '__main__':


    f2=partial(f1,10)
    print(f2(10,5))

