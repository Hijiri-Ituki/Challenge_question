#2
x = input('あなたの性別は？')
with open('your_sex.txt','w') as y:
    y.write(x)
