'''
* * * * * 
*       * 
* * * * * 
*       * 
*       * 
n= int(input("enter the number: "))
mid=n//2
for i in range(n):
    for j in range(n):
        if (i==0) or j==0 or j==n-1 or i==mid:
           print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
'''
* * * * * 
*       * 
* * * * * 
*       * 
* * * * * 
n= int(input("enter the number: "))
mid=n//2
for i in range(n):
    for j in range(n):
        if (i==0) or j==0 or j==n-1 or i==mid or i==n-1:
           print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
'''
* * * * * 
*         
*         
*         
* * * * * 

n= int(input("enter the number: "))
mid=n//2
for i in range(n):
    for j in range(n):
        if (i==0) or j==0 or i==n-1:
           print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
'''
* * * * * 
*       * 
*       * 
*       * 
* * * * * 

n= int(input("enter the number: "))
mid=n//2
for i in range(n):
    for j in range(n):
        if (i==0) or j==0 or i==n-1 or j==n-1:
           print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    '''
'''
* * * * * 
*         
* * * * * 
*         
* * * * * 

n= int(input("enter the number: "))
mid=n//2
for i in range(n):
    for j in range(n):
        if (i==0) or j==0 or i==n-1 or i==mid:
           print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
'''
* * * * * 
*         
* * * * * 
*         
*    
n= int(input("enter the number: "))
mid=n//2
for i in range(n):
    for j in range(n):
        if (i==0) or j==0 or i==mid:
           print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
'''
* * * * * 
*         
*   * * * 
*   *   * 
* * *   * 
n= int(input("enter the number: "))
m=n//2
for i in range(n):

    for j in range(n):
        if (i==0) or j==0 or (i==n-1 and j<=m)or (j==m and i>=m) or (i==m and j>=m) or (j==n-1 and i>=m):
           print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    '''
'''
*       * 
*       * 
* * * * * 
*       * 
*       * 
n= int(input("enter the number: "))
m=n//2
for i in range(n):
    for j in range(n):
        if (j==0) or j==n-1 or i==m:
           print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
'''
* * * * * 
    *     
    *     
    *     
* * * * * 
n= int(input("enter the number: "))
m=n//2
for i in range(n):
    for j in range(n):
        if (i==0) or i==n-1 or j==m:
           print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    '''
'''
* * * * * 
    *     
    *     
    *     
* * *     

n= int(input("enter the number: "))
m=n//2
for i in range(n):
    for j in range(n):
        if (i==0) or i==n-1 and j<=m or j==m:
           print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    '''
'''
enter the number: 5
*       * 
*     *   
* * *     
*     *   
*       * 

n= int(input("enter the number: "))
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or i==m and j<=m or j==i and i>=m or i+j==n-1 and j>=m:
           print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    '''
'''
*         
*         
*         
*         
* * * * * 

n= int(input("enter the number: "))
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or i==n-1:
           print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    '''
n= int(input("enter the number: "))
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==j and i<=m:
           print('*',end=' ')
        else:
            print(' ',end=' ')
    print()


