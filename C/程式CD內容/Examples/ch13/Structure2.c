#include <stdio.h>

struct
{
  int   productNum;
  char *productName;
  float price;
  int   quantity;
  float discount;
} mfone;

int main()
{
  printf("The size of an int is %ld bytes.\n", sizeof(int));
  printf("The size of a string pointer is %ld bytes.\n", sizeof(char *));
  printf("The size of a float is %ld bytes.\n", sizeof(float));
  printf("The size of mfone is %ld bytes.\n", sizeof(mfone));
}
