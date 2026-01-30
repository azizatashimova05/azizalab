# while loop example
i = 1
while i <= 5:
    print(i)
    i += 1
    # Example 1: Обратный отсчет
count = 5
while count > 0:
    print(count)
    count -= 1
print("Старт!")

# Example 2: Сумма чисел
total = 0
num = 1
while num <= 10:
    total += num
    num += 1
print(f"Сумма: {total}")

# Example 3: Умножение на 2
x = 1
while x <= 16:
    print(x)
    x *= 2

# Example 4: Вывод каждого третьего числа
n = 3
while n <= 15:
    print(n)
    n += 3

# Example 5: Бесконечный цикл с условием выхода
counter = 0
while True:
    print(f"Итерация {counter}")
    counter += 1
    if counter >= 3:
        break
