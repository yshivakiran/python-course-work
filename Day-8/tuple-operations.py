Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#tuple operations

t=(1,2,3,4,5)
t
(1, 2, 3, 4, 5)
t=()
t
()
>>> t=(1,1,1,1,1)
>>> t
(1, 1, 1, 1, 1)
>>> t=(1,1,1.1,'try',[])
>>> t
(1, 1, 1.1, 'try', [])
>>> t=(1,2,3)
>>> t1=(2,3,4,2,2,3)
>>> t+t1
(1, 2, 3, 2, 3, 4, 2, 2, 3)
>>> t*3
(1, 2, 3, 1, 2, 3, 1, 2, 3)
>>> t
(1, 2, 3)
>>> t(1)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    t(1)
TypeError: 'tuple' object is not callable
>>> t[1]
2
>>> t[2]
3
>>> t[:2]
(1, 2)
>>> t[2:]
(3,)
>>> t[1:]
(2, 3)
>>> t[::-1]
(3, 2, 1)
>>> t[::2]
(1, 3)
>>> 1 in t
True
>>> 2 in t
True
>>> 6 not in t
True
>>> 4 in t
False
