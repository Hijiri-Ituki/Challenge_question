#4-1
profile = {
    '身長' : '160cm',
    '好きな色' : '白',
    '好きなラノベ' : 'デート・ア・ライブ'
    }

x = input('身長,好きな色,好きなラノベのいずれかを入力')
if x == '身長':
    print(profile['身長'])
elif x == '好きな色':
    print(profile['好きな色'])
elif x == '好きなラノベ':
    print(profile['好きなラノベ'])
else:
    print('見つかりません')
    
