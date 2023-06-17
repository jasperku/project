#include <stdio.h>

int main()
{
  char str[] = "Hello World";
  printf("[%s]\n", str);
  printf("[%5s]\n", str);
  printf("[%15s]\n", str);
  printf("[%-15s]\n", str);
  printf("[%10.5s]\n", str);
  printf("[%-10.5s]\n", str);
  printf("[%3.5s]\n", str);
  
  puts(str);
}
