low=int(input("Enter the lower limit "))
up=int(input("Enter the upper limit "))
evensum=0
oddsum=0
for i in range (low,up+1):
    if(i%2==0):
        evensum=evensum+i

    else:
        oddsum=oddsum+i
print(evensum)
print(oddsum)
