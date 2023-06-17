#include<stdio.h>

int main()
{
   int i;

   for(i=1;i<=100;i++)
   {
      if( ((i%7) == 0) || ((i%13) == 0))
      {
         printf("%d ", i);
      }
   }
}
