class Person:
    name=""
    age=0
    gender=""
    weight=0
    def __init__(self,name,age,gender,weight):
        self.name=name
        self.age=age
        self.gender=gender
        self.weight=weight

    def eat(self):
        print("eating")
    def play(self):
        print("playing")
    def jump(self):
        print("jumping")




zs=Person("zhangsan",16,"女",110)
ls=Person("ls",30,"nan",120)



