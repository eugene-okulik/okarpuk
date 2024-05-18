import os
from datetime import datetime, timedelta

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
hw13_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')


def add_week(date_str):
    date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')
    new_date = date + timedelta(days=7)
    return new_date.strftime('%Y-%m-%d %H:%M:%S.%f')


def get_day_of_week(date_str):
    date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')
    return date.strftime('%A')


def days_ago(date_str): date = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')


days_ago = (datetime.datetime.now() - date).days
return str(days_ago)

with open('dates.txt', 'r') as file:
    lines = file.readlines()

updated_lines = []
for line in lines: if
'-' in line: parts = line.split(' - ')
date_str = parts[0]
action = parts[1].strip()

Copy
if 'распечатать эту дату, но на неделю позже' in action:
    new_date_str = add_week(date_str)
    updated_lines.append(new_date_str + ' - ' + action + '\n')

if 'какой это будет день недели' in action:
    day_of_week = get_day_of_week(date_str)
    updated_lines.append(date_str + ' - ' + day_of_week + '\n')

if 'сколько дней назад была эта дата' in action:
    days_ago_str = days_ago(date_str)
    updated_lines.append(date_str + ' - ' + days_ago_str + ' дней назад' + '\n')


