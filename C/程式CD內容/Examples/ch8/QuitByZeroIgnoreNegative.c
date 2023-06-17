#include<stdio.h>

int main()
{
   int n, sum=0;
   for(;;)
   {
      printf("Please input a number (0 for quit):");
      scanf("%d", &n);
      if(n==0)
         break;
      if(n<0)
         continue;
      sum+=n;
      // continue敘述使程式碼跳到了這裡
   }
   printf("sum=%d.\n", sum);
}
