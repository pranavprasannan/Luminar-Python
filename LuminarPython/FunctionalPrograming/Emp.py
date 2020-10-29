class Employee:
    def __init__(self,id,name,desig,sal):
        self.id=id
        self.name=name
        self.desig=desig
        self.sal=sal

    def printvalue(self):
        print("Employee id",self.id)
        print("Employee name",self.name)
        print("Employee designation",self.desig)
        print("Employee Salary",self.sal)

    def __str__(self):
        return (self.name)
f=open("Empdetail","r")
lst=[]
for emp in f:
    data=emp.rstrip("\n").split(",")
    id=data[0]
    name=data[1]
    desig=data[2]
    sal=data[3]
    obj=Employee(id,name,desig,sal)
    lst.append(obj)
for ep in lst:
    print(ep)

