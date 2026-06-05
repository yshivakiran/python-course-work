Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dictionary

#empty dic
d={}
d=dict()
type(d)
<class 'dict'>
#dict-key
d={}
d[1]='int
SyntaxError: unterminated string literal (detected at line 1)
d[1]='int'
d
{1: 'int'}
d[2.34]='float'
d
{1: 'int', 2.34: 'float'}
d[2+3j]='complex'
d
{1: 'int', 2.34: 'float', (2+3j): 'complex'}
d['str']='string'
d
{1: 'int', 2.34: 'float', (2+3j): 'complex', 'str': 'string'}
d[[1,2,3,4]]='list'
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    d[[1,2,3,4]]='list'
TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
d[(1,2,3,4)]='tuple'
d
{1: 'int', 2.34: 'float', (2+3j): 'complex', 'str': 'string', (1, 2, 3, 4): 'tuple'}
d[{1,2,3,4,5}]='set'
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    d[{1,2,3,4,5}]='set'
TypeError: cannot use 'set' as a dict key (unhashable type: 'set')
d[{'s1':1,'s2':2,'s3':3}]='dictionary'
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    d[{'s1':1,'s2':2,'s3':3}]='dictionary'
TypeError: cannot use 'dict' as a dict key (unhashable type: 'dict')
d[False]='bool'
d
{1: 'int', 2.34: 'float', (2+3j): 'complex', 'str': 'string', (1, 2, 3, 4): 'tuple', False: 'bool'}

#dict-key are must be mutable & uniqe

#dict-values

d={}
d[1]=1
d
{1: 1}
d[23]=23.4
d
{1: 1, 23: 23.4}
d[3]='werer'
d
{1: 1, 23: 23.4, 3: 'werer'}
d[4]=3+4j
d
{1: 1, 23: 23.4, 3: 'werer', 4: (3+4j)}
d[5]=[1,2,3,4]
d[6]=(1,2,3,4)
d[7]={1,3}
d[8]={1:1,2:2}
d[9]=False
d
{1: 1, 23: 23.4, 3: 'werer', 4: (3+4j), 5: [1, 2, 3, 4], 6: (1, 2, 3, 4), 7: {1, 3}, 8: {1: 1, 2: 2}, 9: False}
#dict-values are allow all datatypes & duplicate values also

d={}
d[1]=14
d
{1: 14}
d={}
d[1]=2
d[2]=2
d[3]=2
d[4]=2
d
{1: 2, 2: 2, 3: 2, 4: 2}
#dict-values are allow duplicate values

#to acces values

d={1:2,2:4,3:6,4:8,5:10}
d
{1: 2, 2: 4, 3: 6, 4: 8, 5: 10}
d[4]
8
d[5]
10
d[1]
2
d={'shiva':78,'kiran':90,'sunny':78,'ravi':23}
d
{'shiva': 78, 'kiran': 90, 'sunny': 78, 'ravi': 23}
d[sunny]
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    d[sunny]
NameError: name 'sunny' is not defined
d['sunny']
78
d['shiva']
78
d['rahul']
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    d['rahul']
KeyError: 'rahul'
# to error handle the use "get method"
d.get('rahul')
d.get("shiva")
78
d.get('rahul','user not found')
'user not found'
d.get("shiva","user not found")
78

#if value is not in dict then you can use above type
d
{'shiva': 78, 'kiran': 90, 'sunny': 78, 'ravi': 23}
'shiva' in d
True
'ramu' not in d
True


#methods-dict

d.key()
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    d.key()
AttributeError: 'dict' object has no attribute 'key'. Did you mean: 'keys'?
d
{'shiva': 78, 'kiran': 90, 'sunny': 78, 'ravi': 23}
d.keys()
dict_keys(['shiva', 'kiran', 'sunny', 'ravi'])
d.values()
dict_values([78, 90, 78, 23])
d.items()
dict_items([('shiva', 78), ('kiran', 90), ('sunny', 78), ('ravi', 23)])
sorted(d)
['kiran', 'ravi', 'shiva', 'sunny']
min(d)
'kiran'
max(d)
'sunny'
len(d)
4
d['rishi']=23
d
{'shiva': 78, 'kiran': 90, 'sunny': 78, 'ravi': 23, 'rishi': 23}
d.update({'ramu':56,'raghu':87})
d
{'shiva': 78, 'kiran': 90, 'sunny': 78, 'ravi': 23, 'rishi': 23, 'ramu': 56, 'raghu': 87}
d.pop()
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    d.pop()
TypeError: pop expected at least 1 argument, got 0
>>> d.popitem()
('raghu', 87)
>>> d.popitem()
('ramu', 56)
>>> d
{'shiva': 78, 'kiran': 90, 'sunny': 78, 'ravi': 23, 'rishi': 23}
>>> del d['shiva']
>>> d
{'kiran': 90, 'sunny': 78, 'ravi': 23, 'rishi': 23}
>>> d.pop("ravi")
23
>>> d
{'kiran': 90, 'sunny': 78, 'rishi': 23}
>>> del d['shiva']
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    del d['shiva']
KeyError: 'shiva'
>>> d.clear()
>>> d
{}
>>> d={'shiva':78,'kiran':90,'sunny':78,'ravi':23}
>>> d
{'shiva': 78, 'kiran': 90, 'sunny': 78, 'ravi': 23}
>>> d.setdefault(ramu,0)
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    d.setdefault(ramu,0)
NameError: name 'ramu' is not defined
>>> d.setdefault('ramu',0)
0
>>> d
{'shiva': 78, 'kiran': 90, 'sunny': 78, 'ravi': 23, 'ramu': 0}
>>> d.setdefault('shiva',0)
78
>>> d
{'shiva': 78, 'kiran': 90, 'sunny': 78, 'ravi': 23, 'ramu': 0}
>>> d.get('shomu',0)
0
>>> d
{'shiva': 78, 'kiran': 90, 'sunny': 78, 'ravi': 23, 'ramu': 0}
