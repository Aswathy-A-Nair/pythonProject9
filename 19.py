n=int(input("enter the number"))
print("enter the elements")
list=[]
for i in range(0,n):
    ele=int(input())
    if (ele%2==0):
        list.append(ele)

    print(list)
