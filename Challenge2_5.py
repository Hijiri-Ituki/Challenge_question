#5 参考書参照　
def x(a):
    try:
        return float(a)
    except ValueError:
        print('整数を入力')
'''関数xの説明
引数aに数字が入れられた場合
浮動小数点数オブジェクトを出力する。

引数aに数字以外のものが入れられた場合
例外処置が実行される
'''

x2 = x(55.0)#←()の中の''クォートは必須 
print(x2)


#5 自分なりに改良したもの
def x(a):
    try:
        return float(a)
    except ValueError:
        print('数字以外受け付けません')

x2 = x(a = input("数字を入力"))
print(x2)

















    
    
