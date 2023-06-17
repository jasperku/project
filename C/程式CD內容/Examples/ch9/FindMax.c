#include <stdio.h>
int main()
{
  int data[10]={ 10, 33, 13, 60, 65, 25, 100, 34, 99, 0};
  int i;
  int maxIndex;

  maxIndex=0;
  for(i=1;i<10;i++)
  {
    if(data[maxIndex] < data[i])
    {
        maxIndex = i;
    }
  }
  printf("Max value is %d\n",data[maxIndex]);
}
