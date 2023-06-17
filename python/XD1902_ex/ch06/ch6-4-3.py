import random
print("===============程式描述========================")
print("= 程式名稱：ch6-4-3.py                        =")
print("= 程式目的：建立一個二元樹後序追蹤              =")
print("==============================================")
Data=[]
BinaryTree=[0]*22
def RandomNum():  #自動產生10個亂數值
  for i in range(1,11,1):
     Data.append(random.randint(1,50))
  for i in range(0,len(Data)):
      print(Data[i],end="  ")
  print()  
  
#建立二元樹之副程式
def CreateBinaryTree(Data,n): 
    node=1
    for i in range(0,n*2):
        BinaryTree[i]=0         #初值設定  
    for i in range(0,n):    
        BinaryTree[node]=Data[i]
        node=node+1
        
#進行後序之副程式 
def Postorder(node):
    if (BinaryTree[node]!=0):
        Postorder(2*node)           #遞迴左子樹
        Postorder(2*node+1)         #遞迴右子樹
        if (BinaryTree[node]!=0):
          print(BinaryTree[node],end="  ")  #列印樹根 

print("=========輸入(自動產生10個亂數值)==========")
RandomNum()              #呼叫產生10個亂數值的副程式
print("=========輸出(建立二元樹結果)==============")
CreateBinaryTree(Data,10)          #呼叫建立二元樹的副程式
Postorder(1)   #呼叫後序之副程式 