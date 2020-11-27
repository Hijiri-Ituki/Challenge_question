#1
# 長方形のコード
class Rectangle:
    def __init__(self,v,h):
        self.vertical = v
        self.holizontal = h
        
    def calculate_perimeter(self):
        return self.vertical * 2 + self.holizontal * 2
    
# 正方形のコード
class Square:
    def __init__(self,s):
        self.side = s

    def calculate_perimeter(self):
        return self.side * 4
    
rectangle = Rectangle(2,3)
print(rectangle.calculate_perimeter())

square = Square(2)
square.side = 5
print(square.calculate_perimeter())
