#include <stdio.h>
#include <string.h>
 
int main()
{
  char str[]="Hello";
  char *p;
  int i;
 
  printf("str at %p\n", str);
 
  for(i=0;i<strlen(str);i++)
  {
    printf("str[%d] at %p\n", i, &str[i]);
  }
 
  p = str;
 
  for(i=0;i<strlen(str);i++)
  {
    printf("*(p+%d)=str[%d]=%c at %p\n", i, i, *(p+i), p+i);
  }
 
  str[0]='h';
  *(p+3)='L';
 
  puts(str);
  puts(p);
}
