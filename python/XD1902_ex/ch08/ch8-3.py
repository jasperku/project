import random
print("===============程式描述========================")
print("= 程式名稱：ch8-3.py                          =")
print("= 程式目的：選擇排序法                         =")
print("==============================================")
A=[]
def RandomNum():  #自動產生10個亂數值
  for i in range(1,11,1):
     A.append(random.randint(1,10))
  for i in range(0,len(A)):
      print(A[i],end="  ")
  print()  

def SelSort(A,n):  #選擇排序之副程式
    i,j,Min=0,0,0
    for i in range(len(A)): 
        Min = i
        for j in range(i+1,n,1):
           if (A[j] < A[Min]):
              Min = j
              #相鄰兩個的資料交換位置
        if Min != i:#找到最小元素進行交換
              A[i],A[Min] = A[Min],A[i]      
def PrintSelSort(A,n):  #排序後的結果之副程式
  for i in range(0,len(A)):
      print(A[i],end="  ")
  print() 
print("=======輸入(自動產生10個亂數值)========")
RandomNum()              #呼叫產生10個亂數值的副程式
print("=========輸出(排序後結果)==============")
SelSort(A, 10)          #呼叫選擇排序法的副程式
PrintSelSort(A, 10)     #呼叫排序後的結果之副程式