#3
class Shape:
    def what_am_i(self):
        return print('I am a shape')

class Rectangle(Shape):
    def __init__(self,v,h):
        self.vertical = v
        self.holizontal = h

    def calculate_perimeter(self):
        return self.vertical * 2 + self.holizontal * 2

class Square(Shape):
    def __init__(self,s):
        self.side = s

    def calculate_perimeter(self):
        return self.side * 4

rectangle = Rectangle(3,5)
print(rectangle.what_am_i())

square = Square(7)
print(square.what_am_i())


    
    
        
