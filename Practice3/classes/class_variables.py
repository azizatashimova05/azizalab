# Отличие переменных класса от переменных экземпляра
class Employee:
    # Переменная класса 
    raise_amount = 1.05 
    
    def __init__(self, name, salary):
        self.name = name # Переменная экземпляра
        self.salary = salary

emp = Employee("Alex", 50000)
print(f"Global raise: {Employee.raise_amount}")
