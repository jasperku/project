print("===============程式描述========================")
print("= 程式名稱：ch2-7.2.py                        =")
print("= 程式目的：2個矩陣相加                        =")
print("==============================================")
#初始設定
Array_A = [[1,2,3], [4,5,6]] 
Array_B = [[11,12,13], [14,15,16]] 
Array_C = [[0,0,0], [0,0,0]]    
#轉換前 
print("輸出A矩陣：")
for row in range(0,2):
  for column in range(0,3):
      print("%4d" % Array_A[row][column],end="")
  print()
print("輸出B矩陣：")
for row in range(0,2):
  for column in range(0,3):
      print("%4d" % Array_B[row][column],end="")
  print()
#轉換程式
for row in range(0,2):
  for column in range(0,3):
     Array_C[row][column] = Array_A[row][column] + Array_B[row][column]
print("輸出A+B=C的結果：")
for row in range(0,2):
  for column in range(0,3):
      print("%4d" % Array_C[row][column],end="")
  print()