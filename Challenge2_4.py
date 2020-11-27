#4参考書参照
def x(a):
    return float(a) / 2

def y(b):
    return float(b) * 4
'''関数xの説明
引数aに入れられた数字を2で割り算する
   関数yの説明
上記の関数xで出力された商を
引数として引数bに代入し4を掛け算したものを出力する
'''

x2 = x(a = input('数字を入力'))
y2 = y(x2)

print(y2)


#4 自分で考えたもの
x = input('数字を入力')
y = int(x)/2
z = y * 4
'''
浮動小数点数オブジェクトを出力する
'''
print(z)
