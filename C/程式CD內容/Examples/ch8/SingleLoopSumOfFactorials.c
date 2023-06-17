#include<stdio.h>

int main()
{
   int i, factorial=1, sum=0;

   for(i=1;i<=10;i++)
   {
      factorial*=i;
      sum += factorial;
   }
   printf("sum=%d.\n", sum);
}
