#include <stdio.h>
#define Size 10

int main()
{
  int data[Size]={1,2,3,4,5,6,7,8,9,10};
  int i;
  int *p;
  int sum=0,sum2=0;
 
  for(p=&data[0];p<&data[Size];p++)
  {
    sum += *p;
  }
  printf("sum = %d\n", sum);
 
  while(p>(int *)&data)
  {
    sum2+=*--p;
  }
  printf("sum2 = %d\n", sum2);
}
