#include <stdio.h>

int main()
{
   // Declaration Section:
   int total;
   
   // Input Section:
   printf("Please input the total:");
   scanf("%d", &total);
   
   // Process Section:
   if(total > 5000 )
   {
      total-=500;
   }
   
   // Output Section: 
   printf("Total=%d\n", total); 
}
