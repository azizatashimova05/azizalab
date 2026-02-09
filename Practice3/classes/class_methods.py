# Определение методов внутри класса
class Smartphone:
    def __init__(self, model):
        self.model = model
    
    def call(self, number):
        """Метод для совершения звонка"""
        return f"{self.model} is calling {number}..."

my_phone = Smartphone("iPhone 15")
print(my_phone.call("8-800-555-35-35"))
