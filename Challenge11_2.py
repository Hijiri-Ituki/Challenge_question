#2_1
class Square:
    def __init__(self,s):
        self.side = s

    def __repr__(self):
        return '{}by{}by{}by{}'.format(self.side,self.side,self.side,self.side)

square = Square(12)
print(square)

#2_2
class Square:
    def __init__(self,s):
        self.side = s

    def four_side(self):
        return '{}by{}by{}by{}'.format(self.side,self.side,self.side,self.side)

square = Square(12)
print(square.four_side())



