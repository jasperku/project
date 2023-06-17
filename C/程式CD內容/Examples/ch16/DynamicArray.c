#include <stdio.h>
#include <stdlib.h>

void showArray(int *p, int n)
{
  int i;
  for(i=0;i<n;i++)
    printf("%d ", p[i]);
  printf("\n");
}
 
int main()
{
  int *data;
  int size, i;
 
  printf("Array Size=? ");
  scanf(" %d", &size);
 
  data = malloc(size*sizeof(int));
 
  for(i=0;i<size;i++)
    data[i]=i;
      
  showArray(data, size);
 
  // add 10 more numbers
  data = realloc(data, (size+10)*sizeof(int));
  for(i=0;i<size+10;i++)
    data[i]=i;

  showArray(data, size+10);
 
  // remove last 5 numbers
  data = realloc(data, (size+5)*sizeof(int));

  showArray(data, size+10-5); 
}
