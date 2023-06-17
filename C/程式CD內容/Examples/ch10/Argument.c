#include <stdio.h>

int sum( int x, int y )
{
   return x+y;
}

int main()
{
   int i=2, j=4, k=6;

   //使用=將函式的傳回值指定給變數i
   i = sum(10, 30);
   printf("10+30 = %d\n", i);

   // 直接把函式的傳回值當成一般的值，並傳給printf做為輸入
   printf("5+6 = %d\n", sum(5,6));

   // 引數的部份也可以為變數
   printf("5+j = %d\n", sum(5,j));

   // 傳回值可做為運算式的一部份
   printf("5+j+k = %d\n", 5+sum(j,k) );

   // 引數的部份也可以為運算式
   printf("5+j+k = %d\n", sum( 5 , (j+k) ) );

   // 引數的部份也可以為另一個函式呼叫
   printf("5+j+k = %d\n", sum( 5 , sum(j,k) ) );
}
