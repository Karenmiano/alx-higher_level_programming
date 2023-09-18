class Base:
    def __init__(self):
        self.id = 1

class Rectangle(Base):
    def __init__(self, width, height, x, y):
        super().__init__()
        self.width = width
        self.height = height
        self.x = x
        self.y = y

obj = Rectangle(10, 2, 1, 9)
print(obj.__dict__)
