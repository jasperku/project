import random
print("===============程式描述========================")
print("= 程式名稱：ch6-3-5.py                        =")
print("= 程式目的：利用一維陣列來建立二元樹            =")
print("==============================================")
Data=[0]
BTree=[0]*16
def RandomNum():  #自動產生9個亂數值
  for i in range(1,10,1):
     Data.append(random.randint(1,50))
  for i in range(1,len(Data)):
      print(Data[i],end="  ")
  print()  

def BTree_Create(BTree,Data,n):  #建立二元樹 之副程式
   for i in range(1,n): 
      node=1
      while BTree[node]!=0:
          if Data[i]>BTree[node]:          #大於樹根的鍵值 
              node=2*node+1                 #放到右子樹 
          else:                             #小於樹根的鍵值
	          node=2*node                   #放到左子樹 
      BTree[node]=Data[i]
  
def PrintBTree(BTree,n):  #排序後的結果之副程式
  for i in range(1,len(BTree)):
      print(BTree[i],end="  ")
  print() 
print("=========輸入(自動產生10個亂數值)==========")
RandomNum()              #呼叫產生9個亂數值的副程式
print("=========輸出(建立二元樹結果)==============")
BTree_Create(BTree,Data,9)          #呼叫建立二元樹的副程式
PrintBTree(BTree, 15)               #呼叫建立二元樹的結果之副程式