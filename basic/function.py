"""方法定义"""
# 1,位置入参，参数必须和定义的时候位置和个数保持一致
def str_form1(name,age):
   return  "我是{}，我今年{}岁了".format(name,age) # 方法调用str_form1("小明",18)
str_form1("小明",18)

#2,默认参数,方法中 声明了默认参数,调用方法时 不传参就是用默认参数

# def str_form2(name='小红',age=18): # 给age设置默认值18
#     return "我是{}，我今年{}岁了".format(name,age)
#
# str_form2(name="小明") # 未传递小明的年龄，则使用方法定义时给定的默认值


#3,关键字入参,使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值

def str_form4(name,age):
    return "我是{}，我今年{}岁了".format(name,age)
str_form4(age=18,name="小明") # 传递参数时，使用关键字来指定参数

'''
不定长参数 (可变参数,魔法参数)不定长参数 分两种情况：
*param（一个星号），将多个参数收集到一个“元组”对象中。
**param（两个星号），将多个参数收集到一个“字典”对象中。
注意: 方法声明不定长参数时,最好**param在倒数第一位,*param在第二位,如果没有**param,那*param最好在倒数第一位
'''
'''强制位置参数 和 强制关键字参数Python3.8 新增了一个函数形参语法 / 用来指明函数形参必须使用指定位置参数，不能使用关键字参数的形式。
/ ：/ 左边的参数必须位置入参,* ： * 右边的参数必须关键字入参'''

'''现有方法如下所示
def f0(name, age):
    XXXX
def f1(name, age=18):
    XXXX
def f2(a, b, /, c, d, *, e, f):
    XXXX
def f3(*args, **kwargs):
    XXXX

调用方法的方式
是否正确: f0(20)-false
调用方法的方式
是否正确: f1(20)-true
调用方法的方式
是否正确: f1(20, 20)-true
调用方法的方式
是否正确: f2(a=20, 20, 20, 10, 1, 1)-false
调用方法的方式
是否正确: f2(20, 20, 20, 10, 1, 1)-false
调用方法的方式
是否正确: f2(20, 20, 20, 10, e=1, f=1)-true
调用方法f3(1, 2, 3, a=4)那么args和kwargs的值是什么
args: (1,2,3)
kwargs: {‘a’:4}
'''

#匿名函数关键字lambda
lam1=lambda x,y:x*y#lambda关键字,x参数1，y参数2;x*y是方法体,lambda（2,3）根据位置传入参数值
print(lam1(2,3))

lam2=lambda a,b,c:a+b-c
print(lam2(2,2,3))




