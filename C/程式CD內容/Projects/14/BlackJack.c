#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "BlackJack.h"

int user[5], pc[5], money=1000, bet=100;

void showGameInfo()
{
  printf("-------------\n");
  printf(" Black Jack!\n");
  printf("-------------\n\n");
}

void showInfoPrompt()
{
   printf("[$%d][Bet %d] ", money, bet);
   printf("Command (h for help) ?");
}

char getUserCommand()
{
  char c;
  scanf(" %c", &c);
  return c;
}

void showHelp()
{
  printf("h for help\n");
  printf("i for increasing your bet\n");
  printf("d for decreasing your bet\n");
  printf("p for playing this round\n");
  printf("w for re-washing the cards\n");
  printf("q for quit\n");
}               

void increasingBet()
{
  if(bet==money)
    printf("No more money to bet!\n");
  else
    bet=(bet+10)<=money? bet+10 : money;   
}

void decreasingBet()
{
  if(bet==100)
    printf("Minimum bet is 100!\n");
  else
    bet = bet>110? bet-10 : 100;
}

void initializedARound()
{
  user[0]=card[cindex++];
  user[1]=card[cindex++];
  pc[0]=card[cindex++];
  pc[1]=card[cindex++];
  user[2]=user[3]=user[4]=pc[2]=pc[3]=pc[4]=(-1);
}

void playingARound()
{
  int winner;
  if((winner=userTurn())==unknownWinner)
  {
    winner=pcTurn();
    if(winner==UserWin)
    {
      money+=bet;
    }
    else if(winner==PCWin)
    {
      money-=bet;
    }
  }
  else if(winner==UserWin)
  {
     showPCCard(5);
     money+=bet;
  }
  else  // userTurn() returns PCWin
  {
    money-=bet;
  }
}

int userTurn() 
{
  int ucindex=2, quit=0;
  char c;
  showUserCard();

  showPCCard(1);                         
  while((ucindex<5)&&(!quit))
  {
    printf("Add a card?(y/n)");
    scanf(" %c", &c);
    if(c=='y')
    {
      user[ucindex++]=card[cindex++];
      showUserCard();
      if(userPoint()>21)
      {
        showPCCard(5);
        printf("I Win!\n");
        return PCWin;
      }
    }
    else
      quit=true;
  }
  if((ucindex==5)&&(userPoint()<=21))
    return UserWin;
  else
    return unknownWinner;
}

void showUserCard() 
{
  printf("User: ");
  showCards(user);
}

void showPCCard(int i) 
{
  printf(" PC : ");
  if(i!=1)
    showCards(pc);
  else
  {
    showACard(pc[0]);
    printf("\n");
  }
}

void showCards( int c[]) 
{
  int i;
  for(i=0;i<5;i++)
  {
    if(c[i]!=(-1))
    {
      showACard(c[i]);
      printf(" ");
    }
  }
  printf("\n");
}

int pcTurn() 
{
  int pcindex=2, quit=0;
  char c;

  showPCCard(5);
  while((pcindex<=5)&&(pcPoint()<16))
  {
    printf("I want to add a card...\n");
    pc[pcindex++]=card[cindex++];
    showPCCard(5);
  }
  if(pcPoint()>21)
  {
    printf("You Win!\n");
    return UserWin;
  }
  else if(userPoint()>pcPoint())
  {
    printf("You Win!\n");
    return UserWin;
  }
  else if(userPoint()==pcPoint())
  {
    printf("Even! You Win\n");
    return UserWin;
  }
  else
  {
    printf("I Win!\n");
    return PCWin;
  }
}

int pcPoint() 
{
  return calculatePoint(pc);
} 

int userPoint() 
{
  return calculatePoint(user);
}

int calculatePoint(int c[])
{
  int i,p,sum=0, a=0;
  for(i=0;i<5;i++)
  {
    if(c[i]!=(-1))
    {
      p=c[i]%13+1;
      p= (p>10)? 10: p;
      if(p==1)
        a++;
      sum+=p;
    }
  }  
  if(a&&((sum+10)<=21))
    sum+=10;
  return sum;
}

int isContinue() 
{
  char c;

  printf("Do you want to play again?(y/n)");
  scanf(" %c", &c);
  if(c=='y')
    return true;
  else
    return false; 
}