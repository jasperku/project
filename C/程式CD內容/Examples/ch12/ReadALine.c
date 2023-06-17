#include <stdio.h>

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

int main()
{
  char str[20];

  printf("Please input your name:");
  readALine(str, 20); // 使用自定的readALine()取得使用者輸入的字串
  printf("Your name is %s.\n", str);
}
