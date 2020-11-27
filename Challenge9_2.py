#2
import math

class Circle:
    def __init__(self,v,s,r):
        self.vertical = v
        self.side = s
        self.radius = r
    print('作成した!')

# 長方形、正方形の面積
    def area1(self):
        return self.vertical * self.side

# 円の面積
    def area2(self):
        return self.radius ** 2 * math.pi

circle = Circle(5,7,2)
print(circle.area1())
print(circle.area2())



    
