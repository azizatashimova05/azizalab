# Переопределение методов родителя
class Bird:
    def fly(self):
        print("Flying high!")

class Penguin(Bird):
    def fly(self):
        # Изменяем поведение метода
        print("Sorry, I cannot fly. I swim instead.")

pingu = Penguin()
pingu.fly()
