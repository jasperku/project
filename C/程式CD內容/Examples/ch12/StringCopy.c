#include <stdio.h>
#include <string.h>

int main()
{
  char str1[20]={}, *str2=NULL;

  strcpy(str1, "abcd");
  printf("%s\n", str1);
  str2=strcpy(str1, "hello");
  printf("%s\n", str2);
}
