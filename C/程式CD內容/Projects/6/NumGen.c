#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
  int x1, x2, x3, x4, x5;
  
  srand(time(NULL));
  x1 = 1+rand()%10;
  x2 = 1+rand()%10;
  x3 = 1+rand()%10;
  x4 = 1+rand()%10;
  x5 = 1+rand()%10;
  
  printf("%d %d %d %d %d\n", x1, x2, x3, x4, x5);
}