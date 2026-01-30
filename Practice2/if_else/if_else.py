# if else example
number = 7

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
# Example 1: Проверка возраста
age = 20

if age >= 18:
    print("Взрослый")
else:
    print("Ребенок")

# Example 2: Проверка температуры
temp = 25

if temp > 30:
    print("Жарко")
else:
    print("Нормально")

# Example 3: Проверка пустой строки
text = ""

if text:
    print("Не пусто")
else:
    print("Пустая строка")

# Example 4: Проверка списка
my_list = [1, 2, 3]

if my_list:
    print("Список не пустой")
else:
    print("Пустой список")

# Example 5: Проверка вхождения
name = "Alice"

if name in ["Alice", "Bob", "Charlie"]:
    print("Имя найдено")
else:
    print("Имя не найдено")
