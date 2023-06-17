#include <stdio.h>

struct point
{
  int x,y;
};

typedef struct point Point;

void showPoint(Point p)
{
  printf("(%d,%d)\n", p.x, p.y);
}

int main()
{
  Point p1;
  Point p2 = {5,5};

  p1=p2;
  p1.x+=p1.y+=10;

  showPoint(p1);
  showPoint(p2);
}
