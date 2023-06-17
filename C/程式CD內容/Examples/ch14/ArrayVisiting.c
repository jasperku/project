#include <stdio.h>

int main()
{
  int data[5]={10, 20, 30, 40, 50};
  int i;
  int *p;

  p=&data[0];
  for(i=0;i<5;i++)
    printf("data[%d]=*(p+%d)=%d \n", i, i, *(p+i));
}
