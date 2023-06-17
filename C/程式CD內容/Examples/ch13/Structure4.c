#include <stdio.h>
#include <string.h>

struct
{
  int   productNum;
  float discount;
  char productName[20];
  float price;
  int   quantity;
} mfone = {12, 0.5, "mPhone 6s", 15000, 100},
  mfone2;  

int main()
{
  printf("The size of mfone is %ld bytes.\n", sizeof(mfone));
  mfone2=mfone;
  printf("%s\n%s\n", mfone.productName, mfone2.productName);
  
  strcpy(mfone.productName, "New Model");
  printf("%s\n%s\n", mfone.productName, mfone2.productName);
}
