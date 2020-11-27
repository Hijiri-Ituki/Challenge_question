#3
import csv

with open('a.csv','w',newline='') as b:
    w = csv.writer(b,delimiter = ',')
    w.writerow(['Top Gun','Risky Business','Minority Report'])
    w.writerow(['Titanic','The Revenant','Inception'])
    w.writerow(['Training Day','Man on fire','Flight'])



   



