# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:

import sqlite3


def get_connection():
    connection = sqlite3.connect('teachers.db')
    return connection


def get_student_school(Student_Id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "SELECT * FROM Students JOIN School ON School.School_Id = Students.School_Id WHERE Student_Id = ?"
        cursor.execute(query,(Student_Id,))
        records = cursor.fetchall()
        print('Данные по студенту:', )
        for row in records:
            print ("ID Студента:", row[0])
            print ("Имя студента:", row[1])
            print ("ID школы:", row[2])
            print ("Название школы:", row[4])
    except (Exception, sqlite3.Error) as error:
        print('Ошибка в получении данных ', error)


get_student_school(201)


def close_connection(connection):
    if connection:
        connection.close()
