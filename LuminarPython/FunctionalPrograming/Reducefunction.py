str1="English = 78 science = 83 Math = 68 History = 65 Hindi = 90"
str2=str1.split()
res=[int(i) for i in str2 if i.isdigit()]
count=len(res)
sum=0
for j in res:
    sum=sum+j
    average=sum/count
print(sum)
print(average)