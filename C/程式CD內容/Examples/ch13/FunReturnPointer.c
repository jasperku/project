#include <stdio.h>

struct point
{
  int x,y;
};

typedef struct point Point;

Point * addPoint(Point *p1, Point p2)
{
  p1->x = p1->x + p2.x;
  p1->y = p1->y + p2.y;
  return p1;
}

void showPoint(Point p)
{
  printf("(%d,%d)\n", p.x, p.y);
}

int main()
{
  Point *p1;
  Point p2 = {5,5};
  Point *p3;

  p1=&p2;
  p1->x += p1->y+=10;

  showPoint(*p1);
  showPoint(p2);

  p3=addPoint(p1,p2);
  showPoint(*p1);
  showPoint(*p3);
}
