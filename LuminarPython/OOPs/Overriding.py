class Parent:
    def phone(self):
        print(" has samsung galaxy A10")
class Child(Parent):
    def phone(self):
        print("has an iphone")
m=Child()
m.phone()