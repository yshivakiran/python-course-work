'''
enter the number: 9
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*

n=int (input("enter the number: "))
m=n//2
for i in range(n):
    if i<=m:
        for j in range(i+1):
            print('*', end=' ')
    else:           
        for j in range(n-i):
            print('*', end=' ')
    print()
'''
'''
n=int (input("enter the number: "))
m=n//2
for i in range(n):
    if i<=m:
        print('* '*(i+1), end=' ')
    else:           
        print('* '*(n-i), end=' ')
    print()
'''
'''
enter the number: 9
         *  
       * *  
     * * *  
   * * * *  
 * * * * *  
   * * * *  
     * * *  
       * *  
         *  

n=int (input("enter the number: "))
m=n//2
for i in range(n):
    if i<=m:
        print('  '*(m-i), end=' ')
        print('* '*(i+1), end=' ')
    else:           
        print('  '*(i-m), end=' ')
        print('* '*(n-i),end=' ')
    print()
    '''
  #or shortcut
'''
n=int (input("enter the number: "))
m=n//2
for i in range(n):
    if i<=m:
        print('  '*(m-i)+'* '*(i+1), end=' ')
    else:           
        print('  '*(i-m)+'* '*(n-i), end=' ')
    print()
    '''
'''enter the number: 9
     *  
    * *  
   * * *  
  * * * *  
 * * * * *  
  * * * *  
   * * *  
    * *  
     *  
n=int (input("enter the number: "))
m=n//2
for i in range(n):
    if i<=m:
        print(' '*(m-i), end=' ')
        print('* '*(i+1), end=' ')
    else:           
        print(' '*(i-m), end=' ')
        print('* '*(n-i),end=' ')
    print()
'''

#or shortcut
'''
n=int (input("enter the number: "))
m=n//2
for i in range(n):
    if i<=m:
        print(' '*(m-i)+'* '*(i+1), end=' ')
    else:           
        print(' '*(i-m)+'* '*(n-i), end=' ')
    print()
'''
'''
enter the number: 9
* * * * * * * * * 
*               * 
*               * 
*               * 
*               * 
*               * 
*               * 
*               * 
* * * * * * * * * 
n= int(input("enter the number: "))
for i in range(n):
    for j in range(n):
        if (i==0) or (i==n-1) or j==0 or j==n-1:
           print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    '''
#n should be take odd values only not an even 
'''
enter the number: 9
* * * * * * * * * 
*       *       * 
*       *       * 
*       *       * 
* * * * * * * * * 
*       *       * 
*       *       * 
*       *       * 
* * * * * * * * * 
n= int(input("enter the number: "))
mid=n//2
for i in range(n):
    for j in range(n):
        if (i==0) or (i==n-1) or j==0 or j==n-1 or i==mid or j==mid:
           print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    '''
'''
enter the number: 11
* * * * * * * * * * * 
* *               * * 
*   *           *   * 
*     *       *     * 
*       *   *       * 
*         *         * 
*       *   *       * 
*     *       *     * 
*   *           *   * 
* *               * * 
* * * * * * * * * * * 

n= int(input("enter the number: "))
mid=n//2
for i in range(n):
    for j in range(n):
        if (i==0) or (i==n-1) or j==0 or j==n-1 or j==i or i+j == n-1 :
           print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
n= int(input("enter the number: "))
mid=n//2
for i in range(n):
    for j in range(n):
        if (i==0) or j==0 or j==n-1 or i==mid:
           print('*',end=' ')
        else:
            print(' ',end=' ')
    print()


















       
