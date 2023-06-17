#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

void showHelp()
{
  printf("l: list all numbers.\n");
  printf("i: increasing space.\n");
  printf("d: decreasing space.\n");
  printf("q: quit.\n");
}

void showAllNumbers(int nums[], int size)
{
  int i;
  if(size>=1)
  {
    printf("%d",nums[0]); 
  }
  for(i=1;i<size;i++)
  {
    printf("->%d", nums[i]);
  }
  printf("\n");
}

int increasingSpace(int nums[], int size)
{
  int i, newSize;
  newSize=size*2;
  nums = realloc(nums, sizeof(int)*size*2);
  for(i=size;i<newSize;i++)
  {
    nums[i]=rand()%100+1;
  }
  return newSize;
}

int decreasingSpace(int nums[], int size)
{
  if(size<=10)
  {
    printf("Can\'t resize it!\n");
    return size;
  }
  else
  {
    nums = realloc(nums, sizeof(int)*(size/2));
    return size/2;  
  }
}

int main()
{
  int *nums;
  int quit =0;
  char cmd;
  int size=10;
  int i;
  
  nums=malloc(sizeof(int)*size);
  srand(time(NULL));
  for(i=0;i<size;i++)
  {
    nums[i]=rand()%100+1;
  }
  
  while(!quit)
  {
    printf("command?");
    cmd=getchar();
    switch(cmd)
    {
      case 'h':
        showHelp();
        getchar();
        break;
      case 'l':
        showAllNumbers(nums, size);
        getchar();
        break;
      case 'i':
        size=increasingSpace(nums, size);
        getchar();
        break;
      case 'd':
        size=decreasingSpace(nums, size);
        getchar();
        break;
      case 'q':
        quit=1;
        break;
    }
  }
}
