class Parent:
    def m1(self):
        print("inside parent")
class Child:
    def m2(self):
        print("inside child")
class Subchild(Child,Parent):
    def m3(self):
        print("inside subchild")

sb=Subchild()
sb.m3()
sb.m1()
sb.m2()


p=Parent()
p.m1()

ch=Child()
ch.m2()
