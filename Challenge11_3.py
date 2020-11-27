#3
class Name:
    def __init__(self,n):
        self.namae = n

    def personal_name(self):
        return self.namae

name_1 = Name('ひじり')
name_2 = name_1
print(name_1 is name_2)

name_3 = Name('ひじり')
print(name_1 is name_3)








