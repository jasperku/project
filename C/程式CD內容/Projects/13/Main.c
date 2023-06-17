#include <stdio.h>
#include "Toolbox.h"

int main()
{
    int data[]={4,2,1,5,3};
    printArray(data,5);
    sortArray(data, 5, Increasing);
    printArray(data, 5);
    sortArray(data, 5, Decreasing);
    printArray(data, 5);
}