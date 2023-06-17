#include <stdio.h>

struct point
{
  int x,y;
};

typedef struct point Point;

int main()
{
  Point p1;
  Point p2 = {5,5};

  p1=p2;
  p1.x+=p1.y+=10;

  printf("p1=(%d,%d) p2=(%d,%d)\n", p1.x, p1.y, p2.x, p2.y);
}
