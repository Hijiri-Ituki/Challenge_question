#5 正規法1
x = ['The','fox','jumped','over','the','fence','.']
x = ' '.join(x)
print(x[0:-2] + '.')#:の右側の数字は要素ではなくその数字の文字数目が出力される


#5 正規法2
x = ['The','fox','jumped','over','the','fence','.']
x = ' '.join(x)
x = x[0:-2] + '.'#:の右側の数字は要素ではなくその数字の文字数目が出力される
print(x)


#5 最後のピリオドがなくなる
x = ['The','fox','jumped','over','the','fence','.']
x = ' '.join(x)
print(x[0:-2])#:の右側の数字の文字をそのまま出力される



#5  リストが出力される
x = ['The','fox','jumped','over','the','fence','.']
print(x[0:-1])#:の右側の数字の1つ小さい要素が出力される 


#5 リストが出力される
x = ['The','fox','jumped','over','the','fence','.']
x = x[0:-2]
print(x)#:の右側の数字の1つ小さい要素が出力される








