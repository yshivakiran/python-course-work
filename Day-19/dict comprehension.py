#dict comprehension
'''
d={}
for i in range(1,11):
    d[i]=i*i

print(d)


res={i:i*i for i in range(1,11)}
print(res)
'''
'''
d={}
for i in range(5):
    name=input("enter the name: ")
    marks= int(inpt("enter the marks: "))
    d[name]=marks

print(d)

#step1

d={}
for i in range(5):
    d[input("enter the name: ")]=int(input("enter the marks: "))

print(d)
'''
#step2

res={input("enter the name: "):int(input("enter the marks: ")) for i in range(5)}
print(res)

