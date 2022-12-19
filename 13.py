str1=input("enter first string")
str2=input("enter second string")

a=str2[0]
b=str1[0]
new_str1=a+str1[1:]
new_str2=b+str2[1:]
print(new_str1+' '+new_str2)