#include <stdio.h>

int main()
{
  int i;

  char *month[] = { "January", 
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
                 "December" };

  for(i=0;i<12;i++)
  {
    printf("&month[%d]=%p month[%d]=%p %s\n", 
           i, &month[i], i, month[i], month[i]);
  }
}
