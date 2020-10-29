class Person:
    def __init__(self,id,name,desig,sal):
        self.id=id
        self.name=name
        self.desig=desig
        self.sal=sal
    def __str__(self):
        return self.name
f=open("Empdetails","r")
emplst=[]

for data in f:
    values=data.rstrip("\n").split(",")
    id=values[0]
    name=values[1]
    desig=values[2]
    sal=values[3]
    obj=Person(id,name,desig,sal)
    emplst.append(obj)

for emp in emplst:
    print(emp)