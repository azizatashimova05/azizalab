# while loop with continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
# Example 1: Пропустить нечетные числа
i = 0
while i < 10:
    i += 1
    if i % 2 != 0:
        continue
    print(i)

# Example 2: Пропустить определенные буквы
word = "python"
index = 0
while index < len(word):
    letter = word[index]
    index += 1
    if letter in "aeiou":
        continue
    print(letter)

# Example 3: Пропустить отрицательные числа
numbers = [5, -2, 8, -3, 10, 7]
i = 0
while i < len(numbers):
    num = numbers[i]
    i += 1
    if num < 0:
        continue
    print(num)

# Example 4: Пропустить пустые строки
lines = ["hello", "", "world", "", "python"]
i = 0
while i < len(lines):
    line = lines[i]
    i += 1
    if not line:
        continue
    print(line)

# Example 5: Пропустить деление на ноль
values = [10, 5, 0, 8, 0, 3]
i = 0
while i < len(values):
    val = values[i]
    i += 1
    if val == 0:
        continue
    print(10 / val)
