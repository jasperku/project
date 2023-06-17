#include <stdio.h>
 
int main()
{
   int x,y;
   char c;
 
   y = scanf("%d %c", &x, &c);
 
   x = printf("The number of input data is %d.\n", y);
 
   printf("The above line has %d characters.\n", x);
}
