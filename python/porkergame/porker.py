from random import sample
flower = ['spade','heart','diamond','club']
num = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
c = []

for a in flower:
    for b in num:
            c += [[b,a]]
hc = sample(c,5)

for i in range(0,5):
    for j in range(0,2):
        print(hc[i][j])
    print()