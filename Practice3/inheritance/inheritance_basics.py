# Базовое наследование
class Animal:
    def breathe(self):
        print("Breathing...")

class Fish(Animal):
    def swim(self):
        print("Swimming in water...")

goldie = Fish()
goldie.breathe() # Унаследовано
goldie.swim()    # Собственный метод
