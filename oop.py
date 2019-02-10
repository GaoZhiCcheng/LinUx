class Llei():
    name = "gao"
    age = 24
    print("我要睡觉了")
    def ju(self):
        name = "asd"
        age = 24
        print(name,age)
        return None
class Zi(Llei):
    pass
idx = Llei()
print(idx.age)
print(idx.name)
print(idx.ju())
js = Zi()
print(js.name)