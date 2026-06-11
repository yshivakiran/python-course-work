password='shiva@123'


for i in range(5):
    n=input("enter the password: ")
    if n==password:
       print("password is correct")
       break
    else:
        print("password is incorrect try again")
else:
    print("try sometime, after 60 seconds")


