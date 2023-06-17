#include <stdio.h>
#include <stdlib.h>
#include <math.h>
 
int maximum(int d[], int n)
{ 
  int max=d[0];
  int i;
 
  for(i=1;i<n;i++)
    if(max<d[i])
      max=d[i];
  return max;
} 
 
int minimum(int d[], int n)
{ 
  int min=d[0];
  int i;
 
  for(i=1;i<n;i++)
    if(min>d[i])
      min=d[i];
  return min;
} 
 
int median(int d[], int n)
{ 
  double average=0.0;
  int i,med;
  double temp;
 
  for(i=0;i<n;i++)
  {
    average+=d[i];
  }
  average/=n;
 
  med=d[0];
  for(i=1;i<n;i++)
    if(fabs(med-average) > fabs(d[i]-average))
      med=d[i];
 
  return med;
} 
 
int functionPicker( int (*func)(int d[], int s), int data[], int size)
{ 
  return (*func)(data,size);
} 
 
int main()
{ 
  int data[10] = { 113, 345, 23, 75, 923, 634, 632, 134, 232, 98 };
  int num;
 
  num = functionPicker(maximum, data, 10);
  printf("The maximum is %d.\n", num);
  num = functionPicker(minimum, data, 10);
  printf("The minimum is %d.\n", num);
  num = functionPicker(median, data, 10);
  printf("The median is %d.\n", num);
}
