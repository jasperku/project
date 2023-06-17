#include <stdio.h>

int main()
{
   int deptID;

   scanf("%1d", &deptID);

   if( deptID == 1 )
   {
      printf("Computer Science and Information Engineering\n"); 
      printf("Phone: (08)7238700 ext.21201.\n");
   }
   else if( deptID == 2 )
   {
      printf("Computer and Communications\n");
      printf("Phone: (08)7238700 ext.21303.\n");
   }
   else if( deptID == 3 )
   {
      printf("Computer and Multimedia\n");
      printf("Phone: (08)7238700 ext.21701.\n");
   }
   else
   {
      printf("The value of deptID %d is invalid!\n", deptID);
   }
}
