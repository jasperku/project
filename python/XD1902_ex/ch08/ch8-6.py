import random
print("===============程式描述========================")
print("= 程式名稱：ch8-6.py                          =")
print("= 程式目的：謝耳排序法                         =")
print("==============================================")
A=[]
MAX=10
def RandomNum():  #自動產生10個亂數值
  for i in range(1,11,1):
     A.append(random.randint(1,10))
  for i in range(0,len(A)):
      print(A[i],end="  ")
  print()  

def Shellsort(A):  #謝耳排序法之副程式
    Gap = MAX // 2
    while(Gap > 0):
        for k in range(0,Gap,1): 
            for i in range(k+Gap,MAX,Gap): 
                for j in range(i - Gap,k-1,-Gap):
                    if(A[j] > A[j+Gap]):
                        A[j], A[j+Gap]= A[j+Gap],A[j]
                    else: 
                        break 
        for i in range(0,MAX,1):
            print(A[i],end="  ")
        print()
        Gap=Gap//2
print("=======輸入(自動產生10個亂數值)========")
RandomNum()              #呼叫產生10個亂數值的副程式
print("=========輸出(排序後結果)==============")
Shellsort(A)          #呼叫謝耳排序法的副程式