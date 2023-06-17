#include <stdio.h>
#include "Toolbox.h"

void newline()
{
  printf("\n");
}

void sortArray(int data[], int size, int order)
{
  int i, j, temp;
  
  for(i=0;i<size-1;i++)
  {
    for(j=0;j<size-i-1;j++)
    {    
      if((data[j]>data[j+1])&&(order==Increasing))
      {
        temp=data[j];
        data[j]=data[j+1];
        data[j+1]=temp;
      }
      else if((data[j]<data[j+1])&&(order==Decreasing))
      {
        temp=data[j];
        data[j]=data[j+1];
        data[j+1]=temp;
      }
    }
  }
}

void printArray(int data[], int size)
{
  int i;
  for(i=0;i<size;i++)
  {
    printf("%d ", data[i]);
  }
  newline();
}
