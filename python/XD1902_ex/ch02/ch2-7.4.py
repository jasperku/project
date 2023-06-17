print("===============程式描述========================")
print("= 程式名稱：ch2-7.4.py                        =")
print("= 程式目的：將一稀疏矩陣轉換成壓縮的表示法       =")
print("==============================================")
#初始設定
Sparse= [[5, 0, 0], [0, 0, -1], [3, 0, 0], [0, 9, 10]]
Compress = [[0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0]]    
#轉換前 
print("輸出稀疏矩陣：")
for row in range(0,4):
  for column in range(0,3):
      print("%4d" % Sparse[row][column],end="")
  print()
#壓縮處理
k = 1                              #設定變數初值     
Compress[0][0] = 4                # 陣列sparse有m列  
Compress[0][1] = 3                # 陣列sparse有n行 
Compress[0][2] = 5                # 陣列使用5個元素
for row in range(0,4):
  for column in range(0,3):
      if ( Sparse[row][column] != 0 ):         # 判斷是否為非0元素   
          Compress[k][0] = row                 # 儲存列數         
          Compress[k][1] = column              # 儲存行數         
          #儲存元素值
          Compress[k][2] = Sparse[row][column]   
          k=k+1
print("輸出壓縮結果：")
for row in range(0,6):
  for column in range(0,3):
      print("%4d" % Compress[row][column],end="")
  print()