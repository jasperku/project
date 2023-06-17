#include <stdio.h>

int main()
{
  int x;
  short int y;
  long int z;

  printf("Please input an int:");
  scanf("%d",&x);

  printf("%d_decimal =  %o_octal = %x_hexadecimal.\n", x, x, x);

  printf("Please input a short int in octal:");
  scanf("%ho",&y);
  printf("%hd_decimal =  %ho_octal = %hx_hexadecimal.\n", y, y, y);

  printf("Please input a long int in hexadecimal:");
  scanf("%lx",&z);
  printf("%ld_decimal =  %lo_octal = %lx_hexadecimal.\n", z, z, z);
}
