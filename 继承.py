class Person():#父类
    name = "gaodaxia"
    age = 24
    __sokr = "我的爱好，游戏"#隐藏的
    _shiyou = "我的小名，gao"#小名是受保护的，子类可以用，但不能公用
    def sleep(self):
        print("我是老师！")
class Teacher(Person):# 调用父类 把父类写进括号就可以调用
    gao_id = "9527"
    name = "sad"
    def make_test(self):
        print("attention")
t = Teacher()
t.name = "saafa"
print(t.name )
print("--分--隔----符--")
print(Teacher.name)
print(t._shiyou)
t.sleep()
print(t.gao_id)
t.make_test()


