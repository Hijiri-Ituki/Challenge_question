#3 参考書参照
def c(x,y,z,a=2,b=3):
    return x+a,z*b,x+y+z

c2 = c(1,2,3)
print(c2)


#3　自分で改良したもの c2を見やすくした
def c(x,y,z,a=2,b=3):
    try:
        return int(x) + a,int(z) * b,int(x) + int(y) + int(z)
    except ValueError:
        print('数字のみ受け付け')
'''関数cの説明
引数x,y,zに入れられた数字を使い計算
その答えを出力する
'''
c2 = c(x = input('1つ目の数字を入力'),
       y = input('2つ目の数字を入力'),
       z = input('3つ目の数字を入力'))
print(c2)


#3 自分で改良したもの c2が見にくい
def c(x,y,z,a=2,b=3):
    try:
        return int(x) + a,int(z) * b,int(x) + int(y) + int(z)
    except ValueError:
        print('数字のみ受け付け')
'''関数cの説明
引数x,y,zに入れられた数字を使い計算
その答えを出力する
'''
c2 = c(x = input('1つ目の数字を入力'),y = input('2つ目の数字を入力'),z = input('3つ目の数字を入力'))
print(c2)
