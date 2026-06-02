Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

============================================================ RESTART: C:/Users/HP/Desktop/Python-Course-work/Day-7/report.py ===========================================================

============================================================ RESTART: C:/Users/HP/Desktop/Python-Course-work/Day-7/report.py ===========================================================
bunny
502

Traceback (most recent call last):
  File "C:/Users/HP/Desktop/Python-Course-work/Day-7/report.py", line 3, in <module>
    s1=int(input())
ValueError: invalid literal for int() with base 10: ''
bunny
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    bunny
NameError: name 'bunny' is not defined

============================================================ RESTART: C:/Users/HP/Desktop/Python-Course-work/Day-7/report.py ===========================================================
bunny
502
30

Traceback (most recent call last):
  File "C:/Users/HP/Desktop/Python-Course-work/Day-7/report.py", line 4, in <module>
    s2=int(input())
ValueError: invalid literal for int() with base 10: ''

=========================================================== RESTART: C:/Users/HP/Desktop/Python-Course-work/Day-7/strings.py ===========================================================
bunny
Total characters: 5
First character: b
Last character: y
Uppercae: BUNNY
Reversed String: ynnub

=========================================================== RESTART: C:/Users/HP/Desktop/Python-Course-work/Day-7/students.py ==========================================================
2 3 4
sum: 9
average: 3.0
Product: 24
-----------------------------------------------------------------------------
SyntaxError: invalid syntax
s='Python programming'
len(s)
18
max(s)
'y'
min(s)
' '
sorted(s)
[' ', 'P', 'a', 'g', 'g', 'h', 'i', 'm', 'm', 'n', 'n', 'o', 'o', 'p', 'r', 'r', 't', 'y']
chr(a)
'\x02'
char(y)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    char(y)
NameError: name 'char' is not defined. Did you mean: 'chr'?
chr(y)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    chr(y)
NameError: name 'y' is not defined
ord('A')
65
chr(57)
'9'
s.upper()
'PYTHON PROGRAMMING'
s.lower
<built-in method lower of str object at 0x0000018C0DB574F0>
s.lower()
'python programming'
s.capitalize()
'Python programming'
s.title()
'Python Programming'
s.swapcase()
'pYTHON PROGRAMMING'
s.casefold()
'python programming'
s
'Python programming'
s.center(48,'*')
'***************Python programming***************'
s.ljust(58,'-')
'Python programming----------------------------------------'
s.rjust(68,'*')
'**************************************************Python programming'
'345'.zfill(9)
'000000345'
s
'Python programming'
s.find('o')
4
s.rfind('o')
9
s.find('z')
-1
s.index('o')
4
s.rindex('o')
9
s.index('z')
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    s.index('z')
ValueError: substring not found
s.count('o')4
SyntaxError: invalid syntax
s.count('o')
2
s
'Python programming'
s.repace('python','java')
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    s.repace('python','java')
AttributeError: 'str' object has no attribute 'repace'. Did you mean: 'replace'?
s.replace('python','java')
'Python programming'
s.replace('python','java')
'Python programming'
'Python programming'
'Python programming'

s.maketrans('python','123456')
{112: 49, 121: 50, 116: 51, 104: 52, 111: 53, 110: 54}
translate(s.maketrans('python','123456'))
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    translate(s.maketrans('python','123456'))
NameError: name 'translate' is not defined


s.translate(s.maketrans('python','123456')
S
            
SyntaxError: '(' was never closed
s.translate(s.maketrans('python','123456'))
            
'P23456 1r5grammi6g'
    s='python','java','c','c++'
            
SyntaxError: unexpected indent
s='python','java','c','c++'
            
s
            
('python', 'java', 'c', 'c++')
s.split('-')
            
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    s.split('-')
AttributeError: 'tuple' object has no attribute 'split'
s.split(',')
            
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    s.split(',')
AttributeError: 'tuple' object has no attribute 'split'
s='python,java,c,c++'
            
s
            
'python,java,c,c++'
s.split(',')
            
['python', 'java', 'c', 'c++']
s.rsplit(',',2)
            
['python,java', 'c', 'c++']
s.splitlines()
            
['python,java,c,c++']
s.join('@')
            
'@'
s
            
'python,java,c,c++'



n
nn
            
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    nn
NameError: name 'nn' is not defined












>>> s
...             
'python,java,c,c++'
>>> s='python','java', 'c', 'c++'
...             
>>> s
...             
('python', 'java', 'c', 'c++')
>>> s.join('@')
...             
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    s.join('@')
AttributeError: 'tuple' object has no attribute 'join'
>>> s=['python,java', 'c', 'c++']
...             
>>> s
...             
['python,java', 'c', 'c++']
>>> '@'.join(l)
...             
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    '@'.join(l)
NameError: name 'l' is not defined
>>> '@'.join(s)
...             
'python,java@c@c++'
>>> s
...             
['python,java', 'c', 'c++']
>>> s='python,java,c,c++,js'
...             
>>> s
...             
'python,java,c,c++,js'
>>> s.partition(',')
...             
('python', ',', 'java,c,c++,js')
>>> s.rpartition(',')
...             
('python,java,c,c++', ',', 'js')
>>> s.replace('java','react')
...             
'python,react,c,c++,js'
