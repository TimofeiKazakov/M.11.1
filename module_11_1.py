import pandas as pd
import numpy as np
import requests

# Pandas — это программная библиотека на языке Python для обработки и анализа данных.
# Она предоставляет специальные структуры данных и операции для манипулирования числовыми
# таблицами и временными рядами.

Data = [1, 3, 2, 5, 6, 9, 4]
s = pd.Series(Data)
Index = ["a", "b", "c", "d", "e", "f", "g"]
si = pd.Series(Data, Index)
print(si)

#NumPy — это библиотека для языка программирования Python, добавляющая поддержку больших многомерных массивов и матриц,
#а также большой набор высокоуровневых математических функций для работы с этими массивами.

print()
# Создание двумерного массива
A = np.array([[1, 2, 3], [4, 5, 6]])
print("Двумерный массив:\n", A)
# Сумма элементов двумерного массива
print("Сумма элементов двумерного массива:\n", np.sum(A))

#Requests — это модуль для языка Python, который используют для упрощения работы с HTTP-запросами.
# Поиск местонахождения для запросов на GitHub
response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
)
print()
# Анализ некоторых атрибутов местонахождения запросов
json_response = response.json()
repository = json_response['items'][0]
print(f'Название репозитория: {repository["name"]}')  # Python 3.6+
print(f'Описание репозитория: {repository["description"]}')  # Python 3.6+