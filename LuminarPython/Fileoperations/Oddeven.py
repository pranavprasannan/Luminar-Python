f=open("Numbers","r")
list=[]
odd=[]
even=[]
for num in f:
    if (int(num)%2==0):
        even.append(int(num))
    else:
        odd.append(int(num))
print(odd)
print(even)