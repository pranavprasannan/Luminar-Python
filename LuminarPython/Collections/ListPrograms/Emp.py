emp={"eid":1002,"ename":"person","desig":"tester","salary":15000}
print(emp["ename"])
print("company name" in emp)
emp["company name"]="Luminar Technology"
emp["salary"]+=5000
for keys in emp:
 print(keys,":",emp[keys])