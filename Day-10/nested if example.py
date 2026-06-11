data ={
    'subbu':{'status':True,'python':98,'mysql':95,'flask':94},
    'nagendra':{'status':True,'python':78,'mysql':65,'flask':84},
    'dinesh':{'status':False,'python':None,'mysql':None,'flask':None},
    'naresh':{'status':True,'python':65,'mysql':55,'flask':64},
    'rishi':{'status':True,'python':33,'mysql':25,'flask':34}
    }
name=input("enter the name: ")

if name in data:
    if data[name]['status']:
        total = data[name]['python']+data[name]['mysql']+data[name]['flask']
        avg =total/3
        if avg > 90:
            print(f"congration {name}, you are frist class!!!")
        elif avg>70:
            print(f"good {name}, keep it up for the next time")
        elif avg>35:
            print(f"better {name}, work hard next time!!")
        else:
            print(f"{name},you are failed in the exam. bring your parents")
    else:
        print(f"{name} didn't written the exam. bring your parents")
else:
    print(f"{name}'s data is not found")

    
