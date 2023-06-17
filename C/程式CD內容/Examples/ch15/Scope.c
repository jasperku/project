#include <stdio.h>
int g; // global variable
void foo(int a, int b)
{                    
   int x=1, y=2, z;    //  local variables: a, b, x, y, z
   z = a+b;
   printf("x=%d y=%d z=%d g=%d \n", x, y, z, g); // x=1 y=2 z=15 g=8;
}

int main()
{               
   int x=3, y=5;
   g = x+y;
   printf("x=%d y=%d g=%d\n", x, y, g); // x=3 y=5 g=8;

   {           
      int z;   
      z = x+y;                 
      printf("x=%d y=%d z=%d g=%d\n", x, y, z, g); // x=3 y=5 z=8 g=8;
   }           
   foo(6, 9);
}
