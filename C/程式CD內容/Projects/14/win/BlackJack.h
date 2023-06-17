#include "Poker.h"

#define true 1
#define false 0

#define UserWin 0
#define PCWin 1
#define unknownWinner 2

extern int user[5], pc[5], money, bet;

void showGameInfo();
void showInfoPrompt();
char getUserCommand();
void showHelp();
void increasingBet();
void decreasingBet();
void initializedARound();
void playingARound();
int userTurn();
void showUserCard();
void showPCCard();
void showCards(int c[]);
int pcTurn();
int pcPoint();
int userPoint();
int calculatePoint(int c[]);
int isContinue();
