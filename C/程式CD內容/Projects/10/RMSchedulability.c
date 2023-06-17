#include <stdio.h>
#include <math.h>

int main()
{
  int n,i,T,C;
  double U=0.0, upperBound=0.0;
  scanf("%d", &n);
  
  for(i=0;i<n;i++)
  {
    scanf("%d:%d:%*d", &T, &C);
    U += (C/(double)T);
  }
  upperBound=n*(pow(2, 1/(double)n)-1);
  printf("The utilization of the %d tasks is %f.\n", n, U);
  printf("Since %f ", U);
  if(U<=upperBound)
    printf("<=");
  else
    printf(">");
  printf(" n(2^(1/n)-1)=%d(2^(1/%d)=%f,\n", n, n, upperBound);  
  printf("these %d tasks are ", n);
  if(U<=upperBound)
    printf("schedulable by RMS.\n");
  else
    printf("unschedulable by RMS.\n");
}