#include <stdio.h>

int main()
{
  int size;
  int data[] = { 3, 4, 5, 6, 7, 8 };
  
  size = sizeof(data)/sizeof(int);
  
  printf("The array size is %d.\n", size);
}
