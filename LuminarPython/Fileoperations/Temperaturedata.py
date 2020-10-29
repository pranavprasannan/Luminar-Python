f=open("Temperaturedata","r")
dict={}
for lines in f:
    district,temperature=lines.split(",")
    # print(district)
    # print(temperature)
    if(district not in dict):
        dict[district]=temperature
    else:
        old=dict[district]
        if temperature>old:
            dict[district]=temperature
for k,v in dict.items():
    print(k,",",v)