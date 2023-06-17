print("===============程式描述========================")
print("= 程式名稱：ch3-2.py                          =")
print("= 程式目的：使用堆疊進行push以及pop            =")
print("==============================================")
MaxNum=5           #定義堆疊大小
Stack=[0,0,0,0,0]  #以陣列Stack當作堆疊
Top =0
def menu():
    print("==============================================");
    print("=   1.push(加入)                             =");
    print("=   2.pop(取出)                              =");  
    print("=   3.結束                                   =");    
    print("==============================================");
#將資料加入堆疊
def Push():
    global Top            #Top紀錄目前堆疊頂端的索引值，初始值設為-1表示堆疊為空
    while True:
        item =input("請輸入你要push(加入)的資料：")
        if item=="": break
        if(Top == MaxNum-1):
          print("堆疊是滿的!")
        else:
          Top=Top+1
          Stack[Top] = item       

#取出堆疊資料
def Pop():
    global Top            #Top紀錄目前堆疊頂端的索引值，初始值設為-1表示堆疊為空
    strTmep=""
    while True:
     if(Top == -1): 
       print("堆疊是空的!")
     else:
         for i in range(Top,0,-1):    
           strTmep=strTmep + Stack[i]
         print("%s 是從堆疊彈pop(取出)的資料" % strTmep)
     input("請按任意鍵返回主選單") 
     break          
    
while True:
    menu()
    choice = int(input("請輸入您的選擇："))
    print()
    if choice==1:
        Push()          #將資料加入堆疊
    elif choice==2:
        Pop()           #取出堆疊資料
    elif choice==3:
         break     
print("程式執行完畢！")

