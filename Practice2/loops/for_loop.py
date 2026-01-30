# for loop example
for i in range(1, 6):
    print(i)
# Example 1: Вывод квадратов чисел
for i in range(1, 6):
    print(i ** 2)

# Example 2: Итерация по списку
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Example 3: Вывод букв строки
word = "Python"
for letter in word:
    print(letter)

# Example 4: Сумма чисел
total = 0
for num in range(1, 11):
    total += num
print(f"Сумма: {total}")

# Example 5: Таблица умножения
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} * {j} = {i * j}")
