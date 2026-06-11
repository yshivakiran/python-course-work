'''
s='looping statements'

for i in s:
    if i in 'aeiouAEIOU':
        print(i)
#to print even number only in list
l=[12,23,34,45,56,67,78,89,90]
for i in l:
    if i%2==0:
        print(i)
'''
d={'laptops':0,'chargers':2,'keyboard':10,'phone':15,'tab':0,'mouse':5}

for i in d:
    if d[i]:
        print(i)
