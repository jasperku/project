#include <stdio.h>

struct
{
  int x;
  int y;
} p1, p2;

int main()
{
  printf("The size of an int is %ld bytes.\n", sizeof(int));
  printf("The size of p1 is %ld bytes.\n", sizeof(p1));
  printf("The size of p2 is %ld bytes.\n", sizeof(p2));  
}
