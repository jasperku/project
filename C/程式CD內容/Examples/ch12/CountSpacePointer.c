#include <stdio.h>

int countSpace(const char *s)
{
  int count=0;

  printf("the argument s at %p.\n", s);

  for(;*s!='\0';s++)
  {
    if(*s==' ')
    {
      count++;
    }
  }
  return count;
}

int main()
{
  char str[]="This is a test.";

  printf("%s at %p.\n", str, str);
  printf("There are %d space(s) in the string.\n", countSpace(str) );
}
