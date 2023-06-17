print("===============程式描述========================")
print("= 程式名稱：ch7-5-1.py                        =")
print("= 程式目的：深度優先搜尋法(DFS)                =")
print("==============================================")
N=8                       #定義頂點總數 
Edge=10                   #定義邊的總數 
G=[[0 for i in range(8)] for j in range(8)] 
Gnode =[[1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [4, 8], [5, 8], [6, 8], [7, 8]];
Visited=[0 for i in range(8)]                #記錄已被拜訪過的節點 
row, column, i=0,0,0
#設定節點都尚未被拜訪
for i in range(0,N):
    Visited[i] = 0
    
#將二維陣列的內容轉換成相鄰陣列
R_node=0
#相鄰陣列預設為0
for row in range(0,N):
   for column in range(0,N):
      G[row][column]=0
  
#設定頂點的起點
for row in range(0,Edge):
    R_node = Gnode[row][0] - 1   
    for column in range(0,2):
      G[R_node][Gnode[row][column] - 1] = 1

#設定頂點的終點
for row in range(0,Edge):
    R_node = Gnode[row][1] - 1
    for column in range(0,2):
      G[R_node][Gnode[row][column] - 1] = 1

#對角線設定為0
for row in range(0,N):
    for column in range(0,N):
       if(row == column):
          G[row][column]=0

def Create_Graph():      #建立圖形 
  print("圖形的相鄰串列內容如下:\n");
  for row in range(0,N):
    for column in range(0,N):
        print("%3d" % G[row][column],end="")
    print()

def DFS(i):    #深度優先搜尋法(DFS)
  j=0
  Visited[i] = 1
  print("v%d  " % (i + 1),end="")
  for j in range(0,N):
    if(G[i][j] == 1):
      if (Visited[j]!=1):  #判斷是否已經被拜訪過
         DFS(j)
Create_Graph() #建立圖形 
print("=================輸出==================\n")         
print("深度優先搜尋法(DFS)拜訪頂點的順序為：\n")  #印出走訪過程 
DFS(0)                                       #呼叫深度優先搜尋法(DFS)