
#lambda
'''
syntax
var= lambda agr: exp
'''
#add of two numbers using lambda
'''
add= lambda a,b:a+b

print(add(12,13))
print(add(22,33))
'''
#2
'''
wish= lambda name: f"welcome python course {name}"

print(wish("shiva"))
print(wish("sunny"))
'''
#gst
'''
gst=lambda price: price+price*0.18
print(gst(1000))
print(gst(600))
print(gst(89000))
'''
#greatest numbers
'''
greatest= lambda a,b: a if a>b else b

print(greatest(12,34))
print(greatest(12,3))
'''
# checking even or odd number
'''
iseven=lambda a:f'{a} is even number' if a%2==0 else f'{a} is odd number'
print(iseven(12))
print(iseven(15))
print(iseven(11))
'''
#charge
'''
bill=lambda charge:charge if charge>99 else charge+30
print(bill(67))
print(bill(99))
print(bill(120))
'''
#-------------------------------------------------------------------------
# nested if else in lambda
'''
login= True
instock =True

status = lambda login,instock : ("you can buy product" if instock
else "product is out of the stock") if login else "login to buy a product"

print(status(login,instock))
'''
#---------------------------------------------------
#map-update each of the element
'''
l=[1,2,3,4,5,6,7]
res = list(map(lambda i:i**3,l))
print(res)
'''
'''
names=["shiva","kiran","sunny"]
t= list(map(lambda i:i.title(),names))
print(t)
'''
#---------------------------------------------------------------------------
#filter-
'''
l=[1,2,3,4,5,6,7]
res = list(filter(lambda i:i%2==0,l))
print(res)

#map-[False, True, False, True, False, True, False]
#filter-[2, 4, 6]

l=[1,2,3,4,5,6,7]
res = list(filter(lambda i:i>5,l))
print(res)

#map-[False, False, False, False, False, True, True]
#filter=[6, 7]

l=[1,2,3,4,5,6,7]
res = list(filter(lambda i:i%3==0,l))
print(res)

[3, 6]
'''
#-------------------------------------------
#reduce- combin the together

from functools import reduce

l=[1,2,3,4,5,6,7,8,9,10,11,12,13]

s=reduce(lambda sum,i: sum+i,l)
p=reduce(lambda pro,i: pro*i,l)
m=reduce(lambda max,i:max if max>i else i,l)

print(s,p,m)

