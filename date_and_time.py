from datetime import date, time, datetime

current_date = date.today()
print(current_date)

current_time = datetime.now()
print(current_time)
print("Today is ", current_date.year, current_date.month, current_date.day)
