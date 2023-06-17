#include <stdio.h>

int factorial( int n)
{
   if((n==0)||(n==1))
      return 1;
   else if(n>1)
   {
      return n*factorial(n-1);
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
