#function syntax
'''
def function_name(arg):
    #stmts
    return
function_name(para)
'''
'''
def wish(name):
    print(f'welcome to the python course {name}')
wish('shiva')
wish('kiran')
wish('sunny')
'''
#even number checking using function
'''
def iseven(num):
    if num%2==0:
        return f"{num} - Even Number"
    else:
        return f"{num} - odd Number"
print(iseven(12))
print(iseven(15))
'''
#factorial

'''
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact
num = int (input("enter the number: "))
print("factorial: ",factorial(num))
'''
#prime number
'''
def isprime(num):
    for i in range(2,num//2):
        if num%i==0:
            return f"{num} - not prime number"
    return f"{num} - prime Number"

num=int(input("enter the number: "))
print(isprime(num))
        '''
#positional- argument

'''
def display(name,email,pwd):
    print("name:",name)
    print("email:",email)
    print("pwd:",pwd)

display('subbu','subbu@gmail.com','subbu@123')
display('subbu@gmail.com','subbu','subbu@123')
display('subbu@123','subbu','subbu@gmail.com')
'''
#keyword-argument
'''
def display(name,email,pwd):
    print("name:",name)
    print("email:",email)
    print("pwd:",pwd)

display(name='subbu',email='subbu@gmail.com',pwd='subbu@123')
display(email='subbu@gmail.com',name='subbu',pwd='subbu@123')
display(pwd='subbu@123',name='subbu',email='subbu@gmail.com')
'''
#default-argument
'''
def display(name,email='',pwd=''): #default value should be at last not at first
    print("name:",name)
    print("email:",email)
    print("pwd:",pwd)

display('subbu','subbu@gmail.com','subbu@123')
display('subbu','subbu@gmail.com')
'''
# varible lenght- argument # output: as tuple
'''
def display(*name):
    print("name:",name)

display('subbu','shiva','sunny','ramu','ravi')
display('subbu','ramu','ravi')
display('sunny','ramu','ravi')
display('subbu')
'''
#keyword - varible lenght- argument # output: as dictionary

def display(**name):
    print("name:",name)

display(k1='subbu',k2='shiva',k3='sunny',k4='ramu',k5='ravi')
display(k1='subbu',k2='ramu',k3='ravi')
display(k1='sunny',k2='ramu',k3='ravi')
display(k1='subbu')
