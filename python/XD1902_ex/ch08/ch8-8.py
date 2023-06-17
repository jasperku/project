import random
print("===============程式描述========================")
print("= 程式名稱：ch8-8.py                          =")
print("= 程式目的：基數排序法                         =")
print("==============================================")
data=[]
order=[]
temp=[],[]
def RandomNum():  #自動產生10個亂數值
  for i in range(1,11,1):
     data.append(random.randint(1,101))
  for i in range(0,len(data)):
      print(data[i],end="  ")
  print()  
def RadixSort(data,d):  #基數排序法之副程式    
    size = len(data)
    k = 0
    n = 1
    temp = []
    for i in range(size):
        temp.append([0] * size)
    order = [0] * size
    while n <= d:
        for i in range(size):
            lsd = (data[i] // n) % 10
            temp[lsd][order[lsd]] = data[i]
            order[lsd] += 1
        for i in range(size):
            if order[i] != 0:
                for j in range(order[i]):
                    data[k] = temp[i][j]
                    k += 1
            order[i] = 0
        n *= 10
        k = 0                  
def PrintRadixSort(data,n):  #排序後的結果之副程式
  for i in range(0,len(data)):
      print(data[i],end="  ")
  print() 
print("=======輸入(自動產生10個亂數值)========")
RandomNum()              #呼叫產生10個亂數值的副程式
print("=========輸出(排序後結果)==============")
RadixSort(data, 10)          #呼叫基數排序法的副程式
PrintRadixSort(data, 10)     #呼叫排序後的結果之副程式