#include<stdio.h>

int main()
{
   int i,j,k;
   for(i=1;i<=5;i++)
   {
      for(j=1;j<=(5-i+1); j++)
      {
         printf(" ");
      }
      for(k=1;k<=(i*2-1); k++)
      {
         printf("*");
      }
      printf("\n");
   }
}
