import arrow
import calendar
a = arrow.now().format('YYYY-MM')
year = int(a[:4])
month = int(a[5:])
print(calendar.month(year,month))