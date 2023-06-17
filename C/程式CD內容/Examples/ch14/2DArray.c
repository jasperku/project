#include <stdio.h>
 
#define ROW 3
#define COL 5
 
int main()
{
  int data[ROW][COL];
  int i, j;
 
  for(i=0;i<ROW;i++)
    for(j=0;j<COL;j++)
      data[i][j]= i*COL+j;

  for(i=0;i<ROW;i++)
  {
    for(j=0;j<COL;j++)
    {
      if(j>0)
        printf(", ");
      printf("%3d", data[i][j]);
    }
    printf("\n");
  }
}
