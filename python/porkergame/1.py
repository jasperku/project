import random
import string
flower = ['黑桃','紅心','方塊','梅花']
num = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
i = 0
while i < 1:
    carda = random.choice(flower),random.choice(num)
    cardb = random.choice(flower),random.choice(num)
    cardc = random.choice(flower),random.choice(num)
    cardd = random.choice(flower),random.choice(num)
    carde = random.choice(flower),random.choice(num)
    if  carda != cardb != cardc != cardd != carde:
        i = i + 1 
print(carda,cardb,cardc,cardd,carde)

if carda[0] == cardb[0]:
    print("一對")