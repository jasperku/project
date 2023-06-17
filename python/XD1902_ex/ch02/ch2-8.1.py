print("===============程式描述========================")
print("= 程式名稱：ch2-8.1.py                        =")
print("= 程式目的：上三角矩陣轉一維矩陣(以列為主)       =")
print("==============================================")
#初始設定
Array_Data1= [[1,2,3,4,5],[0,6,7,8,9],[0,0,10,11,12],[0,0,0,13,14],[0,0,0,0,15]]
Array_Data2= [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
#轉換前 
print("上三角矩陣的原始資料：")
for row in range(0,5):
  for column in range(0,5):
      print("%4d" % Array_Data1[row][column],end="")
  print()
#轉換
Location=0  
for row in range(0,5):
  for column in range(0,5):
      if(Array_Data1[row][column] != 0):   #非0元素
           Array_Data2[Location] = Array_Data1[row][column]
           Location=Location+1
#輸出結果
print("輸出結果：")
for i in range(0,len(Array_Data2)):
      print("%4d" % Array_Data2[i],end="")
print()