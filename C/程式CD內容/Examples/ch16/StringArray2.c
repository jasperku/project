#include <stdio.h>
#include <stdlib.h>
#include <string.h>
 
#define numString 10
#define LEN 20
 
int main()
{
  char **strs;
  int i;
 
  strs = malloc(numString*sizeof(void *));
  for(i=0;i<numString;i++)
    *(strs+i) = malloc(LEN+1);
 
  for(i=0;i<numString;i++)
  {
    printf("String %d = ", i+1);
    scanf(" %[^\n]", *(strs+i));
  }
 
  for(i=0;i<numString;i++)
    puts(*(strs+i));
}
