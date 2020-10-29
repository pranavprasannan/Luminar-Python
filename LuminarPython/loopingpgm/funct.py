num1=int(input("Enter the first number "))
num2=int(input("Enter the second number "))


def add(num1,num2): #arguement and no return
    sum=num1+num2
    print(sum)
add(num1,num2)



def sub():
    subb=num1-num2  #no arguement and no return
    print(subb)
sub()


def multi(num1,num2): #arguement and return
    mul=num1*num2
    return mul
data=multi(num1,num2)
print(data)
