#include <stdio.h>
#define Size 10

int main()
{
  int data[Size]={321, 432, 343, 44, 55, 66, 711, 84, 19, 610};
 
  int i;
  int *p;
  int max, max2;
 
  max = *(p = &data[0]);
  for( ; p<&data[Size]; p++)
     max = (max < *p) ? *p : max;
  printf("max = %d \n", max);
}
