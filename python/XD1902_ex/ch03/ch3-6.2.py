print("===============程式描述========================")
print("= 程式名稱：ch3-6.2.py                        =")
print("= 程式目的：計算Fibonacci(費氏數)              =")
print("==============================================")
#遞迴函式名稱
def Fib(N):  
   if (N <=2):
     return 1
   else:
     return Fib(N-1) + Fib(N - 2) #函式自己又可以呼叫自己
N = int(input("請輸入費氏數值項次："))
Sum = Fib(N)            #呼叫遞迴函式
print("N=%2d 時的費氏數=%3d" %(N,Sum)) 