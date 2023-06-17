#include <stdio.h>
#include "BlackJack.h"

int main() 
{
  int quit=false;
  char cmd;

  showGameInfo();
  initializedCards();
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
          increasingBet();
          break;
      case 'd':
          decreasingBet();
          break; 
      case 'w':
          washCards();
          break;
      case 'p':
          initializedARound();
          playingARound();
          break;
      case 'q':
          quit=true;
          break;
    }
    if(money<=0)
    {
      printf("You lose all of your money.\n");
      if(isContinue())
      {
        washCards();
        money=1000;
      }
      else
      {
        quit=true;
      }
    }
    else if(cindex>=30)
    {
      washCards();
    }
  }
}
