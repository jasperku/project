#include <stdio.h>
#include "Tools.h"

int main()
{
    char cmd;
    while((cmd=getCommand())!='q')
    {
        showCommand(cmd);
        newline();
    }
    printf("Bye!");
    newline();
}
