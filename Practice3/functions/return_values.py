# Возврат значения из функции
def calculate_area(radius):
    """Вычисляет площадь круга"""
    pi = 3.14159
    return pi * (radius ** 2)

circle_area = calculate_area(5)
print(f"The area is: {circle_area}")
