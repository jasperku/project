#include <stdio.h>
#include <stdlib.h>

struct vstring
{
  int len;
  char chars[];
};
 
int main()
{
  struct vstring *str = malloc(sizeof(struct vstring)+10);
  str->len=10;
  printf("Please input a string:");
  fgets(str->chars, str->len, stdin);
  printf("%s", str->chars);  
}
