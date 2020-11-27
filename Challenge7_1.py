#1
with open('x.txt','w') as y:
    y.write("sport = ['テニス','野球','サッカー']")


with open('x.txt','r') as y:
    print(y.read())
