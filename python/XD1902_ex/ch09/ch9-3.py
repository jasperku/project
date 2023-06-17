import random
print("===============程式描述========================")
print("= 程式名稱：ch9-3.py                          =")
print("= 程式目的：二分法搜尋程式                     =")
print("==============================================")
A=[]
def RandomNum():  #自動產生10個亂數值
  for i in range(1,11,1):
     A.append(random.randint(1,100))
  for i in range(0,len(A)):
      print(A[i],end="  ")
  print()  

def search(A, Key):
    Low = 0
    High = len(A) - 1
    while Low <= High:
        Middle = (Low + High) // 2
        if A[Middle] < Key:
            Low = Middle + 1
        elif A[Middle] > Key:
            High = Middle - 1
        else:
            return Middle
    return -1
print("=======輸入(自動產生10個亂數值)========")
RandomNum() 
print("=======排序之後========")
A.sort()
for i in range(0,len(A)):
      print(A[i],end="  ")
Key =int(input("請輸入欲搜尋資料："))
find = search(A, Key)
print("找到數值於索引 " + str(find) if find >= 0 else "找不到數值") 