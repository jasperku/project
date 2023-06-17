#include <stdio.h>

void foo();

int main()
{
   foo();
   printf("This is main function.\n");
}

void foo()
{
   printf("This is foo.\n");
}
