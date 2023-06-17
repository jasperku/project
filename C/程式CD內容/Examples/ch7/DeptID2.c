#include <stdio.h>

int main()
{
  int deptID;

  scanf("%1d", &deptID);

  switch (deptID )
  {
     case 1:
            printf("Computer Science and Information Engineering\n"); 
            printf("Phone: (08)7238700 ext.21201.\n");
            break;
     case 2:
            printf("Computer and Communications\n");
            printf("Phone: (08)7238700 ext.21303.\n");
            break;
     case 3:
            printf("Computer and Multimedia\n");
            printf("Phone: (08)7238700 ext.21701.\n");
            break;
     default: 
            printf("The value of deptID %d is invalid!\n", deptID);
  }
}
