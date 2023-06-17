#include <stdio.h>
 
inline int foo(int x, int y)
{
    return x+y;
}
 
int main()
{ 
  printf("%d\n", foo(3,5));
}
