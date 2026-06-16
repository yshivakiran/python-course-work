#local scope- a varable which declared inside of block or function then it's acces inside only
'''
def display():
    n=10
    print("Inside:",n)
display()
'''
#global scope- Avarable which declared outside of block or function then it's acces inside and outside also
'''
n=10
def display():
   
    print("Inside:",n)
display()
print("outside:",n)
'''
#global keyword
'''
def display():
    global n       #golbal keyword it's use is when varable is declared inside then to acces outside use"global"
    n=10
    print("Inside:",n)
display()
print("outside:",n)
'''
'''
def display(n):
    #global n       
    n+=10
    print("Inside:",n)
n=10    
display(n)
print("outside:",n) #Inside: 20  outside: 10


def display():
    global n       
    n+=10
    print("Inside:",n)
n=10    
display()
print("outside:",n)  #Inside: 20  outside: 20
'''
#nonlocal
'''
def outer():
    n=10
    def inner():
        nonlocal n
        n+=10
        print("inner function: ",n)
    inner()

    print("outer funtion: ",n)
outer()
'''
#without nonlocal
'''
def outer():
    n=10
    def inner(n):
        n+=10
        print("inner function: ",n)
    inner(n)

    print("outer funtion: ",n)
outer()
'''
'''
s='python'
print(len(s))
len=
'''
#pass by value-(int,float,complex,str,tuple,bool)-immutable
# pass by reference-(list,set,dict)-mutable

#int
'''
def update(n):
    n+=10
    print("inside: ",n)
n=10
update(n)
print("outside: ",n)
'''
#float
'''
def update(n):
    n+=10
    print("inside: ",n)
n=10.2
update(n)
print("outside: ",n)
'''
#complex
'''
def update(n):
    n+=10
    print("inside: ",n)
n=2+3j
update(n)
print("outside: ",n)
'''
#str
'''
def update(n):
    n+=('  kiran')
    print("inside: ",n)
n='shiva'
update(n)
print("outside: ",n)
'''
#list
'''
def update(n):
    n.append(6)
    print("inside: ",n)
n=[1,2,3,4,5]
update(n)
print("outside: ",n)
'''
#tuple

def update(n):
    n+=(6,)
    print("inside: ",n)
n=(1,2,3,4,5)
update(n)
print("outside: ",n)


