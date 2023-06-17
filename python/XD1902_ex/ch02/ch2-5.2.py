print("===============程式描述========================")
print("= 程式名稱：ch2-5.2.py                        =")
print("= 程式目的：多維矩陣轉一維矩陣(以行為主)        =")
print("==============================================")
#初始設定
Array_Data1 = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]] 
Array_Data2 =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
print("==================輸入========================"); 
print("二維資料之原始資料：")
for row in range(0,3):
  for column in range(0,5):
      print("%4d" %Array_Data1[row][column],end="")
  print()
#處理
for row in range(0,3):
  for column in range(0,5):
     i = row + column * 3  
     Array_Data2[i] = Array_Data1[row][column]; 
print("==================輸出========================")  
print("以行為主：")   
for i in range(0,15):  
  print("%d " %Array_Data2[i],end="") 