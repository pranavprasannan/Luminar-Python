lst=[10,11,12,13,14,15,2,3,4,5]
lst.sort()
print(lst)
low=0
up=len(lst)-1
element=int(input("Enter the element to be searched "))
flg=0
while(low<=up):
    mid=(up+low)//2
    if(element>lst[mid]):
        low=mid+1
    elif(element<lst[mid]):
        up=mid-1
    elif(element==lst[mid]):
        flg+=1
        break
if(flg>0):
    print("Element found")
else:
    print("Not found")


