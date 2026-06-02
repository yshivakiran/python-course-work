Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
type(a)
<class 'int'>
t=999.99
type(t)
<class 'float'>
c=12+8j
type(c)
<class 'complex'>
s='python'
type(s)
<class 'str'>
>>> s="dedf"
>>> type(s)
<class 'str'>
>>> l=[1,2,3,4]
>>> id(l)
2467837214144
>>> 
>>> type(l)
<class 'list'>
>>> 
>>> t=()
>>> type(t)
<class 'tuple'>
>>> t=(1,2,3,4,5)
>>> t
(1, 2, 3, 4, 5)
>>> type(t)
<class 'tuple'>
>>> #mapping
>>> #set
>>> s={1,2,3,4}
>>> s
{1, 2, 3, 4}
>>> type(s)
<class 'set'>
>>> s=set()
>>> #dict
>>> d=('name':'shiva','age':22,'course':'pfs'}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
>>> d={'name':'shiva','age':22,'course':'pfs'}
>>> type(d)
<class 'dict'>
>>> status= True
>>> type(status)
<class 'bool'>
>>> a=None
>>> type(a)
<class 'NoneType'>
