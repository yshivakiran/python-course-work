#exceptional
#try-checking the error
#except
#
#finally- deafult message
'''
synataxerror is complier
logical mistake is runtim error
value error,name error,type error,key error,index error
'''
#valueerror
'''
try:
    a=int(input("enter the age: "))
    #print(12/0)
    #print(b)
    #print(13+'14')
    d={1:1,2:2,3:3,4:4}
    #print(d[5])
    l=[1,2,3,4]
    #print(l[10])
          
except ValueError:
    print("enter the age in a digit[0-9] format")
except ZeroDivisionError:
    print("cant'n divide with zero")
except NameError:
    print("define the var")
except TypeError:
    print("Add the same datatype")
except KeyError:
    print("key is not present")
except IndexError:
    print("index is out of range")
else:
    print("age: ",a)
finally:
    print("Thankyou")
    '''
# or use this
'''
try:
    #a=int(input("enter the age: "))
    #print(12/0)
    print(b)
    #print(13+'14')
    d={1:1,2:2,3:3,4:4}
    #print(d[5])
    l=[1,2,3,4]
    #print(l[10])
          
except (ValueError,ZeroDivisionError,NameError,TypeError,KeyError,IndexError) as e:
    print("Error Occured:",e)

else:
    print("Error Occured")
finally:
    print("Thankyou")
'''
# or use this
'''
try:
    #a=int(input("enter the age: "))
    #print(12/0)
    print(b)
    #print(13+'14')
    d={1:1,2:2,3:3,4:4}
    #print(d[5])
    l=[1,2,3,4]
    #print(l[10])
          
except Exception as e:
    print("Error Occured:",e)

else:
    print("Error Occured")
finally:
    print("Thankyou")
'''
#raise keyword

try:
    amount = int(input("enter the amount to withdraw: "))
    if amount<0:
        raise Exception("enter the amount greater rhan zero")

except Exception as e:
    print("error occured:",e)
else:
    print("thankyou")
