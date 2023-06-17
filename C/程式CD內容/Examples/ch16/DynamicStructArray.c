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
 
#define LEN 5
 
int main()
{
  Point *ps = malloc(sizeof(Point)*LEN);
  int i;
 
  for(i=0;i<LEN;i++)
  {
    ps[i].x=i;
    ps[i].y=i;
    showPoint(ps[i]);
    showPoint(*(ps+i));
  }
}
