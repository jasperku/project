#include <stdio.h>
void foo()
{
  static int i=1;
  printf("i=%d\n", i++);
}

int main()
{
  int i;
  for(i=0;i<10;i++)
    foo();
}
