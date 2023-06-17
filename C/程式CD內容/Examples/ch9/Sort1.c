#include <stdio.h>
int main()
{
  int data[10]={ 10, 33, 13, 60, 65, 25, 100, 34, 99, 0};
  int i, j;
  int maxIndex;

  for(i=0;i< 10;i++)
  {
    maxIndex=0;
    for(j=1;j<10;j++)
    {
      if(data[maxIndex] < data[j])
      {
        maxIndex = j;
      }
    }
    printf("%d ",data[maxIndex]);
    data[maxIndex]=(-1);
  }
  printf("\n");  
}
