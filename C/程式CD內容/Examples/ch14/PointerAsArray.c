#include <stdio.h>
#define Size 5

int main()
{
  int data[Size]={10, 20, 30, 40, 50};
  int *p = data;
  int i;

  for(i=0;i<Size;i++)
    printf("p[%d]=%d\n", i, p[i]);
}
