Python — популярный язык программирования. Он был создан Гвидо ван Россумом и выпущен в 1991 году.

Он используется для:

веб-разработка (серверная часть),
разработка программного обеспечения,
математика,
системный скриптинг.

Что может Питон?
Python можно использовать на сервере для создания веб-приложений.
Python можно использовать вместе с программным обеспечением для создания рабочих процессов.
Python может подключаться к системам баз данных. Он также может читать и изменять файлы.
Python можно использовать для обработки больших данных и выполнения сложных математических операций.
Python можно использовать для быстрого прототипирования или для разработки готового программного обеспечения.

Отступы — это пробелы в начале строки кода.

Если в других языках программирования отступы в коде предназначены только для удобочитаемости, то в Python отступы очень важны.

Python использует отступ для обозначения блока кода.
if 5 > 2:
  print("Five is greater than two!")
  Вы должны использовать одинаковое количество пробелов в одном и том же блоке кода, иначе Python выдаст вам ошибку.

  Комментарии начинаются с #
  Комментарии могут быть размещены в конце строки, и Python проигнорирует оставшуюся часть строки:
Пример
print("Hello, World!") #This is a comment
Python на самом деле не имеет синтаксиса для многострочных комментариев.
Чтобы добавить многострочный комментарий, вы можете вставить a #для каждой строки.
Python будет игнорировать строковые литералы, которые не назначены переменной, вы можете добавить в свой код многострочную строку (тройные кавычки) и поместить в нее свой комментарий:

Пример
"""
This is a comment
written in
more than just one line
"""
Casting
If you want to specify the data type of a variable, this can be done with casting.

Example
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

You can get the data type of a variable with the type() function.

Example
x = 5
y = "John"
print(type(x))
print(type(y))

Имена переменных
Переменная может иметь короткое имя (например, x и y) или более описательное имя (возраст, имя автомобиля, общий_объем). Правила для переменных Python:
Имя переменной должно начинаться с буквы или символа подчеркивания.
Имя переменной не может начинаться с цифры
Имя переменной может содержать только буквенно-цифровые символы и символы подчеркивания (Az, 0–9 и _).
Имена переменных чувствительны к регистру (возраст, возраст и возраст — это три разные переменные).
Multi Words Variable Names
Variable names with more than one word can be difficult to read.

There are several techniques you can use to make them more readable:

Camel Case
Each word, except the first, starts with a capital letter:
myVariableName = "John"

Pascal Case
Each word starts with a capital letter:
MyVariableName = "John"

Snake Case
Each word is separated by an underscore character:
my_variable_name = "John"
Множество значений для нескольких переменных
Python позволяет вам присваивать значения нескольким переменным в одной строке:

Пример
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

Unpack a Collection
If you have a collection of values in a list, tuple etc. Python allows you extract the values into variables. This is called unpacking.

Example
Unpack a list:

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

Оператор Python printчасто используется для вывода переменных.

Чтобы объединить текст и переменную, Python использует +символ:

Пример
x = "awesome"
print("Python is " + x)
Python is awesome
Вы также можете использовать этот +символ, чтобы добавить переменную к другой переменной:

Пример
x = "Python is "
y = "awesome"
z =  x + y
print(z)
Для чисел +символ работает как математический оператор:

Пример
x = 5
y = 10
print(x + y)
Если вы попытаетесь объединить строку и число, Python выдаст вам ошибку:

Пример
x = 5
y = "John"
print(x + y)
JS-de ise bu mumkundu setir ve ededi birlesdirirdi

Python - Global Variables
Global variables can be used by everyone, both inside of functions and outside.

Example
Create a variable outside of a function, and use it inside the function

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

To create a global variable inside a function, you can use the global keyword.
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

Чтобы изменить значение глобальной переменной внутри функции, обратитесь к переменной с помощью globalключевого слова:

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)