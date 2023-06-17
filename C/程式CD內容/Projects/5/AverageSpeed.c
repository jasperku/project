#include <stdio.h>

int main()
{
int h, m, s;
float dist, avgSpeed;

    scanf("%*c%*c%*c%d%*c%d%*c%d", &h, &m, &s);
    scanf(" %*c%*c%*c%f", &dist);

    avgSpeed=dist/(float)(h+(m/60.0)+(s/3600.0));

    printf("Duration:%.2d:%.2d:%.2d(HH:MM:SS)\n", h, m, s);
    printf("Distance:%7.2fKM\n", dist);
    printf("Average Speed: %2.2fKM/H\n", avgSpeed);
}
