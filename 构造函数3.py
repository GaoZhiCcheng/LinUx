class A():
    pass
class B():
    def __init__(self,name):
        print("这是b")
        print(name)
class C(B):
    # C中想扩展B的构造函数
    # 即调用b的构造函数后再增加一些功能
    # 有两种方法实现

    '''
    #这是第一种
    def __init__(self, name):
        B.__init__(self,name)
        print("这是C附加的功能")

    '''

    # 这是第二种 super 方法
    def __init__(self,name):
    # 首先调用父类函数
        super(C,self).__init__(name)
    # 其次在增加自已的功能
        print("这是C增加的功能")


# 此时首先查找C的构造函数
#如果没有，则向上按照MRO顺序查找父类的够着函数，直到找到为止。
c = C("我是c")
print(c)
