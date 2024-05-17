import os
import datetime

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
hw13_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')

print(hw13_file_path)

with open(hw13_file_path) as basic_file:
    basic_file.read()

def read_file():
    with open(hw13_file_path, 'r') as data_file:
        # print(data_file)
        for line in data_file.readlines():
            yield line


for data_line in read_file():
    with open(hw13_file_path, 'a') as new_file:
        data_line = data_line.split(" - ")[0]

        if data_line.startswith("1"):
            data_line = data_line.replace('1. ', '')

            python_data_line = datetime.datetime.strptime(data_line, '%Y-%m-%d %H:%M:%S.%f')

            new_data_line = python_data_line + datetime.timedelta(weeks=1)


        new_file.write(data_line)



        # parts_2 = parts_1[0]
        # print(f'parts_1 {parts_1}')
        # print(f'parts_2 {parts_2}')








# def print_date_week_later(date_str):
#     date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")
#     new_date = date + datetime.timedelta(weeks=1)
#     print(new_date)


