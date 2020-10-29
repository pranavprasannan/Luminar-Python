lst=[10,2,3,4,5,6]
sum=0
count=len(lst)
j=1
for i in range(0,count):
    sum=lst[i]**j
    j+=1
    print(sum)
