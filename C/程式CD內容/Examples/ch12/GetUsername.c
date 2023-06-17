#include <stdio.h>
#define LEN 10

int main()
{
  char name[LEN + 1];

  printf("Please input your name:");
  scanf("%s", name);
  printf("Your name is %s.\n", name);
}
