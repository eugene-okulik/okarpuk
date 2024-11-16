import datetime

my_date = 'Jan 15, 2023 - 12:05:33'

python_date = datetime.datetime.strptime(my_date, '%b %d, %Y - %H:%M:%S')
print(f'Python date and time format: {python_date}')

my_month = python_date.strftime('%B')
print(f'Month: {my_month}')

custom_date = python_date.strftime('%d.%m.%Y, %H:%M')
print(f'Custom date and time format: {custom_date}')

