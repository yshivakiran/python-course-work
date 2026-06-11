l=[2,3,5,6,8,10,34,12]
item = int(input("enter the num: "))
for i in range(len(l)):
    if l[i]==item:
        print(item, i)
        break
else:
    print("not found")
    
