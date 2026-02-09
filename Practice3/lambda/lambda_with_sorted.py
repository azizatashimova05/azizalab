# Сортировка сложных структур данных
students = [("Alice", 88), ("Bob", 75), ("Charlie", 92)]
# Сортируем по оценке
sorted_students = sorted(students, key=lambda student: student[1])
print(f"Sorted by score: {sorted_students}")
