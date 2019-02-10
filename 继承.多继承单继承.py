# 多继承案例
class Fish():
    def __int__(self,name):
        self.name = name
        return None
    def swin(self):
        print("i am swimming.........")
        return "YU"
class Bird():
    def __init__(self,name):
        self.name = name
        return None
    def fly(self):
        print("i am flying.....")
        return "NIAO"
class   Person():   
    def __init__(self,name):
        self.naem = name
        return None

    def work(self):
        print("working...........")
        return None
class juzhen():
    def juxing(self):
        for i in range(6):
            for j in range(7):
                print("zheshishenm  asfa"
                      "",end = "")
            print()
class SuperMan(Person,Bird,Fish,juzhen):
    def __init__(self, name):
        self.name = name
        return None

i = SuperMan("wuxxiomei")
print(i.swin())
print(i.fly())
print(i.juxing())