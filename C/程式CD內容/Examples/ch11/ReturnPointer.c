#include <stdio.h>

int *max(int *a, int *b)
{
  if(*a > *b)
    return a;
  else
    return b;
}

int main()
{
  int x, y;
  int *p;

  scanf(" %d %d", &x, &y);
  p = max(&x, &y);
  printf("The maximum value is %d.\n", *p);

  *max(&x, &y)=100;
  printf("The values of x and y are %d and %d.\n", x, y);
}
