#include <stdio.h>
#include "Toolbox.h"

int main()
{
    int data[10]={43, 23, 24, 9, 25, 47, 98, 12, 3, 77};
    printArray(data, 10);
    printf("The sum of this array is %d.\n", sumArray(data, 10));
}
