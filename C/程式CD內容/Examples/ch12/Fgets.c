#include <stdio.h>

#define LEN 10

int main()
{
  char name[LEN+1];
  printf("Please input your name:");
  fgets(name, 10, stdin); // 從stdin讀取不超過10個字元至name字串
  printf("Your name is %s.\n", name);
}
