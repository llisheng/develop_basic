# -*- coding:utf-8 -*-
'''联系课件中的代码

创建一个Car类,有三个属性name,no,speed, 编写三个方法:
show()：输出每一个属性的值
start(): 启动，speed=100，输出车名，启动了
run(): 行驶，输出车名和当前速度
stop(): 刹车，speed=0，输出车名，刹车当前速度

创建一个car对象,依次 调用show(),start(),run(),stop()方法'''
global1="全局变量"
class car():

    def __init__(self,name,no,speed):
        self.name=name
        self.no=no
        self.speed=speed
    def show(self):
        print(f"这是车的名称：{self.name}")
        print("这是车的型号：%s" %(self.no))
        print("车速：{}".format(self.speed))
    def start(self):
        print(self.name+"启动了")

    def run(self):
        print(self.name+self.no+"当前车速是："+self.speed)
    def stop(self):
        self.speed ="0"
        print(self.name+'刹车了,当前车速是'+self.speed)
    def gl(self):
        global global1
        print(global1)

car1=car("大众","迈腾","100")

if __name__ == '__main__':
    car1.show()
    car1.start()
    car1.run()
    car1.stop()
    car1.gl()