#include <stdio.h>

int main()
{
  char d1, d2, d3, d4, d5, d6, d7, d8, d9;
  int vcode;
  
  scanf("%c%c%c%c%c%c%c%c%c", &d1, &d2, &d3, &d4, &d5, &d6, &d7, &d8, &d9);
  d1-=48;
  d2-=48;
  d3-=48;
  d4-=48;
  d5-=48;
  d6-=48;
  d7-=48;
  d8-=48;
  d9-=48;  

  vcode=(((d1+d3+d5+d7)*5+(d2+d4+d6+d8))-7)%10;
  printf("%d\n", vcode);
}
