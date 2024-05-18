import os
import datetime

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
hw13_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')


def add_week(add_week_str):
    date = datetime.datetime.strptime(add_week_str, '%Y-%m-%d %H:%M:%S.%f')
    new_date = date + datetime.timedelta(days=7)
    return new_date.strftime('%Y-%m-%d %H:%M:%S.%f')


def get_day_of_week(get_day_str):
    date = datetime.datetime.strptime(get_day_str, '%Y-%m-%d %H:%M:%S.%f')
    return date.strftime('%A')


def days_ago(ago_str):
    date = datetime.datetime.strptime(ago_str, '%Y-%m-%d %H:%M:%S.%f')
    days_ago_qty = (datetime.datetime.now() - date).days
    return str(days_ago_qty)


def read_file():
    with open(hw13_file_path, "r") as data_file:
        for line in data_file.readlines():
            yield line


for data_line in read_file():
    with open(hw13_file_path, 'a') as new_file:
        parts = data_line.split(" - ")
        date_str = (parts[0])[3:]
        action = parts[1].strip()

        if 'распечатать эту дату, но на неделю позже' in action:
            data_line = "\nAdd week - " + add_week(date_str)
            new_file.write(data_line)

        if 'какой это будет день недели' in action:
            data_line = "\nDay of week - " + get_day_of_week(date_str)
            new_file.write(data_line)

        if 'сколько дней назад была эта дата' in action:
            data_line = "\nDays ago - " + days_ago(date_str)
            new_file.write(data_line)
