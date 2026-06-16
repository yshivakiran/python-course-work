'''
s='python'
for i in range(len(s)):
    for j in range(i+1,len(s)):
        print(s[i],s[j],sep='',end=' ')

l=[[1,2,3],[4,5,6],[7,8,9]]
t=0
for i in l:
    for j in i:
        t+=j
print(t)
        
#using sum

l=[[1,2,3],[4,5,6],[7,8,9]]
t=0
for i in l:
    t+=sum(i)
print(t)

d={
    '1234':{'pin':'4567','balance':2300},
    '2345':{'pin':'3455','balance':2100},
    '3456':{'pin':'4321','balance':2200},
    '4567':{'pin':'7890','balance':2500}

    }
for i in d:
    print('Account nummber: ',i)
    print('pin number: ',d[i]['pin'])

   
n=int(input("enter the size: "))
for row in range(n):
    for col in range(n):
        print('*',end=' ')
    print()
     '''
