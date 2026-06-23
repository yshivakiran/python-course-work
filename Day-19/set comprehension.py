#set comprehension

s=set()
for i in range(1,11):
    s.add(i)

s1 ={i for i in range(1,11)}

print(s,s1)
