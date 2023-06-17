print("===============程式描述========================")
print("= 程式名稱：ch2-7.1.py                        =")
print("= 程式目的：矩陣轉置                           =")
print("==============================================")
#初始設定
Array_A = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]] 
Array_B =[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]     
#轉換前 
print("轉換前：")
for row in range(0,4):
  for column in range(0,4):
      print("%4d" % Array_A[row][column],end="")
  print()
#轉換程式
for row in range(0,4):
  for column in range(0,4):
       Array_B[column][row] = Array_A[row][column]
#轉換後 
print("轉換後：")
for row in range(0,4):
  for column in range(0,4):
     print("%4d" % Array_B[row][column],end="")
  print()      