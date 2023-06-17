#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
  int answer, userInput,n, quit;
  char cont;
  srand(time(NULL));
  do
  {
    n=quit=0;
    answer=rand()%100+1;
    printf("Guess a number between 1 and 100: ");
    do
    {
      scanf("%d", &userInput);
      n++;
      if(userInput==answer)
      {
        printf("Congratulations! That’s it.\n");
        printf("You have guessed %d times.\n", n);
        quit=1;
      }
      else if(userInput > answer)
      {
        printf("Too high, try again! ");
      }
      else
      {
        printf("Too low, try again! ");
      }
    } while(!quit);
    printf("Do you want to play it again (y/n)?");
    scanf(" %c", &cont);
  }while(cont!='n');
}