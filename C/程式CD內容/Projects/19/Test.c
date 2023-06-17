#include <stdio.h>
#include "FiveInARow.h"

int main()
{
  char chessboard[19][19];
  int i,j;
  Player winner;
  
  for(i=0;i<19;i++)
    for(j=0;j<19;j++)
      scanf(" %c",&chessboard[i][j]);
      
  for(i=0;i<19;i++)
  {
    for(j=0;j<19;j++)
    {
      printf("%c ", chessboard[i][j]);
    }
    printf("\n");
  }
  
  winner = check4Winner(chessboard);
  if(winner==Black)
    printf("Black win!\n");
  else if(winner==White)
    printf("White Win!\n");
  else
    printf("Even!\n");
}