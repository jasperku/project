import random
print("===============程式描述========================")
print("= 程式名稱：ch9-2.py                          =")
print("= 程式目的：循序搜尋程式                       =")
print("==============================================")
A=[]
def RandomNum():  #自動產生10個亂數值
  for i in range(1,11,1):
     A.append(random.randint(1,100))
  for i in range(0,len(A)):
      print(A[i],end="  ")
  print()  
def Sequential_search(A,key):  #循序搜尋之副程式
  for i in range(0,10):        #從頭到尾拜訪一次
    if A[i] == key:	      #比對陣列內的資料是否等於欲搜尋的條件
        print("陣列中的第 %d 筆" %(i+1))
print("=======輸入(自動產生10個亂數值)========")
RandomNum()              #呼叫產生10個亂數值的副程式
key =int(input("請輸入欲搜尋資料："))
print("=========輸出結果)==============")
Sequential_search(A,key)
