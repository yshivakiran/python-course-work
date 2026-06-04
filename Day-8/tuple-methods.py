Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #tuple methods
>>> 
>>> t=(10,20,30,40,50)
>>> t
(10, 20, 30, 40, 50)
>>> len(t)
5
>>> sorted(t)
[10, 20, 30, 40, 50]
>>> min(t)
10
>>> max(t)
50
>>> sum(t)
150
>>> t.count(10)
1
>>> t.index(10)
0
>>> z=1,2,3,4,5
>>> z
(1, 2, 3, 4, 5)
>>> #above is packed
>>> #below is unpacked
>>> a=(1,2,3)
>>> a
(1, 2, 3)
>>> x,y,z=a
>>> x
1
>>> y
2
>>> z
3
>>> t=(1,2,3,[4,5,6],7,8)
>>> t[2]
3
>>> t[4]
7
>>> t[3]
[4, 5, 6]
t[2]
3
t[2]=4
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    t[2]=4
TypeError: 'tuple' object does not support item assignment
t[2].append(10)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    t[2].append(10)
AttributeError: 'int' object has no attribute 'append'
t[3].append(10)
t
(1, 2, 3, [4, 5, 6, 10], 7, 8)
