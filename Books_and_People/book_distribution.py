import json
import math
import os
from gettext import install
import pep8
import pip
import re

my_cwd = os.getcwd()
name_file_people = "data/people.json"
path_to_people = os.path.join(my_cwd, name_file_people)

# Чтение файла file_people
with open(path_to_people, "r", encoding='utf-8') as file_people:
    content_with_people = json.load(file_people)

my_cwd = os.getcwd()
name_file_books = "data/books.json"
path_to_books = os.path.join(my_cwd, name_file_books)

# Чтение файла file_books
with open(path_to_books, "r", encoding='utf-8') as file_books:
    content_with_books = json.load(file_books)
# Сортировка нужных данных в новую переменную
result_people = []
correct_data = {}
#Инициализация нужных данных
for people in content_with_people:
    correct_data = {
        'name': people['name'],
        'gender': people['gender'],
        'address': people['address'],
        'age': people['age'],
        'books': []
    }
    result_people.append(correct_data)

result_books = []
correct_books_data = {}
#Инициализация нужных данных
for books in content_with_books:
    correct_books_data = {
        'title': books['title'],
        'author': books['author'],
        'pages': books['pages']
    }
    result_books.append(correct_books_data)

len_people = len(result_people)
len_books = len(result_books)
#Подсчет книг на человека
math_result = math.ceil((len_books / len_people))

for person in result_people:
    person['books'] = []

person_index = 0

for book in result_books:
    result_people[person_index]['books'].append({
        'Title': book['title'],
        'Author': book['author'],
        'Pages': book['pages']
    })

    person_index = (person_index + 1) % len(result_people)

empty_final = []
for person in result_people:
    empty_final.append(person)


#Создание итогового файла с данными
with open("people_with_books.json", "w", encoding='utf-8') as file_finish:
    json.dump(empty_final, file_finish, ensure_ascii=False, indent=4)
