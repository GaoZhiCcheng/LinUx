#构造函数的调用顺序
# 如果子类没有写构造函数，则自动向上查找，直到找到位置
class A():
    pass
class B():
    def __init__(self):
        print("B")
class C(B):
    pass
# 此时首先查找C的构造函数
#如果没有，则向上按照MRO顺序查找父类的够着函数，直到找到为止。

c = C()
print(c)
