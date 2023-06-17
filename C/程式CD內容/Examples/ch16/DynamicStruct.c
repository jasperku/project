#include <stdio.h>
#include <stdlib.h>
 
typedef struct
{
  int x;
  int y;
} Point;
 
void showPoint(Point p)
{
  printf("(%d,%d)\n", p.x, p.y);
}
 
int main()
{
  Point *p1 = malloc(sizeof(Point));
  p1->x=5;
  p1->y=10;
  showPoint(*p1);
}
