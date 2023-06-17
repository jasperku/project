#include <stdio.h>
#include "StringBox.h"

int main()
{
  int quit=0;
  char cmd;
  

  while(!quit)
  {
    showInfoPrompt();
    cmd=getUserCommand();
    switch(cmd)
    {
      case 'h':
            showHelp();
            break;
      case 'i':
            insertion();
            break;
      case 'd':
            deletion();
            break;
      case 'l':
            showStrings();
            break;
      case 's':
            sortingStrings();
            break;
      case 'q':
            quit=true;
            break;
    }
  }
  printf("Bye.\n");
}