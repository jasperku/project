#include <stdio.h>

#define LEN 20

int main()
{
  char name[LEN + 1];
  printf("Please input your name:");
  gets(name);
  printf("Your name is %s.\n", name);
}