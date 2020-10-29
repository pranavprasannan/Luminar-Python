pattern="ABABCABCDABAAADC"
dict={}
for char in pattern:
 print(char)
 if(char not in dict):
  dict[char]=1
 else:
  dict[char]+=1
print(dict)
