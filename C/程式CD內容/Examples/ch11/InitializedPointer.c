#include <stdio.h>

int main()
{
  int *p;
  
  printf("The memory address of p is %p.\n", &p);
  printf("The value of p is %p.\n", p);
  p=NULL;
  printf("Let p=NULL, the value of p is %p.\n", p);
  p=0;
  printf("Let p=0, the value of p is %p.\n", p);
}
