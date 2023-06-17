#include <stdio.h>

#define N 10

int main()
{
  int data[N]={ 10, 33, 13, 60, 65, 25, 100, 34, 99, 0};
  int i, j, temp;

  for(i=0;i<N-1;i++)
  {
    for(j=0;j<N-i-1;j++)
    {
      if(data[j] > data[j+1])
      {
        temp=data[j];
        data[j]=data[j+1];
        data[j+1]=temp;
      }
    }
  }
  for(i=0;i<N;i++)
    printf("%d ", data[i]);
  printf("\n");
}