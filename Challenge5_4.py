x = 2
x2 = input('数字を入力')
x3 = int(x2)
if x3 > x:
    print('x2はxより大きい')
elif x3 < x:
    print('x2はxより小さい')
else:
    print('x2はxと同じ')


#4
print('数字あてゲーム')

a = [11, 32, 33, 15, 1]

while True:
    b = input("数字を推測するか、ｑで終了します")
    if b == "q":
        break
    try:
        b = int(b)
    except ValueError:
        print("数字を入力するか、ｑで終了してください")
    if b in a:
        print("あなたが推測した数字は当たっていました！")
    else:
        print("あなたが推測したものは外れてしまいました")




