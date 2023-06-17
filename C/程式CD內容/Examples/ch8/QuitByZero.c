#include<stdio.h>

int main()
{
   int n, sum=0;

   while(1) //或是 for(; ;)也是一樣的意思
   {
      printf("Please input a number (0 for quit):");
      scanf("%d", &n);
      if(n==0)
         break;
      sum+=n;
   }
   printf("sum=%d.\n", sum);
}
