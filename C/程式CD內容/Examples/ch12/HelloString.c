#include <stdio.h>

int main()
{
  char *p;
  char *q;
  int i;

  p="Hello";
  q=p;

  printf("%s\n", p); // %s為字串的format specifier 

  for(i=0;i<6;i++)
  {
    printf("%c = %d at %p\n", *q, *q, q);
    q++;
  }
  return 0;
}
