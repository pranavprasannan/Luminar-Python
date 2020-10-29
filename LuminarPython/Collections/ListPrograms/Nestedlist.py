employees=[[1001,"Arun",15000],
           [1002,"Arjun",20000],
           [1003,"Vinu",25000],
           [1004,"Binu",10000]]
sum=0
for employee in employees:
    # if(employee[2]>17000):
    #     print(employee[1])
    #     break
    sum=sum+employee[2]
print(sum)