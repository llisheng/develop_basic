#for循环
# msg="我是一个中国人"
# for i in msg:
#     print(i)

#终止循环break
# msg="我是一个中国人"
# for i in msg:
#     print(i)
#     if i=="一":
#         break

# #跳过循环continue
# msg1 = "我是一个中国人"
# for i in msg1:
#     if i=="一":
#         continue
#     print(i)
#1-50之间的偶数和
# sum=0
# for i in range(1,51):
#     j= i%2
#     if j==0:
#
#         sum+=i
# print(sum)
# #1-100之间的奇数和
# a=1
# for i in range(1,101):
#     k=i%2
#     if k==1:
#         a=a+i
# print(a)

#使用for循环打印出1-100之间能被3和5整除的数字

# for i in range(1,101):
#     if i%3==0 and i %5==0:
#
#         print(i)


#使用for循环打印出1-100之间能被3和5整除的数字，打印四个数就停止
# c=0
# for i in range(1,101) :
#
#     if i%3==0 and i %5==0:
#
#         print(i)
#         c+=1
#         if c ==4:#c是打印的个数
#             break

# #通过for循环去重
# a=[2,1,1,3,3,4,5]
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)
# c=set(a)#去重
# print(c)
#嵌套循环
# for i in range(5):
#     print(f"外循环第{i}次")
#     for j in range(3):
#         print(f"内循环第{j}次")
# list 转 字典 , 索引作为key , 索引对应的值 作为 value
# alist = [3, 2, 1, 5, 4, 4, 5]
# adict={}
# for i in range(len(alist)):
#         v = alist[i]
#         adict[i] = v
# print(adict)


#现有两个列表:
# alist = ['哈', '楼', 4, 5, 1, 2, 3]
# blist = ['哈', '楼', 'wo', 'de', 1, 2, 3]
# '''请使用for循环遍历列表的方式 求出两个列表的 交集(两个列表都包含的元素) 和
# 差集(alist中有的元素blist中没有 和 blist中有的元素alist中没有 的元素)'''
# jiao=[]
# cha=[]
# for i in alist:
#     if i in blist:
#         jiao.append(i)
#
#     else:
#         cha.append(i)
#
# for j in blist:
#     if j not in alist:
#             cha.append(j)
# print(f"这是交集:{jiao}")
# print(f"这是差集:{cha}")
#
# #99乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,"X",i,"=",j*i,end='\t')
#
#     print()
#
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print("%s*%s=%s" %(j,i,j*i),end="  ")
#     print()
#冒泡排序
a=[3,2,1,5,4,9,6,7,8]
len1=len(a)
for i in range(len1):
    for j in range(len1-1):
        if a[j] > a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)

