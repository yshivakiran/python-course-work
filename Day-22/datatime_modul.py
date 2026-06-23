#modul datatime
from datetime import date,time,datetime,timedelta
'''
t=date.today()

print(t)
print("year:",t.year)
print("month:",t.month)
print("day:",t.day)
print("weekday from 0:",t.weekday())
print("weekday from 1:",t.isoweekday())
'''
#checking date is valid or not
'''
t2=date(2026,12,30)

print(t2)
'''
#checking time is valid or not
'''
t3= time(23,59,0)

print(t3)
'''
#getting current date and time
'''
n=datetime.now()
print(n)
print("year:",n.year)
print("month:",n.month)
print("day:",n.day)
print("hour:",n.hour)
print("minute:",n.minute)
print("second:",n.second)
'''
#strftime
'''
n=datetime.now()

print(n.strftime('%d/%m/%y'))
print(n.strftime('%d/%m/%y %H:%M:%S'))
print(n.strftime('%d/%m/%y %I:%M:%S %p'))
print(n.strftime('%d %b %y %I:%M:%S %p'))
print(n.strftime('%d %B %Y %I:%M:%S %p'))              
print(n.strftime('%a,%d %B %Y %I:%M:%S %p'))
print(n.strftime('%A,%d %B %Y %I:%M:%S %p')) 
'''
n=datetime.now()

n15=n + timedelta(minutes=15)
n2=n + timedelta(hours=2)
n7=n + timedelta(days=60)

print(n15,n2,n7,sep='\n')
