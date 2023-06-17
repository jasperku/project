import random
print("===============程式描述========================")
print("= 程式名稱：ch8-5.py                          =")
print("= 程式目的：快速排序法                         =")
print("==============================================")
A=[]
def RandomNum():  #自動產生10個亂數值
  for i in range(1,11,1):
     A.append(random.randint(1,10))
  for i in range(0,len(A)):
      print(A[i],end="  ")
  print()  

def QuickSort(data,left,right):  #快速排序之副程式
    if left >= right :            # 如果左邊大於右邊，就跳出function
        return
    lower = left                     
    upper = right                     
    key = data[left]              # 基準點

    while lower != upper:                  
        while data[upper] > key and lower < upper:   # 從右邊開始找，找比基準點小的值
            upper -= 1
        while data[lower] <= key and lower < upper:  # 從左邊開始找，找比基準點大的值
            lower += 1
        if lower < upper:                        # 當左右代理人沒有相遇時，互換值
            data[lower], data[upper] = data[upper], data[lower] 
    # 將基準點歸換至代理人相遇點
    data[left] = data[lower] 
    data[lower] = key
    QuickSort(data, left, lower-1)   # 繼續處理較小部分的子循環
    QuickSort(data, lower+1, right)  # 繼續處理較大部分的子循環

def PrintQuickSort(A,n):  #排序後的結果之副程式
  for i in range(0,len(A)):
      print(A[i],end="  ")
  print() 
  
print("=======輸入(自動產生10個亂數值)========")
RandomNum()              #呼叫產生10個亂數值的副程式
print("=========輸出(排序後結果)==============")
QuickSort(A,0,9)          #呼叫快速排序法的副程式
PrintQuickSort(A, 10)     #呼叫排序後的結果之副程式