import random
print("===============程式描述========================")
print("= 程式名稱：ch8-7.py                         =")
print("= 程式目的：合併排序法                       =")
print("==============================================")
A,B,C=[],[],[]
MAX1,MAX2=10,10

def RandomNum():  #自動產生10個亂數值
  for i in range(1,11,1):
     A.append(random.randint(10,50))  #/產生10~50的整數亂數值
     B.append(random.randint(51,99))  #/產生51~99的整數亂數值
  print("產生10個亂數值：") 
  print("第一組資料：")
  for i in range(0,len(A)):
      print(A[i],end="  ")
  print()  
  print("第二組資料：")
  for i in range(0,len(B)):
      print(B[i],end="  ")
  print()  
  
#快速排序法之副程式
def Quicksort(A,left,right):
  q=0 
  if(left < right): 
      q = partition(A, left, right)
      Quicksort(A, left, q-1)
      Quicksort(A, q+1, right)


#分割之副程式 
def partition(A,left,right):
    i,j,s=0,0,0 
    s = A[right]
    i = left - 1
    for j in range(left,right,1): 
        if(A[j] <= s):
           i=i+1 
           A[i],A[j]=A[j],A[i]  
           
    A[i+1], A[right]=A[right],A[i+1]
    return i+1

#快速排序法之副程式 
def PrintQuicksort(A,n):  
    i=0
    print("第一組資料：") 
    for i in range(0,MAX1,1): 
        print(A[i],end="  ") 
    print()
    print("第二組資料：")
    for j in range(0,MAX2,1): 
        print(B[j],end="  ")  

#進行合併排序
def Mergesort(A,B,C):
    i,j = 0,0
    for k in range(20):
        if (k<10):
           C.append(A[i])
           i=i+1
        else:
           C.append(B[j])
           j=j+1
#顯示合併排序之結果
def PrintMergesort(C):  #合併後之副程式 
    i=0
    print() 
    print("合併後：") 
    for i in range(0,MAX1+MAX2,1): 
        print(C[i],end="  ") 

print("=======輸入(自動產生10個亂數值)========")
RandomNum()              #呼叫產生10個亂數值的副程式
print("=========輸出(排序後結果)==============")
Quicksort(A, 0, MAX1-1)    #第一組資料排序 
Quicksort(B, 0, MAX2-1)    #第二組資料排序
PrintQuicksort(A,B)        #列印出第一與二組資料排序結果 
Mergesort(A,B,C) #進行合併排序 
PrintMergesort(C)          #顯示合併排序之結果
