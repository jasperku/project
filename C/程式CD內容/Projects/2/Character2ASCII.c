#include <stdio.h>

int main()
{
  char c;
  printf("Please input a character:");
  scanf("%c", &c);
  printf("%c's ASCII code is (%d)_10 or (0x%x)_16.\n",c, c, c); 
}