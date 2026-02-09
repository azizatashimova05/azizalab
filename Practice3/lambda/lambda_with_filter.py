# Фильтрация списка на основе условия
ages = [12, 18, 25, 15, 30, 8]
# Оставляем только тех, кто старше 18
adults = list(filter(lambda age: age >= 18, ages))
print(f"Adults: {adults}")
