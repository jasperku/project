print("===============程式描述========================")
print("= 程式名稱：ch3-6.4.py                        =")
print("= 程式目的：計算河內塔問題                     =")
print("==============================================")
#遞迴函式名稱
def Towers(N,From,Through,To):  
 if (N > 0):
    Towers (N - 1, From, To, Through)
    print("將盤子%d從柱子%s移到柱子%s" %( N, From, To))
    Towers (N - 1, Through, From, To)

print("===================輸入======================") 
N = int(input("請輸入盤子個數N="))
print("===================輸出======================") 
Towers (N,'A','B','C')