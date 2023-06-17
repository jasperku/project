#include <stdio.h>

int main()
{
   int x;
   printf("Please input a number (no more than 3 digits):___\b\b\b");
   scanf("%3d", &x);
   printf("Your input is %d.\n", x);
}
