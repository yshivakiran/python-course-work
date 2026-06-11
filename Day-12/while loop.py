#while loop
'''
int
while condition:
    update
    #stat
   

i=1
while(i<11):
    print(i)
    i+=1
 
i=2
while i<21:
    print(i)
    i+=2

i=10
while(i>0):
    print(i)
    i-=1

i=5
while (i<51):
    print(i)
    i+=5

#list
l=[1,2,4,5,6,7,3,9]
i=0
while (i<len(l)):
    print(l[i])
    i+=1
    
#string
l='python programming'
i=0
while (i<len(l)):
    print(l[i])
    i+=1

#tuple
l=(1,2,4,5,6,7,3,9)
i=0
while (i<len(l)):
    print(l[i])
    i+=1
    
#simple code

l=[1,0,0,0,0,0,2,3,0,0,4,0,5,9,0]
while(0 in l):
    l.remove(0)
print(l)

moves= 30
name='shiva'
while moves>1:
    n=input("enter the name: ")
    if name==n:
        print("you guess correct")
        break
    moves-=1
    print(f'{moves} moves are left')
else:
    print("game is over")
    
moves= 30
while moves>1:
    n=input("[w]in or [c]ontinue: ")
    if n=='w':
        print("you won the game")
        break
    moves-=1
    print(f'{moves} moves are left')
else:
    print("game is over")
    '''
bullets=6
while bullets>1:

    bullets-=1
    print(f'{bullets} bullets are left')
else:
    print("bullets are completed")
    
    
    

