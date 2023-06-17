#include <stdio.h>

int main()
{
  int vcode;
  scanf(" %d", &vcode);
  switch(vcode)
  {
    case 0:
    case 1:
    case 2:
    case 3:
    case 4:
            printf("non-citizen\n");
            break;
    case 5:
    case 6:
    case 7:
            printf("level 2 citizen\n");
            break;
    default:
            printf("level 1 citizen\n");
  }
}