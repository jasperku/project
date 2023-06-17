#include <stdio.h>

char *getMessage(int i)
{
  if(i==0)
    return "Welcome!";
  else
    return "Hello!";
}

int main()
{
  char *str;
  printf("%s\n", getMessage(0));

  str=getMessage(1);
  printf("%s\n", str);
}
