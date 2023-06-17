#include <stdio.h>
#include <string.h>
 
int main()
{
  char str[]="Hello";
  char *p;
 
  p = str;
 
  p[0]='H';
  *(str+3) = 'L';
 
  puts(str);
  puts(p);
}
