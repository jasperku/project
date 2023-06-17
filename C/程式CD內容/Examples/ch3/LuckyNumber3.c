// Header File Section
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
// Variable Declaration Section
   int lucky;
   int x;
   int min;
   int max;
   
// Input Section
   printf("Please input the minimal number: ");
   scanf("%d", &min);
   printf("Please input the maximal number: ");
   scanf("%d", &max);

// Process Section
   srand(time(NULL));
   x = min+rand()%(max-min+1);
   lucky = x;

// Output Section
   printf("Your lucky number is %d!\n", lucky);
}
