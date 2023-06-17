print("===============程式描述========================")
print("= 程式名稱：ch2-7.3.py                        =")
print("= 程式目的：2個矩陣相乘                        =")
print("==============================================")
#初始設定
Array_A = [[1,2,3], [4,5,6]] 
Array_B = [[1,0,1],[1,1,0],[0,1,1]] 
Array_C = [[0,0,0], [0,0,0]]    
#轉換前 
print("輸出A矩陣：")
for row in range(0,2):
  for column in range(0,3):
      print("%4d" % Array_A[row][column],end="")
  print()
print("輸出B矩陣：")
for row in range(0,3):
  for column in range(0,3):
      print("%4d" % Array_B[row][column],end="")
  print()
#轉換程式
for row in range(0,2):
  for column in range(0,3):
       Array_C[row][column]=0;
       for k in range(0,3):
        Array_C[row][column] = Array_C[row][column] + Array_A[row][k] * Array_B[k][column]; 
print("輸出A*B=C的結果：")
for row in range(0,2):
  for column in range(0,3):
      print("%4d" % Array_C[row][column],end="")
  print()