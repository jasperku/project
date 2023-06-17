#include <stdio.h>
int main()
{
   int i=5, sum=0;
   while(i--, sum+=i, i>0);
   printf("sum=%d\n", sum);
}
