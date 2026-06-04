Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#white space & trimming methods for string
s='    hello   world   '
s
'    hello   world   '
s.strip()
'hello   world'
s.lstrip()
'hello   world   '
s.rstrip()
'    hello   world'


#string testing methods(boolean result)

s='strings.py'
s
'strings.py'
s.startswith('str')
True
s.startswith('ste')
False
s.endswith('py')
True
s.endswith('js')
False
'swdfgh'.isalpha()
True
'werty2345'.isalpha()
False
'swdfgh'.isalnum()
True
'werty2345'.isalnum()
True
'werty@#$2345'.isalnum()
False
s.islower()
True
SDerty45.islower()
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    SDerty45.islower()
NameError: name 'SDerty45' is not defined
>>> asdfgh5432.islower()
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    asdfgh5432.islower()
NameError: name 'asdfgh5432' is not defined
>>> asdfgh.islower()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    asdfgh.islower()
NameError: name 'asdfgh' is not defined
>>> 'asdfgh'.islower()
True
>>> 'asdfgh5432'.islower()
True
>>> ESDRRTF.isupper()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    ESDRRTF.isupper()
NameError: name 'ESDRRTF' is not defined
>>> 'ESDRRTF'.isupper()
True
>>> 'ESDRRTF12345'.isupper()
True
>>> 'ESDRRTF@#$%12345'.isupper()
True
>>> '  '.isspace()
True
>>> 'hello       '.isspace()
False
>>> 'Rdfg Yhj Tfffff'.istitle()
True
>>> 'Swdf fv erf'.istitle()
False
>>> 'qqqqwe wsd'.isidentifier()
False
>>> 'qqqqwewsd'.isidentifier()
True
