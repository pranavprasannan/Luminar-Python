student={"rol":1001,"name":"Viny","age":25,"cpp":25}
for keys in student:
 print(keys,":",student[keys])
student["cpp"]=30
student["total"]=150
print("total" in student)
print(student)
