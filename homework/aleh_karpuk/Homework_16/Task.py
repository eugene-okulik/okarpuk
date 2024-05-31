import os
import csv
import mysql.connector as mysql

# ПЕРЕДЕЛАТЬ НА ПОДКЛЮЧЕНИЕ М ПОМОЩЬЮ DOTENV

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor()



base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
hw16_file_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')



with open(hw16_file_path, newline='') as file:
    file_data = csv.reader(file)
    next(file_data)  # Пропускаем заголовок

    for row in file_data:
        name, second_name, group_title, book_title, subject_title, lesson_title, mark_value = row




        select_all_info_query = f'''
        SELECT students.name, students.second_name, 
        groups.title, 
        subjets.title,
        lessons.title,
        marks.value,
        books.title
        FROM students
        JOIN `groups`
        ON students.group_id = groups.id
        JOIN books
        ON students.id = books.taken_by_student_id
        JOIN marks
        ON students.id = marks.student_id
        JOIN lessons
        ON marks.lesson_id = lessons.id
        JOIN subjets
        ON lessons.subject_id = subjets.id
        WHERE name = %s AND second_name = %s AND groups.title = %s AND books.title = %s
        AND subjets.title = %s AND lessons.title = %s AND marks.value = %s'''
        values = (name, second_name, group_title, book_title, subject_title, lesson_title, mark_value)

        cursor.execute(select_all_info_query, values)
        result = cursor.fetchall()



        if result:
            print(f"{row} - FOUND in database")
        else:
            print(f"{row} - NOT FOUND in database")

db.close()
