Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#int
a=123
floot(a)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    floot(a)
NameError: name 'floot' is not defined. Did you mean: 'float'?
float(a)
123.0
srt(a)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    srt(a)
NameError: name 'srt' is not defined. Did you mean: 'set'?
str(a)
'123'
list(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
bool(a)
True
complex(a)
(123+0j)
#float
f=22.1
int(f)
22
complex(f)
(22.1+0j)
str(f)
'22.1'
list(f)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    list(f)
TypeError: 'float' object is not iterable
tuple(f)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    tuple(f)
TypeError: 'float' object is not iterable
set(f)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    set(f)
TypeError: 'float' object is not iterable
dict(f)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    dict(f)
TypeError: 'float' object is not iterable
#complex
c=2+3j
type(c)
<class 'complex'>
int(c)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
str(c)
'(2+3j)'
list(c)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
tuple(c)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
set(c)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
dict(c)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
#string
s='python'
a=123
b=123.45
type(s)
<class 'str'>
a='123'
b='123.45'
int(s)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'python'
int(a)
123
int(b)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    int(b)
ValueError: invalid literal for int() with base 10: '123.45'
float(s)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    float(s)
ValueError: could not convert string to float: 'python'
>>> float(a)
123.0
>>> float(b)
123.45
>>> complex(s)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    complex(s)
ValueError: complex() arg is a malformed string
>>> complex(a)
(123+0j)
>>> complex(b)
(123.45+0j)
>>> str(s)
'python'
>>> str(a)
'123'
>>> '123'str(b)
SyntaxError: invalid syntax
>>> str(b)
'123.45'
>>> list(s)
['p', 'y', 't', 'h', 'o', 'n']
>>> list(a)
['1', '2', '3']
>>> list(b)
['1', '2', '3', '.', '4', '5']
>>> tuple(s)
('p', 'y', 't', 'h', 'o', 'n')
>>> tuple(a)
('1', '2', '3')
>>> tuple(b)
('1', '2', '3', '.', '4', '5')
>>> 
>>> #list
>>> l=[1,2,3,4,5]
>>> type(l)
<class 'list'>
