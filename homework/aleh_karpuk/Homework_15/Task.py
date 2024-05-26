import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

# 1.Создайте студента (student)

cursor.execute("INSERT INTO students (name, second_name) VALUES ('Oleg_1', 'Karpuk_1')")
student_id = cursor.lastrowid

# 2. Создайте несколько книг (books) и укажите, что ваш созданный студент взял их

books_create_query = 'INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)'
cursor.executemany(
    books_create_query, [
        ('1984', student_id),
        ('Dune', student_id),
        ('The Martian', student_id)
    ]
)

# 3. Создайте группу (group) и определите своего студента туда

cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES ('SuperGroup_1', 'mar 2024', 'sep 2024')")
group_id = cursor.lastrowid
cursor.execute(f"UPDATE students SET group_id = {group_id} WHERE id = {student_id}")

# 4. Создайте несколько учебных предметов (subjects)

subjects_create_query = 'INSERT INTO subjets (title) VALUES (%s)'
cursor.executemany(
    subjects_create_query, [
        ('Oleg_Sub_1',),
        ('Oleg_Sub_2',),
        ('Oleg_Sub_3',)
    ]
)

sub1_id = cursor.lastrowid
sub2_id = sub1_id + 1
sub3_id = sub1_id + 2

# 5. Создайте по два занятия для каждого предмета (lessons)

lessons_create_query = 'INSERT INTO lessons (title, subject_id) VALUES (%s, %s)'
cursor.executemany(
    lessons_create_query, [
        ('Oleg_Lesson_1_1', sub1_id),
        ('Oleg_Lesson_1_2', sub1_id),
        ('Oleg_Lesson_2_1', sub2_id),
        ('Oleg_Lesson_2_2', sub2_id),
        ('Oleg_Lesson_3_1', sub3_id),
        ('Oleg_Lesson_3_2', sub3_id),

    ]
)

lesson1_1_id = cursor.lastrowid
lesson1_2_id = lesson1_1_id + 1
lesson2_1_id = lesson1_1_id + 2
lesson2_2_id = lesson1_1_id + 3
lesson3_1_id = lesson1_1_id + 4
lesson3_2_id = lesson1_1_id + 5

# 6. Поставьте своему студенту оценки (marks) для всех созданных вами занятий

marks_create_query = 'INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)'
cursor.executemany(
    marks_create_query, [
        ('C', lesson1_1_id, student_id),
        ('A', lesson1_2_id, student_id),
        ('B', lesson2_1_id, student_id),
        ('A', lesson2_2_id, student_id),
        ('B', lesson3_1_id, student_id),
        ('C', lesson3_2_id, student_id)
    ]
)

# Получите информацию из базы данных:
# 1. Все оценки студента

cursor.execute(f'SELECT * from marks where student_id = {student_id}')
marks_info = cursor.fetchall()
print('STUDENT MARKS:')
for i in marks_info:
    print(i)

# 2. Все книги, которые находятся у студента

cursor.execute(f'SELECT * from books where taken_by_student_id = {student_id}')
books_info = cursor.fetchall()
print('STUDENT BOOKS:')
for i in books_info:
    print(i)

# 3. Для вашего студента выведите всё, что о нем есть в базе: группа, книги, оценки с названиями занятий и предметов
# (всё одним запросом с использованием Join)

select_all_info_query = f'''
SELECT students.name as 'Student name', students.second_name as 'Student surname', students.group_id as 'Group ID',
groups.title as 'Group title', groups.start_date as 'Start date', groups.end_date as 'End date',
subjets.title as 'Subject title',
lessons.title as 'Lesson title',
marks.value as 'Mark',
books.title as 'Book title'
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
WHERE student_id = {student_id}
'''
cursor.execute(select_all_info_query)
student_info = cursor.fetchall()
print('ALL INFORMATION ABOUT STUDENT:')
for i in student_info:
    print(i)

db.commit()

db.close()
