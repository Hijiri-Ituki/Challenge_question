#4
import csv

with open('b.csv','w',encoding='utf_8_sig') as c:
    w = csv.writer(c,delimiter=',')
    w.writerow(['トップガン','リスキービジネス'])
    w.writerow(['インセプション','タイタニック'])
    w.writerow(['トレーニングデイ','マンオンファイア'])
