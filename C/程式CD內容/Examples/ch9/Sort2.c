#include <stdio.h>

int main()
{
  int data[10]={ 10, 33, 13, 60, 65, 25, 100, 34, 99, 0};
  int flag[10] ={0};
  int i, j;
  int max, maxIndex;
  
  for(i=0;i< 10;i++)
  {
    maxIndex=0;    
    for(j=0;j<10;j++)
    {
      if(flag[j]!=1)
      {
        maxIndex=j;
        break;
      }
    }
    
    for(j=1;j<10;j++)
    {
      if((data[maxIndex] < data[j])&&(flag[j]!=1))
      {
        maxIndex = j;
      }
    }
    printf("%d ",data[maxIndex]);
    flag[maxIndex]= 1;
  }
  printf("\n");
}