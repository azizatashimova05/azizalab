# Применение функции к каждому элементу списка
numbers = [1, 2, 3, 4, 5]
# Возводим каждое число в куб
cubed_numbers = list(map(lambda x: x**3, numbers))
print(f"Cubed: {cubed_numbers}")
