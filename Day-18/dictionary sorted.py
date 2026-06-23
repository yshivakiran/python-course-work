#dic sorted
'''
d={'subbu':50,'shiva':40,'vamshi':60,'dinesh':80,'sahith':70}

print(dict(sorted(d.items()))) #frist letter of word
print(dict(sorted(d.items(),key=lambda i:i[1]))) #(sahith, i=sahith , 70 -> i[1]=70

print(dict(sorted(d.items(),reverse= True)))
print(dict(sorted(d.items(),key=lambda i:i[1],reverse=True)))
'''
#dict update 

d={'sugar':40,'salt':20,'cookin oil':80,'chilli':60}

print(d.items()) #output as tuple that'swhy we use "()"
#gst
res = dict(map(lambda i:(i[0],i[1]+i[1]+0.18),d.items()))
#discount
res1 = dict(map(lambda i:(i[0],i[1]-i[1]*0.5),d.items()))

res2 = dict(filter(lambda i:i[1]>50,d.items()))

res3 = dict(filter(lambda i:i[1]<50,d.items()))


print(res)
print(res1)
print(res2)
print(res3)

