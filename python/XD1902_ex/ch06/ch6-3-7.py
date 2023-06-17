import random
print("===============程式描述========================")
print("= 程式名稱：ch6-3-7.py                        =")
print("= 程式目的：建立二元樹                         =")
print("==============================================")
Data=[0]
def RandomNum():  #自動產生9個亂數值
  for i in range(1,11,1):
     Data.append(random.randint(1,50))
  for i in range(1,len(Data)):
      print(Data[i],end="  ")
  print()  

def BTree_Create(Data,n):  #建立二元樹 之副程式
    print("樹根的鍵值為 %d" %Data[1])
    for i in range(1,10):
      if(2*i <= 10): 
         print("節點 %d 的左子樹為：%d" % (Data[i],Data[2*i]))
      if(2*i < 10):
         print("節點 %d 的右子樹為：%d" % (Data[i],Data[2*i+1]))
  
print("=========輸入(自動產生10個亂數值)==========")
RandomNum()              #呼叫產生10個亂數值的副程式
print("=========輸出(建立二元樹結果)==============")
BTree_Create(Data,10)          #呼叫建立二元樹的副程式