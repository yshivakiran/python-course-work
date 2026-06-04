Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#set
s={1,2,3,4}
s
{1, 2, 3, 4}
#empty set
s=set()
s{1,1,1,1,1,1}
SyntaxError: invalid syntax
s={1,1,1,1,1,1}
s
{1}
s=(23,34,45,56,87,09,87,65}
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
ss=(23,34,45,56,87,9,87,65}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
s={23,34,45,56,87,9,87,65}
s
{65, 34, 23, 87, 56, 9, 45}
s=set{}
SyntaxError: invalid syntax
s=set()
s
set()
s.add(1)
s
{1}
s.add(56.567)
s
{56.567, 1}
s.add('kjh')
s
{56.567, 1, 'kjh'}
s.add([1,2,3,4,5])
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    s.add([1,2,3,4,5])
TypeError: cannot use 'list' as a set element (unhashable type: 'list')


#set don't allows the list why becomes set uses map funtion & set don't allow the mutable


s.add((1,2,3,4))
s
{56.567, 1, (1, 2, 3, 4), 'kjh'}
s.add({1,2,34})
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    s.add({1,2,34})
TypeError: cannot use 'set' as a set element (unhashable type: 'set')


#set only uses one opertaion is memebership operation

1
1
s
{56.567, 1, (1, 2, 3, 4), 'kjh'}
1 in s
True
2 in s
False
False not in s
True
s
{56.567, 1, (1, 2, 3, 4), 'kjh'}
a={1,2,3,4,5}
b={5,2,6,7,8,1}
#methods

a | b
{1, 2, 3, 4, 5, 6, 7, 8}
#or
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8}

a.intersection(b)
{1, 2, 5}
#or
a & b
{1, 2, 5}

a -b
{3, 4}

a^b
{3, 4, 6, 7, 8}
a
{1, 2, 3, 4, 5}

#subset is {1}{2}{3}
a<={1}
False
a <={1,2}
False
a<={1,2,3,4,5,6,7}
True
a.disjoint({90,30})
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    a.disjoint({90,30})
AttributeError: 'set' object has no attribute 'disjoint'. Did you mean: 'isdisjoint'?
a.isdisjoint({90,30})
True



a
{1, 2, 3, 4, 5}
a.add{14}
SyntaxError: invalid syntax
a.add(14)
a
{1, 2, 3, 4, 5, 14}
a.update({11,12,13,14})
a
{1, 2, 3, 4, 5, 11, 12, 13, 14}
a.pop()
1
a
{2, 3, 4, 5, 11, 12, 13, 14}
a.remove(2)
a
{3, 4, 5, 11, 12, 13, 14}
a.remove(2)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    a.remove(2)
KeyError: 2
a.discard(2)
a
{3, 4, 5, 11, 12, 13, 14}
a.discard(2)
a
{3, 4, 5, 11, 12, 13, 14}
a.discard(4)
>>> a
{3, 5, 11, 12, 13, 14}
>>> a.clear()
>>> a
set()
>>> 
>>> a
set()
>>> a={1,2,3,4}
>>> b={3,4,22,55,4}
>>> a
{1, 2, 3, 4}
>>> b
{3, 4, 22, 55}
>>> a.intersection(b)
{3, 4}
>>> a
{1, 2, 3, 4}
>>> b
{3, 4, 22, 55}
>>> a.intersection_update(b)
>>> a
{3, 4}
>>> b
{3, 4, 22, 55}
>>> c=b
>>> c.add(12)
>>> c
{3, 4, 12, 22, 55}
>>> b
{3, 4, 12, 22, 55}
>>> d=c.copy()
>>> d
{3, 4, 22, 55, 12}
>>> c
{3, 4, 12, 22, 55}
>>> d.add(34)
>>> d
{34, 3, 4, 22, 55, 12}
>>> c
{3, 4, 12, 22, 55}
