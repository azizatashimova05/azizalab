# while loop with break
i = 1
while i <= 10:
    if i == 6:
        break
    print(i)
    i += 1
# Example 1: Поиск первого отрицательного числа
numbers = [3, 7, -2, 9, 5]
i = 0
while i < len(numbers):
    if numbers[i] < 0:
        print(f"Найдено отрицательное: {numbers[i]}")
        break
    i += 1

# Example 2: Поиск определенного имени
names = ["Alice", "Bob", "Charlie", "David"]
index = 0
while index < len(names):
    if names[index] == "Charlie":
        print("Найден Charlie")
        break
    index += 1

# Example 3: Прерывание при достижении суммы
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0
i = 0
while i < len(nums):
    total += nums[i]
    if total > 15:
        print(f"Сумма превысила 15: {total}")
        break
    i += 1

# Example 4: Поиск первого четного числа
numbers = [1, 3, 5, 8, 9, 10]
i = 0
while i < len(numbers):
    if numbers[i] % 2 == 0:
        print(f"Первое четное: {numbers[i]}")
        break
    i += 1

# Example 5: Прерывание при вводе 'quit'
commands = ["start", "stop", "pause", "quit", "resume"]
i = 0
while i < len(commands):
    if commands[i] == "quit":
        print("Выход из программы")
        break
    print(f"Обработка команды: {commands[i]}")
    i += 1
