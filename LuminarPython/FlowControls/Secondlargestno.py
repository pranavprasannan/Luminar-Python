num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
num3=int(input("Enter the third number"))
if((num3>num1>num2)|(num2>num1>num3)):
    print("2ndlarg= ",num1)
elif((num3>num2>num1)|(num1>num2>num3)):
    print("2ndlarg= ",num2)
else:
    print("2ndlarg= ", num3)