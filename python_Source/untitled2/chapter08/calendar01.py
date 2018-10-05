import calendar

cal = calendar.Calendar(calendar.SUNDAY)
print(cal)
cal_data = cal.yeardays2calendar(2018, 9)
print('len(cal_data)    :', len(cal_data))

top_months = cal_data[0]
print('len(top_months)  :', len(top_months))

first_month = top_months[0]
print('len(first_month)   :', len(first_month))

print('first_month:')
print(first_month)

print(":", calendar.monthcalendar(2018,9))

print(calendar.calendar(2018))