
'''
n=int(input("enter the size: "))
for row in range(n):
    for col in range(n):
        print(col%2, end=' ')
    print()
    
n=int(input("enter the size: "))
for row in range(n):
    for col in range(row+1):
        print('*', end=' ')
    print()

n=int(input("enter the size: "))
for row in range(n):
    for col in range(n-row):
        print('*', end=' ')
    print()

n=int(input("enter the size: "))
for row in range(n):
    for space in range(n-1-row):
        print(' ', end=' ')
    for j in range(row+1):
        print('*',end=' ')
    print()

n=int(input("enter the size: "))
for row in range(n):
    for space in range(row):
        print(' ', end=' ')
    for j in range(n-row):
        print('*',end=' ')
    print()

n=int(input("enter the size: "))        
for row in range(n):
    for col in range(n):
        print((row+col)%2,end=' ')
    print()
    
n=int(input("enter the size: "))
c=1
for row in range(n):
    for col in range(row+1):
        print(str(c), end=' ')
        c+=1
    print()
    '''

n=int(input("enter the size: "))
c=1
for row in range(n):
    for col in range(row+1):
        print(str(c).zfill(2), end=' ')
        c+=1
    print()
