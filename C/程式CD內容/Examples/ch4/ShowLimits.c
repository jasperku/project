#include <stdio.h>
#include <limits.h>

int main()
{
   printf("short int [%d, %d]\n",SHRT_MIN, SHRT_MAX);
   printf("int [%d, %d]\n", INT_MIN, INT_MAX);
   printf("long int [%ld, %ld]\n", LONG_MIN, LONG_MAX);
   printf("unsigned short int [0, %u]\n", USHRT_MAX);
   printf("unsigned int [0, %u]\n", UINT_MAX);
   printf("unsigned long int [0, %lu]\n", ULONG_MAX);
}
