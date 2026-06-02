Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
name = input()
shiva kiran
name
'shiva kiran'
name=input("enter your name: ")
enter your name: y shiva kiran
name
'y shiva kiran'
age=int(input("enter your age: "))
enter your age: 22
gpa =float(input("enter your gpa: "))
enter your gpa: 7.8
gpa
7.8
type(gpa)
<class 'float'>
'shiva kiran sunny rahul'
'shiva kiran sunny rahul'
'shiva kiran sunny rahul'.split()
['shiva', 'kiran', 'sunny', 'rahul']
'shiva kiran sunny rahul'.split('-')
['shiva kiran sunny rahul']
['shiva kiran sunny rahul'].split(" ")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    ['shiva kiran sunny rahul'].split(" ")
AttributeError: 'list' object has no attribute 'split'
names= input("enter the names: ").split()
enter the names: shiva ramu raghu
names
['shiva', 'ramu', 'raghu']
topics=tuple(input("enter the topics:").split())
enter the topics:token statement variable comments
topics
('token', 'statement', 'variable', 'comments')
op=set(input("enter the oper: ").split())
enter the oper: in not in is is not and or not
op
{'in', 'not', 'is', 'and', 'or'}
marks=input("enter the marks: ").split()
enter the marks: 34 54 56 43
marks
['34', '54', '56', '43']
list(map(int,input("enter the prices: ").split()))
enter the prices: 42525
[42525]
list(map(int,input("enter the prices: ").split()))
enter the prices: 5345 353435 53435 6535
[5345, 353435, 53435, 6535]
tuple(map(int,input("enter the prices: ").split()))
enter the prices: 653553
(653553,)
tuple(map(int,input("enter the prices: ").split()))
enter the prices: 443 4344 25 762 
(443, 4344, 25, 762)
set(map(int,input("enter the prices: ").split()))
enter the prices: 4 3 4 3 4 3
{3, 4}
per =list(map(float,input("enter the per's: ").split()))
enter the per's: 43.4 45.4 543.5 
per
[43.4, 45.4, 543.5]
per =tuple(map(float,input("enter the per's: ").split()))
enter the per's: 34 33 44 22 55 
per
(34.0, 33.0, 44.0, 22.0, 55.0)
per =set(map(float,input("enter the per's: ").split()))
enter the per's: 22 546 754 56 765
per
{546.0, 754.0, 22.0, 56.0, 765.0}
marks=int(input("enter the marks: ").split())
enter the marks: 2222222 3333333333 44444444 55555555555 
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    marks=int(input("enter the marks: ").split())
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
a,b=10,20
a,b=(10,20)
a
10
b
20
a,b=[10,20]
a
10
s
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    s
NameError: name 's' is not defined
b
20
username,password= input("enter the username & password: ").split()
enter the username & password: shiva
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    username,password= input("enter the username & password: ").split()
ValueError: not enough values to unpack (expected 2, got 1)
username,password= input("enter the username & password: ").split()
enter the username & password: shiva s@123
username
'shiva'
>>> password
's@123'
>>> a,b,c,d=list(map(int,input("enter the 4 sides: ").split()))
enter the 4 sides:  4 5 6 7
>>> a
4
>>> b
5
>>> c
6
>>> d
7
>>> price,discount=list(map(float,input().split()))
53433
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    price,discount=list(map(float,input().split()))
ValueError: not enough values to unpack (expected 2, got 1)
>>> price,discount=list(map(float,input().split()))
434443 44
>>> price
434443.0
>>> discount
44.0
>>> a=eval(input())
36535
>>> type(a)
<class 'int'>
>>> a=eval(input())
4443.44
>>> type(a)
<class 'float'>
>>> a=eval(input())
[1,2,3,4]
>>> type(a)
<class 'list'>
>>> a=eval(input())
(1,2,3,4,5)
>>> type(a)
<class 'tuple'>
>>> a=eval(input())
{1,2,3,4,5,6}
type(a)
<class 'set'>
a=eval(input())
{'name':'shiva','age':22,'coruse':'pfs'}
a
{'name': 'shiva', 'age': 22, 'coruse': 'pfs'}
type(a)
<class 'dict'>
