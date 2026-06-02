Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

#arthimatic
a=20
b=20
a+b
40
a=20
b=10
a+b
30
a-b
10
a*b
200
a/b
2.0
9/2
4.5
a//b
2
9//2
4
a%b
0
9%2
1
a**2
400

#comparision
a>b
True
a<b
False
a<=b
False
a>=b
True
a==b
False
a!=b
True
#assignment
y=2
y
2
y=y+2
y
4
y=y+6
y
10
y+=10
y
20
y+=20
y
40
y-=20
y
20
y*=2
y
40
y/=2
y
20.0
y//=2
y
10.0
y //=2
y
5.0
y*=10
y
50.0
print(y//=5)
SyntaxError: invalid syntax
print(y //=5)
SyntaxError: invalid syntax
y
50.0
x=10
x/=5
x
2.0
x*10
20.0
x//=2
x
1.0
x*=20
#logical
a=20
b=10
a%20==0
True
a%20==0 and b%=20==0 and a>b
SyntaxError: 'expression' is an illegal expression for augmented assignment
a%20==0 and b%20==0 and a>b
False
a%20==0 or b%20==0 or a>b
True
#membership
a='python'
a
'python'
yina
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    yina
NameError: name 'yina' is not defined
y in a
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    y in a
TypeError: 'in <string>' requires string as left operand, not float
'y'in a
True
'z'in not a
SyntaxError: invalid syntax
'z' not in a
True
l=['shiva',12,'kiran']
l
['shiva', 12, 'kiran']
type(l)
<class 'list'>
12 in l
True
'shiva' in l
True
t=('shiva', 'sunny','ramu','raghu')
shiva in t
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    shiva in t
NameError: name 'shiva' is not defined
'shiva' in t
True
'rahul' not in t
True
s={11,22,33,44,55,66}
11 in s
True
12 in s
False
12 not in s
True
d={'name':'shiva','age':22,'course': 'pfs'}
d
{'name': 'shiva', 'age': 22, 'course': 'pfs'}
type(d)
<class 'dict'>
'shiva' in d
False
name in d
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    name in d
NameError: name 'name' is not defined
'name' in d
True
#dict in only works on "key" only not for value
#dict in only works on "key" only not for value

#identity
l=[1,2,3,4,5]
m=[1,2,3,4,5]
l==m
True
n=m
n
[1, 2, 3, 4, 5]
id(l)
1981643897856
id(m)
1981643703552
id(n)
1981643703552
i is m
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    i is m
NameError: name 'i' is not defined. Did you mean: 'id'?
>>> l is m
False
>>> m is n
True
>>> l is not m
True
>>> m is not n
False
>>> #bitwise
>>> 8 & 7
0
>>> 8 & 14
8
>>> 8 | 7
15
>>> 10^11
1
>>> ~12
-13
>>> ~15
-16
>>> ~-12
11
>>> 8>>2
2
>>> 15>>1
7
>>> 15<<1
30
>>> ~o
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    ~o
NameError: name 'o' is not defined
>>> ~0
-1
>>> ~1
-2
