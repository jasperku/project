#include <stdio.h>
#include <stdlib.h>
 
int main()
{
  int **data;
  int Row, Col;
  int i,j;
 
  Row=3;
  Col=2;
 
  data = malloc(sizeof(int *)*Row);
  for(i=0;i<Row;i++)
    data[i] = malloc(Col*sizeof(int));
 
  for(i=0;i<Row;i++)
    for(j=0;j<Col;j++)
      data[i][j]=i*Col+(j+1);
 
  for(i=0;i<Row;i++)
  {
    for(j=0;j<Col;j++)
      printf("%d ", data[i][j]);
    printf("\n");
  }
}
