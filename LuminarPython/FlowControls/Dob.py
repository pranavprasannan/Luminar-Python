dob=int(input("Enter your day of birth "))
mob=int(input("Enter month of birth "))
yob=int(input("Enter year of birth "))
cdob=int(input("Enter current day "))
cmob=int(input("Enter current month "))
cyob=int(input("Enter current year "))

dobb=(yob*10000+mob*100+dob)
cdobb=(cyob*10000+cmob*100+cdob)
cbt=cdobb-dobb
age=cbt//10000
print("Your current age =",age,"Years")