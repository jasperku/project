print("===============程式描述========================")
print("= 程式名稱：ch4-2.py                         =")
print("= 程式目的：使用佇列進行Enqueue               =")
print("==============================================")
MaxNum=5           #定義佇列大小
Queue=[0,0,0,0,0]  #以陣列Queue當作佇列
Rear =0
Front=0
def menu():
    print("==============================================");
    print("=   1.Enqueue(加入)                          =");
    print("=   2.Showqueue(顯示)                        =");  
    print("=   3.結束                                   =");    
    print("==============================================");
#將資料加入佇列
def Enqueue():
    global Rear
    global Front
    while True:
        item =input("請輸入你要加入的資料：")
        if item=="": break
        if(Rear == MaxNum-1):
          print("佇列是滿的!")
        else:
          Rear=Rear+1
          Queue[Rear] = item       

#列印目前佇列的內容
def Showqueue():
    global Rear
    global Front
    strTmep=""
    while True:
     if(Front == Rear): 
       print("佇列是空的!")
     else:      
        for i in range(Front+1,Rear+1,1):    
           strTmep=strTmep + Queue[i]
        print("%s 是從佇列取出的資料" % strTmep)
     input("請按任意鍵返回主選單") 
     break          
    
while True:
    menu()
    choice = int(input("請輸入您的選擇："))
    print()
    if choice==1:
        Enqueue()          #將資料加入佇列
    elif choice==2:
        Showqueue()      #取出佇列資料
    elif choice==3:
         break     
print("程式執行完畢！")

