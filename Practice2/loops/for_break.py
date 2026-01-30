# for loop with break
for i in range(1, 10):
    if i == 5:
        break
    print(i)
    # Example 1: Поиск первого отрицательного числа
numbers = [3, 7, -2, 9, 5]
for num in numbers:
    if num < 0:
        print(f"Найдено отрицательное: {num}")
        break

# Example 2: Поиск определенного имени
names = ["Alice", "Bob", "Charlie", "David"]
for name in names:
    if name == "Charlie":
        print("Найден Charlie")
        break

# Example 3: Прерывание при достижении суммы
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0
for n in nums:
    total += n
    if total > 15:
        print(f"Сумма превысила 15: {total}")
        break

# Example 4: Поиск первого четного числа
numbers = [1, 3, 5, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        print(f"Первое четное: {num}")
        break

# Example 5: Прерывание при вводе 'quit'
commands = ["start", "stop", "pause", "quit", "resume"]
for cmd in commands:
    if cmd == "quit":
        print("Выход из программы")
        break
    print(f"Обработка команды: {cmd}")
