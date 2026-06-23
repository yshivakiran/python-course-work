#list comprehension
'''
syntax
l=[val for var in seq]
l=[val for var in seq if condition]
l=[val if condition else val for var in seq ]

'''
'''
res1=[]
for i in range(1,11):
    res1.append(i)

res2=[i for i in range(1,11)]

print(res1)
print(res2)
print("----------------")

res3=[]
for i in range(3,31,3):
    res3.append(i)

res4=[i for i in range(3,31,3)]

print(res3)
print(res4)
print("----------------")


res5=[]
for i in range(2,51,2):
    res5.append(i)

res6=[i for i in range(2,51,2)]

print(res5)
print(res6)
'''
#--------------------------------------------------------------
'''
a="python programming"

l1=[]
for i in a:
    if i in "aeiouAEIOU":
        l1.append(i)
print(l1)

#same using list comprehension

l2=[i for i in a if i in "aeiouAEIOU"]
print(l2)
'''
#-------------------------
'''
a=[1,2,3,4,5,6,7,8,9,10,2,23,4,45,56,67,78,89]

l1=[]
for i in a:
    if i%2==0:
        l1.append(i)
    else:
        l1.append(0)
        
print(l1)

#same using list comprehension

l2=[i if i%2==0 else 0 for i in a]
print(l2)
'''
#====================================
'''
l=[]
for i in range(10):
    l.append(int(input(f"enter the number-{i+1}: ")))
print(l)

#same using list comprehension

l1=[int(input(f"enter the number-{i+1}: ")) for i in range(10)]
print(l1)
'''
#--------------------------------
'''
l=[]
for i in range(3):
    for j in range(1,4):
        l.append(j)
print(l)

l1=[j for i in range(3) for j in range(1,4)]
print(l1)
'''
'''
l=[]
for i in range(3):
    temp=[]
    for j in range(1,4):
        temp.append(j)
    l.append(temp)
print(l)
'''
#step1
'''
l=[]
for i in range(3):
    temp=[j for j in range(1,4)]
    l.append(temp)
print(l)
'''
#step2

l=[[j for j in range(1,4)] for i in range(3)]
print(l)

#=============================================

