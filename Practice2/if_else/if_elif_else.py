# if elif else example
score = 85

if score >= 90:
    print("A")
elif score >= 75:
    print("B")
elif score >= 60:
    print("C")
else:
    print("F")
# Example 1: Проверка числа
num = 10

if num > 0:
    print("Положительное")
elif num < 0:
    print("Отрицательное")
else:
    print("Ноль")

# Example 2: Проверка времени суток
hour = 14

if hour < 12:
    print("Утро")
elif hour < 18:
    print("День")
elif hour < 22:
    print("Вечер")
else:
    print("Ночь")

# Example 3: Проверка пароля
password = "admin123"
min_length = 8

if len(password) < min_length:
    print("Слишком короткий")
elif not any(c.isdigit() for c in password):
    print("Добавьте цифры")
elif not any(c.isalpha() for c in password):
    print("Добавьте буквы")
else:
    print("Пароль надежный")

# Example 4: Калькулятор скидок
purchase = 5000

if purchase >= 10000:
    discount = 20
elif purchase >= 5000:
    discount = 10
elif purchase >= 1000:
    discount = 5
else:
    discount = 0

print(f"Скидка: {discount}%")

# Example 5: Проверка возраста
age = 25

if age < 13:
    print("Ребенок")
elif age < 18:
    print("Подросток")
elif age < 65:
    print("Взрослый")
else:
    print("Пенсионер")
