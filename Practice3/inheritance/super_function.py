# Использование super() для расширения родительского метода
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):
    def __init__(self, side):
        # Вызываем конструктор родителя
        super().__init__(side, side)

sq = Square(10)
print(f"Area: {sq.length * sq.width}")
