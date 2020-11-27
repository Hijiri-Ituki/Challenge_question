#4-2
profile = {
    '身長' : '160cm',
    '好きな色' : '白',
    '好きなラノベ' : 'デート・ア・ライブ'
    }
x = input('身長,好きな色,好きなラノベのいずれかを入力')
if x in profile:
    profiles = profile[x]
    print(profiles)
else:
    print('見つかりません')
    

