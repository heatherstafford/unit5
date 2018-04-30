#Heather Stafford
#4/30/18
#displatDate.py

from datetime import *

today = date.today()
weekday = today.weekday()
month = today.month
year = today.year

days = ['Monday', 'Tuesday', 'Wednesday' , 'Thursday' , 'Friday' , 'Saturday' , 'Sunday']
months = ['January', 'Feburary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

print('The date is ',days[weekday],today, months[month], year)
