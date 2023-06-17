#include "StringBox.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char str[numStrings][stringLength];
int count=0;

int readALine(char str[], int n)
{
  int ch, i=0;
  
  while(((ch=getchar())!='\n')&&(i<n))
  {    
    if(!((i==0)&&(ch==' ')))
    {
      str[i++]=ch;
    }
  }
  str[i]='\0';
  return i;
}

void showHelp()
{
  printf("h for help\n");
  printf("i for inserting a new string into the box\n");
  printf("d for deleting an existing string from the box\n");
  printf("l for listing all strings in the box\n");
  printf("s for sorting strings according to the Lexicographic order\n");
  printf("q for quit\n");
}

void showInfoPrompt()
{
  printf("<command> ? ");
}

char getUserCommand()
{
  char c;
  scanf(" %c", &c);
  return c;
}

void insertion()
{
  if(count<numStrings)
  {
    getchar();
    readALine(str[count++], stringLength);
  }
  else
  {
    printf("The string box is full!\n");
  }
}

void showStrings()
{
  int i;
  if(count==0)
  {
    printf("The box is empty!\n");
  }
  else
  {
    for(i=0;i<count;i++)
    {
      printf("%d[%s]\n", i+1, str[i]);
    }
  }
}

void deletion()
{
  int i,n;
  if(count==0)
  {
    printf("Nothing to delete!\n");
  }
  else
  {
    showStrings();
    printf("Which one you want to delete? ");
    scanf(" %d", &n);
    if((n>count)||(n<=0))
    {
      printf("Out of range!\n");
    }
    else
    {
      count--;
      for(i=(n-1); i<count; i++)
      {
        strcpy(str[i], str[i+1]);
      }
      str[i][0]='\0';
    }
  }
}

void sortingStrings()
{
  int i,j;
  char temp[20];
  for(i=0;i<count-1;i++)
  {
    for(j=0; j<count-i-1; j++)
    {
      if(strcmp(str[j], str[j+1]) > 0)
      {
        strcpy(temp, str[j]);
        strcpy(str[j], str[j+1]);
        strcpy(str[j+1], temp);
      }
    }
  }
}