#include <stdio.h>
#define Size 5

int main()
{
  int data[Size]={10, 20, 30, 40, 50};
  int *p;

  p=&data[0];
  for(p=&data[0]; p<&data[Size]; p++)
    printf("p=%p *p=%d \n", p, *p);
}
