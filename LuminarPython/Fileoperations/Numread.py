f=open("Numbers","r")
list=[]
for num in f:
    # print(num)
    list.append(int(num.rstrip("\n")))
res=sum(list)
print(res)
