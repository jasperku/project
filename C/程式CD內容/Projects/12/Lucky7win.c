//設定一付撲克牌
// 0-12 spade
// 13-25 heart
// 26-38 diamond
// 39-51 club
// 0 for A, 1 for 2, ..., 8 for 9, 9 for 10, 10 for J, 11 for Q and 12 for K

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define true 1
#define false 0

int main()
{
   int cards[52];
   char points[] = {'A','2','3','4','5','6','7','8','9','T','J','Q','K'};
   int i, j, temp, quit=0;
   int money=1000, bet=100;
   char cmd;
   int wash=1;
   int current=0;
   

   printf("-------------------------------\n");
   printf("Poker Game: Bigger or Smaller?!\n");
   printf("-------------------------------\n");
   printf("Press h for help.\n\n");
   while(!quit)
   {
      if(bet>money)
         bet=money;
      printf("[$%d][Bet %d] Cards(%d)\n", money, bet, 52-current);
      printf("Bigger or Smaller than 7 (b/s)?");      
      scanf(" %c", &cmd);
      
      // wash cards
      if(wash)
      {
         for(i=0;i<52;i++)
         {
            cards[i]=i;
         }

         srand(time(NULL));

         for(i=0;i<52;i++)
         {
            j = rand()%52;   
            temp = cards[i];
            cards[i] = cards[j];
            cards[j] = temp;      
         }
         wash=false;
         current=0;
      }
      
      switch(cmd)
      {
         case 'h':
            printf("h for help\n");
            printf("i for increasing your bet\n");
            printf("d for decreasing your bet\n");
            printf("b for guessing the card is bigger than 7\n");
            printf("s for guessing the card is smaller than 7\n");
            printf("w for re-washing the cards\n");
            printf("q for quit\n");
            break;         
         case 'i':
            if(bet==money)
               printf("No more money to bet!\n");
            bet=(bet+100)<=money? bet+100 : money;
            break;         
         case 'd':
            if(bet==100)
               printf("Minimum bet is 100!\n");
            bet = bet>=200? bet-100 : 100;
            break;
         case 'w':
            wash=true;
            current=0;
            break;
         case 'b':
         case 's':
            printf("The card is ");
            
            switch(cards[current]/13)
            {
               case 0:
                  printf("%c", '\6');
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
            printf("%c,", points[cards[current]%13]);
            
            if(((cmd=='b')&&(cards[current]%13>=6))||
               ((cmd=='s')&&(cards[current]%13<=6)))
            {
               printf("You win!\n");
               money+=bet;
            }
            else
            {
               printf("You lose!\n");
               money-=bet;
            }
            current++;
            break;
         case 'q':
            quit=1;
      }
      
      if(money<100)
      {
         printf("Game Over!\n");
         quit=1;
      }
      if(current==41)
         wash=true;
   }
   printf("Good Bye!\n");
}

