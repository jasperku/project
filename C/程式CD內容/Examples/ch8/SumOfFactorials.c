#include<stdio.h>

int main()
{
   int i,j,factorial,sum=0;

   for(i=1;i<=10;i++)
   {
      factorial=1;
      for(j=2; j<=i; j++)
      {
         factorial*=j;
      }
      sum += factorial;
   }
   printf("sum=%d.\n", sum);
}
