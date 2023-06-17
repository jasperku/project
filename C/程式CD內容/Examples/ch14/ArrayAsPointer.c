#include <stdio.h>
#define Size 5

int main()
{
  int data[Size]={10, 20, 30, 40, 50};
  int i;

  for(i=0;i<Size;i++)
    printf("(data+%d)=%p *(data+%d)=%d\n", i, data+i, i, *(data+i) );

  printf("\n");

  int *p;
  for(p=data;p<data+Size;p++)
    printf("p=%p *p=%d \n", p, *p);
}
