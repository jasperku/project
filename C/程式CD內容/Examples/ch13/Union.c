#include <stdio.h>

union
{
  int i;
  double d;
} data;

int main()
{
  data.i=5;
  printf("data.i=%d data.d=%f sizeof(data)=%ld\n", data.i, data.d, sizeof(data) );

  data.d=10.5;
  printf("data.i=%d data.d=%f sizeof(data)=%ld\n", data.i, data.d, sizeof(data) );
}
