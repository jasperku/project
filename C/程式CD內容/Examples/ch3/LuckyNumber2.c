// header file section
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
   // variable declaration section
	 int lucky;
     int x;

   // input section
   
   // process section
	 srand(time(NULL));
	 x=rand();
	 lucky = x % 10;

   // output section
	 printf("Your lucky number is %d!\n", lucky);
}
