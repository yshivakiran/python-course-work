#In range str,list,tuple is allowed for index for the for loops
#enumerate also used for print the index & value
# in enumerate 0-index are index  & 1-index are char value
'''
s='looping statements'

for i in range(len(s)):
    print(i,s[i])

l=[2,3,4,5,6,7]
for i in range(len(l)):
    print(i,l[i])

l=(2,3,4,5,6,7)
for i in range(len(l)):
    print(i,l[i])
   
s='looping statements'
for i in enumerate(s):
    print(i)# default in print in tuple
# in enumerate 0-index are index  & 1-index are char value
 
s='looping statements'
for i in enumerate(s):
    print(i[0],i[1])
    
l=[2,3,4,5,6,7]
for i in enumerate(l):
    print(i[0],i[1])

l=(2,3,4,5,6,7)
for i in enumerate(l):
    print(i[0],i[1])
'''
l={2,3,4,5,6,7}
for i in enumerate(l):
    print(i[0],i[1])
