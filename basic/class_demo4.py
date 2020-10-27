# -*- coding:utf-8 -*-
class acar():
    def __init__(self, name, no, speed):
        self.name = name
        self.__no = no  # 属性前面加__是私有属性
        self.__speed = speed

    def show(self):
        print("车名：%s" % (self.name))
        print("车型：{}".format(self.__no))
        print(f"车速：{self.__speed}")

    def start(self):
        print(self.name + self.__no + "启动了")

    def run(self):
        print(self.name + self.__no + "当前的车速是%s" % (self.speed))

    def stop(self):
        self.speed = 0
        print(self.name + self.__no + "刹车当前速度为%s" % (self.speed))
    def lub(self):
        print(self.name+"电充满了")

class Tesla(acar):#继承父类acar的方法和属性
    def __init__(self,name, no, speed,color,price):#在父类的属性基础上,加在了子类Tesla上面
        super().__init__(name, no, speed)
        self.color=color
        self.price=price
    def showAll(self):
        self.show()
        print(self.color,self.price)
    def lub(self):
        print(self.name+"电充满了")

if __name__ == '__main__':
    acar=acar("BYD","-A",100)#父类acar的实例化
    acar.show()#调用父类中的show方法
    tesla=Tesla("BYD","-A",100,"red",100)#子类Tesla实例化

    tesla.lub()
    acar.lub()

