#include <stdio.h>

int main()
{
  char strA[]="Hello";
  char *strP = "World";

  printf("%s %s\n", strA, strP);

  strA[0]='h';
  *strP='w';

  printf("%s %s\n", strA, strP);
}
