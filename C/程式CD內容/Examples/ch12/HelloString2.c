#include <stdio.h>

int main()
{
  int i;

  for(i=0;i<6;i++)
  {
    printf("%c = %d at %p\n", "Hello"[i], "Hello"[i], &"Hello"[i]);
  }
  return 0;
}
