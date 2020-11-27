#1
class Square:
    square_list = []
    
    def __init__(self,s):
        self.side = s
        self.square_list.append(self.side)

square = Square(3)
square = Square(23)
square = Square(54)

print(square.square_list)

    
