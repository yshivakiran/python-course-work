#password is strong or not
'''
password=shiva123 ->set(l,l,l,l,l,d,d,d) ->{l,d}
password=shiva@123 ->set(l,l,l,l,l,s,d,d,d) ->{l,s,d}
password=Shiva@123 ->set(u,l,l,l,l,s,d,d,d) ->{u,l,s,d}
'''

password = input("enter the password: ")
if len(password)>=8:
    s=set()
    for i in password:
        if i.isupper():
            s.add("u")
        elif i.islower():
            s.add("l")
        elif i.isdigit():
            s.add("d")
        else:
            s.add("s")
            
    if len(s)==4:
        print("strong password")
    else:
        print("weak password")
else:
    print("weak password")
    
