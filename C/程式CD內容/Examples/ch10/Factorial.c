#include <stdio.h>

int factorial( int n)
{
   int result=1, i;

   if((n==0)||(n==1))
      return 1;
   else if (n>1)
   {
      for(i=2;i<=n;i++)
      {
         result*=i;
      }
      return result;
   }
   else
      return (-1);
}

int main()
{
   int N;
   printf("Please input a number N: ");
   scanf(" %d", &N);
   printf("N!=%d\n", factorial(N) );
}
