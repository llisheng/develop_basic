
#终止循环-改变条件
# count=True
# while count:#判断条件，从这里开始往下走
#     print("hello，world")
#     count=False#到这继续往下走
#     print("你好世界！")#走完这里继续回到判断条件，此时判断为false所以不循环了

#打印1~100以内的数字：
'''count=1
while count <100:
    print(count)
    count=count+1
'''

"""count=1
while count :
    print(count)
    count=count+1
    if count==100:
        break
"""
# #打印100以内的偶数
# count=1
# while count <100:
#     if count % 2 == 0:
#         print(count)
#     count=count+1

#打印1+。。100的和
# count=1
# s=0
# while count <101:
#     s=s+count
#     count=count+1
# print(s)

# #终止循环break
# count=1
# while count <100:
#     print(count)
#     count = count + 1
#     if count==10:
#         break

#continue跳过循环（退出本次循环继续下次循环）
while True:#判断条件
    print("你好")
    print("世界")
    continue#下面的代码不执行，回到while True那里继续执行循环体
    print("你好世界！")





