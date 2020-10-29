lst=[1,2,3,4,5]
lst.sort()
print(lst)
element=int(input("Enter the element "))
low=0
up=len(lst)-1
while(low<=up):
    data=lst[low]+lst[up]
    if(element==data):
        print("Pairs",lst[low],",",lst[up])
        break
    elif(data>element):
        up=up-1
    else:
        low=low+1