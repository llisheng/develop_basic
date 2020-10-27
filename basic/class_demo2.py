# -*- coding:utf-8 -*-
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

if __name__ == '__main__':
    acar=acar("BYD","tang",100)
    acar.stop()
    acar.lub()
    print(acar.__siyou)