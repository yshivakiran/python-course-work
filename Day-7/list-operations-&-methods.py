Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

#list operations

l=[]
l=list()

#the above empty list

type(l)
<class 'list'>
l1=[1,2,3,4]
l2=[2,3,3,5]
l1+l2
[1, 2, 3, 4, 2, 3, 3, 5]
l1*3
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
l1*6
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
l2*2
[2, 3, 3, 5, 2, 3, 3, 5]
l1
[1, 2, 3, 4]
l1.index[2]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    l1.index[2]
TypeError: 'builtin_function_or_method' object is not subscriptable
l1[2]
3
l1[4]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    l1[4]
IndexError: list index out of range
l1[3]
4
l1
[1, 2, 3, 4]
l1[:3]
[1, 2, 3]
l1[3:]
[4]
l1[::-1]
[4, 3, 2, 1]
l1
[1, 2, 3, 4]
l1[-1:-4]
[]
l1[-1:-3]
[]
l1[-1:-3:-1]
[4, 3]
l1
[1, 2, 3, 4]
l1[-2:-5:-1]
[3, 2, 1]
l1[-2:0:-1]
[3, 2]
l1
[1, 2, 3, 4]
l1[-2:-1:-1]
[]
l1[-2:1:-1]
[3]
l1
[1, 2, 3, 4]
l1=[10,20,30,40,50]
l1
[10, 20, 30, 40, 50]
40 in l1
True
50 in l1
True
70 not inl1
SyntaxError: invalid syntax
70 not in l1
True

l1[1]
20
id(l1)
2538744956544
l1[1]=70
id(l1)
2538744956544
l1[4]=100
l
[]
l1
[10, 70, 30, 40, 100]
[10, 70, 30, 40, 100]
[10, 70, 30, 40, 100]
l.append(20)
l1.append(20)
l1
[10, 70, 30, 40, 100, 20]
l1.append(20)
l1
[10, 70, 30, 40, 100, 20, 20]
l1.insert(4,50)
l1
[10, 70, 30, 40, 50, 100, 20, 20]
l1.exten([80,90,110])
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    l1.exten([80,90,110])
AttributeError: 'list' object has no attribute 'exten'. Did you mean: 'extend'?
l1.extend([80,90,110])
l1
[10, 70, 30, 40, 50, 100, 20, 20, 80, 90, 110]
l1.pop()
110
l1
[10, 70, 30, 40, 50, 100, 20, 20, 80, 90]
l.pop(3)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    l.pop(3)
IndexError: pop index out of range
l1.pop(3)
40
l1
[10, 70, 30, 50, 100, 20, 20, 80, 90]
l1.remove(70)
l1
[10, 30, 50, 100, 20, 20, 80, 90]
l1.del(2)
SyntaxError: invalid syntax
del l1[2]
l1
[10, 30, 100, 20, 20, 80, 90]
del l1[2]
l1
[10, 30, 20, 20, 80, 90]
l.clear()
l1.clear()
l1
[]

l=[20,30,40,50,60]
l
[20, 30, 40, 50, 60]
l=[2,60,40,30,20]
l
[2, 60, 40, 30, 20]
#temperary sorted
sorted(l)
[2, 20, 30, 40, 60]
l
[2, 60, 40, 30, 20]
#permenent sort
l.sort()
l
[2, 20, 30, 40, 60]
min(l)
2
max(l)
60
l.reverse()
l
[60, 40, 30, 20, 2]
l
[60, 40, 30, 20, 2]
sorted(l,reverse=True)
[60, 40, 30, 20, 2]
l
[60, 40, 30, 20, 2]
sorted(l,reverse=False)
[2, 20, 30, 40, 60]
l
[60, 40, 30, 20, 2]
l.reversed()
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    l.reversed()
AttributeError: 'list' object has no attribute 'reversed'. Did you mean: 'reverse'?
l.reverse()
l
[2, 20, 30, 40, 60]
l
[2, 20, 30, 40, 60]
l.index(30)
2
l.count(20)
1
l.count(2)
1

len(1)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    len(1)
TypeError: object of type 'int' has no len()
>>> s
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> len(l)
5
>>> sum(l)
152
>>> m=l
>>> m
[2, 20, 30, 40, 60]
>>> l
[2, 20, 30, 40, 60]
>>> m.append(80)
>>> m
[2, 20, 30, 40, 60, 80]
>>> l
[2, 20, 30, 40, 60, 80]
>>> n=l.copy()
>>> n
[2, 20, 30, 40, 60, 80]
>>> l
[2, 20, 30, 40, 60, 80]
>>> n.append(90)
>>> n
[2, 20, 30, 40, 60, 80, 90]
>>> l
[2, 20, 30, 40, 60, 80]
>>> any([1,2,3,4,5,6,0,0,0,0])
True
>>> all([1,2,3,4,5,6,0,0,0,0])
False
>>> #any-any one is true value then it's true
>>> #all-in this all should be true then o/p is true
