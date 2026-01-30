# Boolean comparisons
a = 10
b = 5

print(a > b)
print(a == b)
print(a != b)
print(a <= b)


print("\n=== Пример 1: Сравнение строк ===")
str1 = "hello"
str2 = "world"
str3 = "hello"

print(str1 == str3)  # True - одинаковые строки
print(str1 != str2)  # True - разные строки
print(str1 > str2)   # False - 'h' идет раньше 'w' в алфавите
print(str1 < str2)   # True
print("apple" == "Apple")  # False - регистр имеет значение
print("Python" >= "Java")  # True - 'P' идет после 'J'

print("\n=== Пример 2: Логические операторы ===")
x = 15
y = 10
z = 20

print(x > y and x < z)   # True - 15 > 10 И 15 < 20
print(x > y or x > z)    # True - 15 > 10 (достаточно одного True)
print(not x == y)        # True - not False = True
print(x > y and not z < x)  # True - 15 > 10 И not(20 < 15)
print((x > y) == (z > x))  # True - (True) == (True) → True
print(not (x < y or z < x))  # False

print("\n=== Пример 3: Сравнение списков ===")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [1, 2, 4]
list4 = [1, 2]

print(list1 == list2)  # True - одинаковые элементы
print(list1 != list3)  # True - разные элементы
print(list1 > list4)   # True - [1,2,3] > [1,2] (третий элемент есть)
print(list4 < list1)   # True
print([] == [])        # True - оба пустые списки
print([5, 6] >= [5, 6])  # True

print("\n=== Пример 4: Комбинированные сравнения ===")
a = 7
b = 3
c = 5

print(a + b > c)           # True - 10 > 5
print(a * b == 21)         # True - 7 * 3 = 21
print(a % b != 0)          # True - 7 % 3 = 1, 1 != 0
print((a - b) <= (c + 1))  # True - 4 <= 6
print(b**2 >= a)           # True - 9 >= 7
print((a + b) * 2 == 20)   # True - (7+3)*2 = 20

print("\n=== Пример 5: Сравнение разных типов ===")
print(0 == False)          # True - 0 эквивалентен False
print(1 == True)           # True - 1 эквивалентен True
print("" == False)         # False - пустая строка не равна False
print(None == None)        # True
print(10 == 10.0)          # True - целое равно float
print([1] == [1])          # True
print([1] is [1])          # False - разные объекты в памяти
print(3.14 <= 3.14159)     # True
print(100 >= 99.999)       # True

print("\n=== Пример 6: Операторы 'in' и 'is' ===")
name = "Python"
numbers = [1, 2, 3, 4, 5]
empty_list = []
none_value = None

print("P" in name)             # True
print("thon" in name)          # True
print("Java" not in name)      # True
print(3 in numbers)            # True
print(10 not in numbers)       # True
print(empty_list == [])        # True
print(empty_list is [])        # False - разные объекты
print(none_value is None)      # True
print(none_value == None)      # True

print("\n=== Пример 7: Цепочки сравнений ===")
num = 10
print(5 < num < 15)        # True - 5 < 10 < 15
print(0 <= num <= 100)     # True - 0 <= 10 <= 100
print(10 == num == 10.0)   # True - 10 == 10 == 10.0
print(1 != num != 20)      # True - 1 ≠ 10 ≠ 20

print("\n=== Пример 8: Сложные логические выражения ===")
age = 25
has_license = True
has_car = False

can_drive = age >= 18 and has_license
print(f"Может водить: {can_drive}")  # True

can_rent_car = age >= 21 and has_license and not has_car
print(f"Может арендовать машину: {can_rent_car}")  # True

is_teenager = 13 <= age <= 19
print(f"Подросток: {is_teenager}")  # False

print("\n=== Итоговые проверки ===")
print("Все примеры выполнены успешно!")
