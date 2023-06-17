#include <stdio.h>
#define Size 10

int main()
{
  int data[Size]={3451,25,763,3454,675,256,37,842,3439,510};
 
  int *p, i;

  for(i=0;i<Size-1;i++)
    for(p=&data[0]; p<&data[Size-i-1]; p++) 
      if(*p<*(p+1))
      {
        int temp = *p;
        *p = *(p+1);
        *(p+1) = temp;
      }
 
  for(p=&data[0];p<&data[Size];p++)
    printf("%d \n", *p); 
}
