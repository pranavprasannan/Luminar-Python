f=open("covid_19_india.csv","r")
dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    death=data[7]
    state=data[3]
    if state not in dict:
        dict[state]=death
    else:
        dict[state]=death
for k,v in dict.items():
    print(k,"-",v)
    # if (dict[v]>dict[v]+1):
    #     print(k,v)
    # else:
    #     print(k,v)
