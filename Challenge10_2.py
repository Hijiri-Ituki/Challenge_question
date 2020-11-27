#2
class Square:
    def __init__(self,s):
        self.side = s

    def calculate_perimeter(self):
        return self.side * 4

    def change_size(self,n_s):
        self.side = self.side + n_s

square = Square(3)
print(square.side)

square.change_size(5)
print(square.side)






        
        

    
