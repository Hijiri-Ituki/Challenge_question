#1
print('愛知県')
print('岐阜県')
print('三重県')

x = ['愛知県','岐阜県','三重県']
print(x)


#2
x = 10
if x < 10:
    print('10未満')
else:
    print('10以上')
    

#x =input('数字入力')
#if int(x) <10:
#    print('10未満')
#else:
#    print('10以上')


#3
x = 26
if x <= 10:
    print('10以下')
elif 10 < x <= 25:        #ここはelif x <= 25:でも良い
    print('10以上25以下')
else:
    print('25より大きい')


#4
x = 100
y = 13
z = x%y
print(z)#今回のチャレンジの場合ここまでok
a = x/y
b = x//y
print(a)
print(b)


#5
x = 100
y = 4
z = x/y
print(z)


#6
age = input('年齢は？')
age2 = int(age)
if age2 < 20:
    print('未成年')
    if age2 <= 6:
        print('未就学児')
    elif age2 <= 15:
        print('義務教育')
    else:
        print('残り4歳分')
elif age2 <= 65:
    print('成人')
else:
    print('高齢者')


   
    


