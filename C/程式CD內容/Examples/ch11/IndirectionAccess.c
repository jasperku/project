#include <stdio.h>

int main()
{
  int *p=NULL;
  int x=38;
  int y=27;

  printf("The memory address of p is %p.\n", &p);
  printf("The memory address of x is %p.\n", &x);
  printf("The memory address of y is %p.\n", &y);
  
  p=&x;
  printf("Let p=&x, the value of p is %p.\n", p);
  printf("The value stored in %p is %d.\n", p, *p);
  p=&y;
  printf("Let p=&y, the value of p is %p.\n", p);
  printf("The value stored in %p is %d.\n", p, *p);
}
