#逻辑运算符and，or，not
#x and y布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。
#x or y布尔"或" - 如果 x 是非 0，它返回 x 的值，否则它返回 y 的计算值。
#not x布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。
i=2 and 1
print(i)

'''
代码: a = 5%2 那么a的值是多少?
1
python中判断相等 和 不相等的符号分别是什么?
== & !=
现有代码如下
n1 = 5
n2 = 10
b = n1>=5
c = n1<5 or n2 >8
d = n1>3 and n2 >8
e = n1>3 and n2 >8 and n2>10
f = not n1>=5
求 b,c,d,e,f的值 分别是什么
True True True False False
print( b,c,d,e,f)


'''
n1 = 5
n2 = 10
b = n1>=5
c = n1<5 or n2 >8
d = n1>3 and n2 >8
e = n1>3 and n2 >8 and n2>10
f = not n1>=5
print( b,c,d,e,f)



def operator_demo1(a, b):#带参数函数
    print('加法:', a + b)
    print('减法:', a - b)
    print('乘法:', a * b)
    print('除法:', a / b)
    print('取余:', a % b)
    print('乘方:', a ** b)
    print('取商:', a // b)

if __name__ == '__main__':
    operator_demo1(10,20)


