#3
class Triangle:
    def __init__(self,b,h):
        self.bottom = b
        self.height = h
    print('作成した')

# 三角形の面積
    def area(self):
        return self.bottom * self.height / 2

triangle = Triangle(2,3)
print(triangle.area())

    
