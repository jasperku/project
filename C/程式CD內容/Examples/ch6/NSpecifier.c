#include <stdio.h>

int main()
{
   int x=4;

   scanf("%*d %3d", &x);
   printf("[%*d]\n", 10,x);

   printf("This is a test for %%n.%n\n", &x);
   printf("This program has output %d charachters.\n", x);
}
