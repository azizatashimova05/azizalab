# Short hand if (ternary)
a = 5
b = 10

print("a is bigger") if a > b else print("b is bigger")
# Example 1: Проверка четности
num = 7
result = "Even" if num % 2 == 0 else "Odd"
print(result)

# Example 2: Максимум из двух чисел
x = 15
y = 20
max_num = x if x > y else y
print(f"Maximum: {max_num}")

# Example 3: Проверка возраста
age = 17
status = "Adult" if age >= 18 else "Minor"
print(status)

# Example 4: Проверка строки
text = "Hello"
message = "Not empty" if text else "Empty"
print(message)

# Example 5: Абсолютное значение
value = -10
abs_value = value if value >= 0 else -value
print(f"Absolute: {abs_value}")
