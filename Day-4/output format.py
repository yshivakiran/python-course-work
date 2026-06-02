Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=12
>>> b=12.34
>>> c='python'
>>> print("a=",a,'b=',b,'c=',c.sep='',end='@@@@')
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
>>> print("a=",a,'b=',b,'c=',c))
SyntaxError: unmatched ')'
>>> print("a=",a,'b=',b,'c=',c)
a= 12 b= 12.34 c= python
>>> print("a=",a,'b=',b,'c=',c,sep='',end='@@@@')
a=12b=12.34c=python@@@@
>>> print(f'a={a} b={b} c={c})
...       
SyntaxError: unterminated f-string literal (detected at line 1)
>>> print(f'a={a} b={b} c={c}')
...       
a=12 b=12.34 c=python
>>> print('a={} b={} c={}'.format(a,b,c))
...       
a=12 b=12.34 c=python
