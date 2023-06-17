#include <stdio.h>

int main()
{
   int data[5]={10, 20, 30, 40, 50};
   int i;
   printf("The array data is located at %p.\n", data);
   for(i=0;i<5;i++)
   {
      printf("data[%d] is located at %p. \n", i, &data[i]);
   }
}
