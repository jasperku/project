#include<stdio.h>

int main()
{
   int i;
   float amount=1000.0;
   for(i=1; i<=12;i++)
   {
      amount=amount*1.03;
   }
   printf("%f ", amount);
}
