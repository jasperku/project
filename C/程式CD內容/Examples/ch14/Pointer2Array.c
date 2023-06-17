#include <stdio.h>

#define ROW 3
#define COL 5

int main()
{
  int data[ROW][COL];
  int i, j;
  int (*p2a)[COL];

  for(i=0;i<ROW;i++)
    for(j=0;j<COL;j++)
      data[i][j]= i*COL+j;

  p2a=&data[0];

  printf("The values of the first row are ");
  for(i=0;i<COL;i++)
  {
    if(i==COL-1)
      printf("and %d.\n", (*p2a)[i]);
    else
      printf("%d, ", (*p2a)[i]);
  }
  printf("The values of the first column are ");
  for(i=0;i<ROW;i++)
  {
    if(i==ROW-1)
      printf("and %d.\n", *p2a[i]);
    else
      printf("%d, ", *p2a[i]);
  }
}
