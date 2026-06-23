#sys
'''
import sys

print (sys.argv)
print (sys.path)
print(sys.version)

print("before exit")
sys.exit()
print("after exit")
'''
'''
import platform

print(platform.system(),platform.release(),platform.processor())
'''
'''
import math

print(math.pi)
print(math.e)

print(math.sqrt(25))
print(math.pow(2,5))
print("----ceil------")
print(math.ceil(12.3))
print(math.ceil(12.0000001))
print(math.ceil(12.999999))
print(math.ceil(12.8))
print("--------floor-----")
print(math.floor(12.3))
print(math.floor(12.0000001))
print(math.floor(12.999999))
print(math.floor(12.8))
print("----round-------")
print(round(12.3))
print(round(12.0000001))
print(round(12.999999))
print(round(12.8))
print("-----abs------")#abs(-12)->12,abs(-12.333)->12.333
print(math.fabs(-12))#f->float

print(math.factorial(5))
print(math.gcd(8,28))

print(math.log(10,10))
print(math.sin(10))
print(math.cos(10))
print(math.tan(10))

print(math.degrees(10))
print(math.radians(10))
'''
'''
print("-------random---------")
import random
random.seed(4)# generates the same output

print(random.random())#blw->(0.0,1. )
print(random.randint(1,6))
print(random.uniform(1,6))

l=['pyhon','c','c++','java','html']
print(random.choice(l))
print(random.choices(l,k=3))

s='rps'
print(random.choice(s))
print(l)
random.shuffle(l)
print(l)
'''
'''
print("-----------collections---------")

import collections

s='python programming language'
print(collections.Counter(s))

# same in traditional method

d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

print(d)
'''
#using defaultdict(int)
'''
import collections

s='python programming language'

d= collections.defaultdict(int)

for i in s:
    d[i]+=1
print(d)
'''
#deque
'''
import collections

l=collections.deque([])

l.appendleft(10)
l.appendleft(20)
l.appendleft(30)
l.appendleft(40)
l.pop()
l.pop()
l.pop()
l.appendleft(50)
l.appendleft(60)
l.pop()
print(l)
'''
#combinations,permutations
import itertools

c=(list(itertools.combinations('abcd',2)))
p=(list(itertools.permutations('abcd',2)))

res=[''.join(i) for i in c]
res1=[''.join(j) for j in p]
print(res) #['ab', 'ac', 'ad', 'bc', 'bd', 'cd']
print(res1)#['ab', 'ac', 'ad', 'ba', 'bc', 'bd', 'ca', 'cb', 'cd', 'da', 'db', 'dc']


