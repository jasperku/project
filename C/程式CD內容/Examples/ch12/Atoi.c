#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    printf("%d\n", atoi("123"));
    printf("%d\n", atoi("45.678"));
    printf("%d\n", atoi("abc"));
    printf("%d\n", atoi("5+2"));
}
