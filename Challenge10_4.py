#4
class Horse:
    def __init__(self,n,r):
        self.name = n
        self.rider = r

class Rider:
    def __init__(self,n):
        self.name = n

taketoyo = Rider('武豊')
kitasan = Horse('キタサンブラック',taketoyo)

print('馬の名前は{}です。'.format(kitasan.name))
print('騎手の名前は{}です。'.format(kitasan.rider.name))
