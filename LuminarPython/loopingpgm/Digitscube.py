num=int(input("Enter the number "))
cube=0
while(num!=0):
    digit=num%10
    digit=digit**3
    cube=cube+digit
    num=num//10
print(cube)
