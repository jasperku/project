#include <stdio.h>

int main()
{
  int i;

  char month[][9] = { "January", 
                      "February", 
                      "March", 
                      "April",
                      "May", 
                      "June", 
                      "July", 
                      "August",
                      "September", 
                      "October", 
                      "November", 
                      "December"};
  for(i=0;i<12;i++)
  {
    printf("%s\n", month[i]);
  }
}
