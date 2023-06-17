#include<stdio.h>

int main()
{
   int last1=1, last2=1, current, i;

   printf("%d %d ", last2, last1);
   for(i=3; i<=20;i++)
   {
      current=last1+last2;
      printf("%d ", current);
      last2=last1;
      last1=current;
   }
}
