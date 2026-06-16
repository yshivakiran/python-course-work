#recursive
'''
def func():
    if basecondi:
        return
    func()
'''
'''
def func(num):
    if num == 0:
        return
    print(num,end=' ')
    func(num-1)
func(5)
'''
'''
def func(num):
    if num == 0:
        return
    func(num-1)
    print(num,end=' ')
func(5) #1 2 3 4 5 
'''
#sum of digits
'''
def sumofdigit(n):
    if n==0:
        return 0
    return n+sumofdigit(n-1)

print(sumofdigit(5))
'''
#product of digits
'''
def productofdigit(n):
    if n==0:
        return 1
    return n*productofdigit(n-1)

print(productofdigit(5))
'''
#power
'''
def power(base,pow):
    if pow==0:
        return 1
    return base*power(base,pow-1)
print(power(2,4))
print(power(3,3))
'''
#reverse of string

def reversofstr(s,ind):
    if ind==0:
        return s[0]
    return(s[ind]+reversofstr(s,ind-1))
l="python programming"
print(reversofstr(l,len(l)-1))
           

