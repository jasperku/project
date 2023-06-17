#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "Poker.h"

int card[52], cindex;

void initializedCards()
{  
  int i;
  srand(time(NULL));
  for(i=0;i<52;i++)
    card[i]=i;
  washCards();
}
            
void washCards()
{
  int i,j,temp;
  
  for(i=0;i<52;i++)
  {
     j=rand()%52;
     temp=card[i];
     card[i]=card[j];
     card[j]=temp;
  }
  cindex=0;
}

void showACard(int card) 
{
  int p;
  char points[13]={'A','2','3','4','5','6','7','8','9','T','J','Q','K'};

  switch(card/13)
  {
    case 0:
        printf("%c",'\6');
        break;   
    case 1:
        printf("%c",'\3');
        break;
    case 2:
        printf("%c",'\4');
        break;
    case 3: 
        printf("%c",'\5');
        break;
  }  
  printf("%c ", points[card%13]);    
}
