dict={}
str1=input("enter the word")
v=dict.split(',')
print(v)
for n in str1:
    if n in dict:
        dict[n]+=1
    else:
        dict[n]=1
        print(dict)
print("characters")
for m,k in dict.items():
    print(m,k)