# -*- coding:utf-8 -*-
'''联系课件中的代码

创建一个Car类,有三个属性name,no,speed, 编写三个方法:
show()：输出每一个属性的值
start(): 启动，speed=100，输出车名，启动了
run(): 行驶，输出车名和当前速度
stop(): 刹车，speed=0，输出车名，刹车当前速度

创建一个car对象,依次 调用show(),start(),run(),stop()方法'''
class Car():
    def __init__(self, name, no, speed):
        self.name = name
        self.no = no
        self.speed = speed
    def show(self):
        print("车名：%s" %(self.name))
        print("车型：{}".format(self.no))
        print(f"车速：{self.speed}")

    def start(self):

        print(self.name+self.no+"启动了")

    def run(self):
        print(self.name+self.no+"当前的车速是%s" %(self.speed))
    def stop(self):
        self.speed=0
        print(self.name+self.no+"刹车当前速度为%s" %(self.speed))



class acar():#包含私有方法和私有属性
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

    def __maintenance(self):  #
        print(self.name + "已更换机油和空气滤芯")

    def lub(self):
        __siyou = "私有属性"
        print(self.name + "油加满了")
        print(__siyou)


car = Car('大众', '迈腾330', '300')

if __name__ == '__main__':
    acar = acar('大众', '迈腾330', '300')
    car.show()
    car.start()
    car.run()
    car.stop()
    acar.lub()

    acar.__maintenance()
    print(acar.__no)