#include <stdio.h>

int main()
{
  int num10;
  printf("Please input an integer in decimal:");
  scanf("%d", &num10);
  printf("(%d)_10=(0%o)_8=(0x%x)_16\n",num10, num10, num10); 
}