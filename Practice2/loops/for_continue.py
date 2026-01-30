# for loop with continue
for i in range(1, 6):
    if i == 4:
        continue
    print(i)
# Example 1: Пропустить нечетные числа
for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i)

# Example 2: Пропустить определенные буквы
word = "python"
for letter in word:
    if letter in "aeiou":
        continue
    print(letter)

# Example 3: Пропустить отрицательные числа
numbers = [5, -2, 8, -3, 10, 7]
for num in numbers:
    if num < 0:
        continue
    print(num)

# Example 4: Пропустить пустые строки
lines = ["hello", "", "world", "", "python"]
for line in lines:
    if not line:
        continue
    print(line)

# Example 5: Пропустить деление на ноль
values = [10, 5, 0, 8, 0, 3]
for val in values:
    if val == 0:
        continue
    print(10 / val)
