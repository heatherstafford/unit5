#Heather Stafford
#4/30/18
#displatDate.py

from datetime import *

today = date.today()
weekday = today.weekday()
month = today.month
year = today.year
day = today.day

days = ['Monday', 'Tuesday', 'Wednesday' , 'Thursday' , 'Friday' , 'Saturday' , 'Sunday']
months = ['January', 'Feburary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

print('The date is ',days[weekday], months[month-1], year)
