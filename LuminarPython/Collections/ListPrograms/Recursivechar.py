pattern="ABBAC"
dict={}

for char in pattern:
    if (char not in dict):
        dict[char]=1
    else:
        print("First Recursive character=",char)
        break


