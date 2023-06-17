#include <stdio.h>
#include <float.h>

int main()
{
  printf("A float number takes %lu bits of memory.\n", 
         sizeof(float)*8);
  printf("A double number takes %lu bits of memory.\n", 
         sizeof(double)*8);
  printf("A long double number takes %lu bits of memory.\n",
         sizeof(long double)*8);
}
