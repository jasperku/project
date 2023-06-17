#include <stdio.h>

int main()
{
  float ping, mm;
  printf("How many ping?");
  scanf(" %f", &ping);
  mm=ping*3.3058;
  printf("%f ping = %f mm \n", ping, mm);
}